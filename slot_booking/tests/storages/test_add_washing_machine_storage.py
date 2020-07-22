import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from slot_booking.storages.washing_machine_storage_implementation import WashingMachineStorageImplementation
from slot_booking.dtos.dtos import WashingMachineDto


@pytest.mark.django_db
class TestAddedWashingmachineStorager:
    def test_adding_washing_machine(self):
        new_washing_machine_number = "washing_machine_2"
        new_washing_machine_number = new_washing_machine_number
        expected_washing_machine_dto = WashingMachineDto(washing_machine_number=new_washing_machine_number)
        storage = WashingMachineStorageImplementation()
        # storage.validate_washing_machine_number.return_value = True
        response_user_dto = storage.get_added_washing_machine_dto(washing_machine_number=new_washing_machine_number)
        # Assert
        assert  response_user_dto == expected_washing_machine_dto

    def test_add_washing_machine_raises_error_when_invalid_machine_number_is_given(self):
        invalid_washing_machine_number = ""
        storage = WashingMachineStorageImplementation()
        expected_output = False
        # Act
        response = storage.validate_washing_machine_number(washing_machine_number=invalid_washing_machine_number)

        # Assert
        assert response == expected_output
