import datetime
import pytest
from slot_booking.dtos.dtos import SlotDto
from slot_booking.storages.slot_storage_implementation import SlotStorageImplementation


@pytest.mark.django_db
class TestAddUpdateSlotsOfWashingMachine:
    def test_add_update_slots_for_washing_machine_with_valid_details_results_list_of_altered_slots(
                self,
                slots,
                washing_machines
    ):
        pass

    def test_add_update_slots_for_w_m_with_invalid_machine_id_raises_exception(self, slots, washing_machines):
        # username = "user1"
        washing_machine_id = "washing_machine_10"
        day = "SUNDAY"
        expected = False
        storage = SlotStorageImplementation()
        # storage.validate_washing_machine_id.return_value = False
        response = storage.validate_washing_machine_id(washing_machine_id)
        # Assert
        assert expected == response
