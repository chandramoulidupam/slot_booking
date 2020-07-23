from unittest.mock import create_autospec, patch
from slot_booking.interactors.add_washing_machine_interactor import AddWashingMachineInteractor
from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.dtos.dtos import WashingMachineDto


class TestAddWashingmachineInteractor:

    @patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
    def test_add_washing_machine_with_invalid_washing_machine_id(self, user_is_admin):
        username = "user1"
        added_washing_id = "washing_machine_1"
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        user_is_admin.return_value = True
        storage.validate_washing_machine_id.return_value = False
        interactor = AddWashingMachineInteractor(
            storage=storage
        )

        interactor.add_washing_machine_wrapper(
                washing_machine_id=added_washing_id,
                username=username,
                presenter=presenter
        )
        # Assert
        storage.validate_washing_machine_id.assert_called_once_with(
            added_washing_id
        )
        presenter.raise_exception_for_invalid_washing_machine_id.assert_called_once()

    @patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
    def test_add_washing_machine_when_user_is_not_admin(self, user_is_admin):
        username = "user1"
        added_washing_id = "washing_machine_1"
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        user_is_admin.return_value = False
        storage.validate_washing_machine_id.return_value = True
        interactor = AddWashingMachineInteractor(
            storage=storage
        )

        interactor.add_washing_machine_wrapper(
            washing_machine_id=added_washing_id,
            username=username,
            presenter=presenter
        )
        # Assert
        presenter.raise_exception_for_user_is_not_admin.assert_called_once()

    @patch('userapp.interfaces.service_interface.ServiceInterface.user_is_admin')
    def test_add_washing_machine_with_valid_number_returns_washing_machine_dtos(self, user_is_admin):
        username = "user1"
        added_washing_id = "washing_machine_1"
        washing_machine_status = "ACTIVE"
        added_washing_dto = WashingMachineDto(
                washing_machine_id=added_washing_id,
                washing_machine_status=washing_machine_status
        )
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        user_is_admin.return_value = False
        storage.validate_washing_machine_id.return_value = True
        interactor = AddWashingMachineInteractor(
            storage=storage
        )

        interactor.add_washing_machine_wrapper(
                washing_machine_id=added_washing_id,
                username=username,
                presenter=presenter
        )
        # Assert
        presenter.get_added_washing_machine_details(added_washing_dto)
