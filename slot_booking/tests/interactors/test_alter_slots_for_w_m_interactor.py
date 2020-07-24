import datetime
from unittest.mock import create_autospec, patch
from slot_booking.interactors.update_slots_of_w_m_interactor import UpdateSlotsForWashingMachineInteractor
from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.dtos.dtos import UserSlotDto, SlotDto


@patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
def test_alter_slots_when_user_is_not_admin_raises_exception(user_is_admin):
    day = "SUNDAY"
    username = "user1"
    washing_machine_id = "washing_machine_1"
    slots_dtos = []
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    user_is_admin.return_value = False
    interactor = UpdateSlotsForWashingMachineInteractor(
        storage=storage)

    interactor.update_slots_wrapper(username, washing_machine_id, day, slots_dtos, presenter)
    presenter.raise_exception_for_user_is_not_admin.assert_called_once()

@patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
def test_alter_slots_with_invalid_washing_machine_raises_exception(user_is_admin):
    day = "SUNDAY"
    username = "user1"
    washing_machine_id = "washing_machine_1"
    slots_dtos = []
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    user_is_admin.return_value = True
    storage.validate_washing_machine_id.return_value = False
    interactor = UpdateSlotsForWashingMachineInteractor(
        storage=storage)

    interactor.update_slots_wrapper(username, washing_machine_id, day, slots_dtos, presenter)
    presenter.raise_exception_for_invalid_washing_machine_id.assert_called_once()

@patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
def test_alter_slots_with_invalid_inputs_raises_exception(user_is_admin):
    day = "SUNDAY"
    username = "user1"
    washing_machine_id = "washing_machine_1"
    slots_dtos = []
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    user_is_admin.return_value = True
    storage.validate_washing_machine_id.return_value = True
    storage.validate_given_list_of_slots_dto.return_value = False
    interactor = UpdateSlotsForWashingMachineInteractor(
        storage=storage)

    interactor.update_slots_wrapper(username, washing_machine_id, day, slots_dtos, presenter)
    presenter.raise_exception_for_invalid_inputs.assert_called_once()


@patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
def test_alter_slots_with_valid_inputs_returns_list_of_slot_dtos(user_is_admin):
    day = "SUNDAY"
    username = "user1"
    washing_machine_id = "washing_machine_1"
    slots_dtos = []
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    user_is_admin.return_value = True
    storage.validate_washing_machine_id.return_value = True
    storage.validate_given_list_of_slots_dto.return_value = True
    list_of_slot_dtos = [SlotDto(
        slot_start_time=datetime.time(6, 00, 00),                # (slot_start_time).strftime("%H:%M:%S"),
        slot_end_time= datetime.time(7, 00, 00),                #,(slot_end_time).strftime("%H:%M:%S"),
        slot_day="SUNDAY",
        washing_machine_id="washing_machine_1",
    )]
    interactor = UpdateSlotsForWashingMachineInteractor(
        storage=storage)

    interactor.update_slots_wrapper(username, washing_machine_id, day, slots_dtos, presenter)
    presenter.alter_slots_for_washing_machine_returns_slots_details(list_of_slot_dtos)
