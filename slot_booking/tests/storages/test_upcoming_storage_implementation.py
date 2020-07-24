import datetime

import pytest
from slot_booking.storages.slot_storage_implementation import SlotStorageImplementation
from slot_booking.tests.factories.models import WashingMachineFactory, UserSlotFactory
from slot_booking.dtos.dtos import UserSlotDto



@pytest.mark.django_db
class TestUpcomingSlotsStorager:
    def test_upcoming_slots_with_valid_details_results_list_of_avilable_slots(self):
        washing_machine = WashingMachineFactory()
        UserSlotFactory(
            user_slot_start_time=datetime.time(6, 00, 33, 174867),
            user_slot_end_time=datetime.time(7, 00, 33, 174878),
            washing_machine_id=washing_machine,
            user_slot_date=datetime.date(2020, 8, 2),
            user_slot_status="BOOKED",
            slot_username="username_1"
        )
        UserSlotFactory(
            user_slot_start_time=datetime.time(7, 30, 33, 175177),
            user_slot_end_time=datetime.time(8, 30, 33, 174878),
            washing_machine_id=washing_machine,
            user_slot_date=datetime.date(2020, 8, 12),
            user_slot_status="BOOKED",
            slot_username="username_1"
        )
        username = "user1"
        date = datetime.date(2020, 7, 25)
        expected_slot_dtos = [
                UserSlotDto(
                        user_slot_date=datetime.date(2020, 8, 2),
                        user_slot_start_time=datetime.time(6, 0, 33, 174867),
                        user_slot_end_time=datetime.time(7, 0, 33, 174878),
                        washing_machine_id='washing_machine_1'
                    ),
                UserSlotDto(
                        user_slot_date=datetime.date(2020, 8, 12),
                        user_slot_start_time=datetime.time(7, 30, 33, 175177),
                        user_slot_end_time=datetime.time(8, 30, 33, 174878),
                        washing_machine_id='washing_machine_1'
                    )
            ]
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
