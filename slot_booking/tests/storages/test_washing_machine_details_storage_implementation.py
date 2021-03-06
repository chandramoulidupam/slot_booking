import pytest
from slot_booking.storages.washing_machine_storage_implementation \
        import WashingMachineStorageImplementation
from slot_booking.tests.factories.models import WashingMachineFactory
from slot_booking.dtos.dtos import WashingMachineDto



@pytest.mark.django_db
class TestWashingmachinedetailsStorager:
    def test_washing_machine_details_with_with_valid_inputs_returns_w_m_dto(self):
        WashingMachineFactory.create_batch(size=2, washing_machine_status="ACTIVE")
        # WashingMachineFactory()
        washing_machine_status = "ACTIVE"
        expected_washing_machine_dto = [
                WashingMachineDto(
                        washing_machine_id='washing_machine_1',
                        washing_machine_status='ACTIVE'),
                WashingMachineDto(
                        washing_machine_id='washing_machine_2',
                        washing_machine_status='ACTIVE'
                )
            ]
        storage = WashingMachineStorageImplementation()
        # storage.validate_washing_machine_number.return_value = True
        response_user_dto = storage.washing_machine_details_dto(
                washing_machine_status=washing_machine_status
            )
        # Assert
        assert response_user_dto == expected_washing_machine_dto

    def test_add_washing_machine_raises_error_when_user_is_not_admin(self):
        invalid_washing_machine_id = ""
        storage = WashingMachineStorageImplementation()
        expected_output = False
        # Act
        response = storage.validate_washing_machine_id(
                washing_machine_id=invalid_washing_machine_id
            )

        # Assert
        assert response == expected_output
