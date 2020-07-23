import datetime

import pytest
from slot_booking.storages.slot_storage_implementation import SlotStorageImplementation


@pytest.mark.django_db
class TestUpcomingSlotsStorager:
    def test_upcoming_slots_with_valid_details_results_list_of_avilable_slots(
                self,
                slots,
                washing_machines
    ):
        username = "user1"
        date = datetime.date(2020, 7, 25)
        expected_slot_dtos = []
        storage = SlotStorageImplementation()
        # storage.validate_washing_machine_number.return_value = True
        response_slot_dto = storage.list_of_upcoming_slot_dtos(
                username=username,
                date=date)
        # Assert
        assert expected_slot_dtos == response_slot_dto

    def test_coming_slots_raises_error_when_invalid_date_is_given(self):
        # username = "user1"
        date = datetime.date(2000, 7, 25)
        expected_slot_dtos = False
        storage = SlotStorageImplementation()
        # storage.validate_washing_machine_number.return_value = True
        response_slot_dto = storage.validate_date(date)
        # Assert
        assert expected_slot_dtos == response_slot_dto
