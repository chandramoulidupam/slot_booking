import pytest
from unittest.mock import create_autospec, patch, Mock
from slot_booking.interactors.add_washing_machine_interactor import AddWashingMachineInteractor
from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.interactors.storages.dtos import WashingMachineDto

class TestAddWashingmachineInteractor:
    def test_add_washing_machine_with_invalid_washing_machine_number(self):
        added_washing_number = "washing_machine_1"
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.validate_washing_machine_number.return_value = False
        interactor = AddWashingMachineInteractor(
            storage=storage
        )

        response = interactor.add_washing_machine_wrapper(
            washing_machine_number=added_washing_number,
            presenter=presenter
        )
        # Assert
        storage.validate_washing_machine_number.assert_called_once_with(
            washing_machine_number=added_washing_number
        )
        presenter.raise_exception_for_invalid_washing_machine_number.assert_called_once()

    def test_add_washing_machine_with_valid_number_returns_washing_machine_dtos(self):
        added_washing_number = "washing_machine_1"
        added_washing_dto = WashingMachineDto(washing_machine_number=added_washing_number)
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.validate_washing_machine_number.return_value = True
        interactor = AddWashingMachineInteractor(
            storage=storage
        )

        response = interactor.add_washing_machine_wrapper(
            washing_machine_number=added_washing_number,
            presenter=presenter
        )
        # Assert
        storage.validate_washing_machine_number.assert_called_once_with(
            washing_machine_number=added_washing_number
        )
        presenter.get_added_washing_machine_details(added_washing_dto)