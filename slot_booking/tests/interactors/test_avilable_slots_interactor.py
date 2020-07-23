import datetime
from unittest.mock import create_autospec, patch
from slot_booking.interactors.avilable_slots_interactor import AvilableSlotsInteractor
from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.interactors.storages.dtos import SlotDto


@patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
def test_avilable_slots_with_valid_inputs_returns_list_of_slot_dtos(user_is_admin):
    date = datetime.date(2020, 5, 25)
    username = "user1"
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    user_is_admin.return_value = False
    list_of_slot_dtos = [SlotDto(
        slot_start_time=6,
        slot_end_time=7,
        slot_date="25-05-2020",
        washing_machine_id=1,
        slot_status="Avilable"
    )]
    interactor = AvilableSlotsInteractor(
        storage=storage)

    interactor.avilable_slots_wrapper(username, date, presenter)
    presenter.list_of_upcoming_slots(list_of_slot_dtos)


@patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
def test_avilable_slots_with_invalid_inputs_returns_list_of_slot_dtos(user_is_admin):
    date = datetime.date(2020, 5, 25)
    username = "user1"
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    user_is_admin.return_value = True
    interactor = AvilableSlotsInteractor(
        storage=storage)
    interactor.avilable_slots_wrapper(username, date, presenter)
    presenter.raise_exception_for_user_is_admin.assert_called_once()


@patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
def test_avilable_slots_with_invalid_date_returns_list_of_slot_dtos(user_is_admin):
    date = datetime.date(2000, 5, 25)
    username = "user1"
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    user_is_admin.return_value = False
    storage.validate_date.return_value = False
    interactor = AvilableSlotsInteractor(
        storage=storage)

    interactor.avilable_slots_wrapper(username, date, presenter)
    presenter.raise_exception_for_invalid_date.assert_called_once()
