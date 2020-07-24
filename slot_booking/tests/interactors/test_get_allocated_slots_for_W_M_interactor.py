import datetime
from unittest.mock import create_autospec, patch
from slot_booking.interactors.get_allocated_slots_for_washing_machine_interactor \
        import AllocatedSlotsForWashingMachineInteractor
from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.dtos.dtos import SlotDto


@patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
def test_get_allocated_slots_with_valid_washing_machine_id_returns_raise_exception(user_is_admin):
    day = "SUNDAY"
    washing_machine_id = "1"
    username = "user1"
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.validate_washing_machine_id.return_value = False
    interactor = AllocatedSlotsForWashingMachineInteractor(
        storage=storage)

    interactor.get_allocated_slots_wrapper(username, washing_machine_id, day, presenter)
    presenter.raise_exception_for_invalid_washing_machine_id()

@patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
def test_get_allocated_slots_with_valid_inputs_returns_list_of_slot_dtos(user_is_admin):
    day = "SUNDAY"
    washing_machine_id = "1"
    username = "user1"
    list_of_slot_dtos = [SlotDto(
        slot_start_time=6,
        slot_end_time=7,
        slot_day="SUNDAY",
        washing_machine_id="1",
    )]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.validate_washing_machine_id.return_value = True
    user_is_admin.return_value = True
    interactor = AllocatedSlotsForWashingMachineInteractor(
        storage=storage)
    interactor.get_allocated_slots_wrapper(username, washing_machine_id, day, presenter)
    presenter.get_allocated_slots_for_washing_machine(list_of_slot_dtos)
#     presenter.raise_exception_for_user_is_admin.assert_called_once()

@patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
def test_allocate_slots_for_washing_machine_details_for_user_raise_exception(user_is_admin):
    day = "SUNDAY"
    washing_machine_id = "1"
    username = "user1"
    list_of_slot_dtos = [SlotDto(
        slot_start_time=6,
        slot_end_time=7,
        slot_day="SUNDAY",
        washing_machine_id="1",
    )]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    user_is_admin.return_value = False
    list_of_slot_dtos = [SlotDto(
        slot_start_time=6,
        slot_end_time=7,
        slot_day="SUNDAY",
        washing_machine_id="1",
    )]
    interactor = AllocatedSlotsForWashingMachineInteractor(
        storage=storage)

    interactor.get_allocated_slots_wrapper(username, washing_machine_id, day, presenter)
    presenter.raise_exception_for_user_is_not_admin.assert_called_once()