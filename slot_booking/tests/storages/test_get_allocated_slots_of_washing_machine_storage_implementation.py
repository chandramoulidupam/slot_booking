import datetime
import pytest
from freezegun import freeze_time

from slot_booking.dtos.dtos import SlotDto
from slot_booking.storages.slot_storage_implementation import SlotStorageImplementation
from slot_booking.tests.factories.models import WashingMachineFactory, SlotFactory


# @freeze_time("2020-07-24 6:00:00")
@pytest.mark.django_db
class TestGetAllocatedSlotsOfWashingMachine:

    def test_get_allocated_slots_with_valid_details_results_list_of_allocated_slots(
                self
    ):
        washing_machine = WashingMachineFactory()
        SlotFactory(
                slot_start_time=datetime.time(6, 00, 33, 174867),
                slot_end_time=datetime.time(7, 00, 33, 174878),
                washing_machine_id=washing_machine,
                slot_day="SUNDAY")
        SlotFactory(
            slot_start_time=datetime.time(7, 30, 33, 175177),
            slot_end_time=datetime.time(8, 30, 33, 174878),
            washing_machine_id=washing_machine,
            slot_day="SUNDAY")
        slot_day = "SUNDAY"
        expected_slot_dtos = [
                SlotDto(
                        slot_start_time=datetime.time(6, 0, 33, 174867),
                        slot_end_time=datetime.time(7, 0, 33, 174878),
                        slot_day='SUNDAY', washing_machine_id='washing_machine_1'
                        ),
                SlotDto(
                        slot_start_time=datetime.time(7, 30, 33, 175177),
                        slot_end_time=datetime.time(8, 30, 33, 174878),
                        slot_day='SUNDAY', washing_machine_id='washing_machine_1'
                        )
            ]
        storage = SlotStorageImplementation()
        response_allocated_slot_dtos = storage.allocated_slot_dtos(
            washing_machine.washing_machine_id, slot_day)
        assert response_allocated_slot_dtos == expected_slot_dtos

    def test_get_allocated_slots_with_invalid_machine_id_raises_exception(self, slots, washing_machines):
        washing_machine_id = "washing_machine_10"
        day = "SUNDAY"
        expected = False
        storage = SlotStorageImplementation()
        response = storage.validate_washing_machine_id(washing_machine_id)
        # Assert
        assert expected == response
