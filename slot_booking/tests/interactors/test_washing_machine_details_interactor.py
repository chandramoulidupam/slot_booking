import datetime
from unittest.mock import create_autospec, patch
from slot_booking.interactors.washing_machines_details_interactor import WashingMachineDetailsInteractor
from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.dtos.dtos import SlotDto, WashingMachineDto


@patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
def test_get_washing_machine_details_with_valid_inputs_returns_list_of_washing_machine_dtos(user_is_admin):
    washing_machine_status = "ACTIVE"
    username = "user1"
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    user_is_admin.return_value = False
    washing_machine_details_dto = [WashingMachineDto(
        washing_machine_id="1",
        washing_machine_status="ACTIVE",
    )]
    interactor = WashingMachineDetailsInteractor(
        storage=storage)

    interactor.washing_machine_details_wrapper(username, washing_machine_status, presenter)
    presenter.get_washing_machine_details(washing_machine_details_dto)


@patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
def test_get_washing_machine_details_for_user_raise_exception(user_is_admin):
    washing_machine_status = "ACTIVE"
    username = "user1"
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    user_is_admin.return_value = False
    list_of_slot_dtos = [SlotDto(
        slot_start_time=6,
        slot_end_time=7,
        slot_day="SUNDAY",
        washing_machine_id="1",
    )]
    interactor = WashingMachineDetailsInteractor(
        storage=storage)

    interactor.washing_machine_details_wrapper(username, washing_machine_status, presenter)
    presenter.raise_exception_for_user_is_not_admin.assert_called_once()