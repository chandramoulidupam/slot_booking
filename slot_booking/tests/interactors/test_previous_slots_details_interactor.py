import datetime
from unittest.mock import create_autospec, patch
from slot_booking.interactors.previous_slots_interactor import PreviousSlotsInteractor
from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.dtos.dtos import UserSlotDto


@patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
def test_previous_slots_with_valid_inputs_returns_list_of_slot_dtos(user_is_admin):
    date = datetime.date(2020, 5, 25)
    username = "user1"
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    user_is_admin.return_value = False
    list_of_slot_dtos = [UserSlotDto(
        slot_start_time=6,
        slot_end_time=7,
        slot_date="25-05-2020",
        washing_machine_id=1,
    )]
    interactor = PreviousSlotsInteractor(
        storage=storage)

    interactor.previous_slots(date, username)
    presenter.list_of_previous_slots(list_of_slot_dtos)


@patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
def test_previous_slots_with_invalid_inputs_returns_list_of_slot_dtos(user_is_admin):
    date = datetime.date(2020, 7, 25)
    username = "user1"
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    user_is_admin.return_value = True
    interactor = PreviousSlotsInteractor(
        storage=storage)

    interactor.previous_slots_wrapper(date, username, presenter)
    presenter.raise_exception_for_user_is_admin.assert_called_once()
