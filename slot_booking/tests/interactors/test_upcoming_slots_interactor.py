import pytest
from unittest.mock import create_autospec, patch, Mock
from slot_booking.interactors.upcoming_slots_interactor import UpcomingSlotsInteractor
from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.interactors.storages.dtos import SlotDto

# class TestUpcomingSlotsInteractor:
@patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
def test_upcoming_slots_with_valid_inputs_returns_list_of_slot_dtos(user_is_admin):
        date = "25-07-2020"
        username = "user1"
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        user_is_admin.return_value = False
        list_of_slot_dtos = [SlotDto(
            slot_start_time= 6,
            slot_end_time=7,
            slot_date="25-05-2020",
            washing_machine_id=1,
            slot_status="Avilable"
        )]
        interactor = UpcomingSlotsInteractor(
            storage=storage)

        interactor.upcoming_slots(date, username)
        presenter.list_of_upcoming_slots(list_of_slot_dtos)

@patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
def test_upcoming_slots_with_invalid_inputs_returns_list_of_slot_dtos(user_is_admin):
        date = "25-07-2020"
        username = "user1"
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        user_is_admin.return_value = True
        interactor = UpcomingSlotsInteractor(
            storage=storage)

        interactor.upcoming_slots_wrapper(date, username, presenter)
        presenter.raise_exception_for_user_is_admin.assert_called_once()