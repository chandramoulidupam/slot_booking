import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from slot_booking.storages.slot_storage_implementation import SlotStorageImplementation
from slot_booking.dtos.dtos import SlotDto


@pytest.mark.django_db
class TestPreviousSlotsStorager:
    def test_previous_slots_with_valid_details_results_list_of_avilable_slots(self, slots, washing_machines):
        username = "user1"
        date = "2020-07-25"
        expected_slot_dtos = []
        storage = SlotStorageImplementation()
        # storage.validate_washing_machine_number.return_value = True
        response_slot_dto = storage.list_of_previous_slot_dtos(username=username,date=date)
        # Assert
        assert  expected_slot_dtos == response_slot_dto

    def test_previous_slots_raises_error_when_invalid_date_is_given(self):
        username = "user1"
        date = "2000-07-25"
        expected_slot_dtos = False
        storage = SlotStorageImplementation()
        # storage.validate_washing_machine_number.return_value = True
        response_slot_dto = storage.validate_date(date)
        # Assert
        assert expected_slot_dtos == response_slot_dto