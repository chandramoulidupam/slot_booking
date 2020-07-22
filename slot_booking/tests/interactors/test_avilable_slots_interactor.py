import pytest
from unittest.mock import create_autospec, patch, Mock
from slot_booking.interactors.avilable_slots_interactor import AvilableSlotsInteractor
from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.interactors.storages.dtos import SlotDto

class TestAvilableSlotsInteractor:

    def test_avilable_slots_with_valid_date_returns_list_of_slot_dtos(self):
        date = "25-07-2020"
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        list_of_slot_dtos = [SlotDto(
            slot_start_time= 6,
            slot_end_time=7,
            slot_date="25-05-2020",
            washing_machine_id=1,
            slot_status="Avilable"
        )]
        interactor = AvilableSlotsInteractor(
            storage=storage)
        response = interactor.avilable_slots(date)
        presenter.list_of_avilable_slots(list_of_slot_dtos)