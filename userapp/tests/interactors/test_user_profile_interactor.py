import pytest
from userapp.constants.custom_exceptions import InvalidUsername
from unittest.mock import create_autospec, patch, Mock

from userapp.interactors.get_user_details_interactor import UserProfileInteractor
from userapp.interactors.presenters.presenter_interface import PresenterInterface
from userapp.interactors.storages.storage_interface import StorageInterface
from userapp.interactors.storages.dtos import  UserDto


class TestUserLoginInteractor:

    def test_given_invalid_username_raises_exception(self):
        # Arrange
        username = "mouli"
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.validate_username.return_value = True
        # presenter.raise_exception_for_invalid_username.side_effect =
        interactor = UserProfileInteractor(
            storage=storage)

        # Act
        interactor.user_profile_wrapper(
            username=username,
            presenter=presenter
        )
        # Assert
        storage.validate_username.assert_called_once_with(
            username=username
        )
        presenter.raise_exception_for_invalid_username.assert_called_once()

    def test_user_profile_with_valid_details(self):
        username = "mouli"
        user_dto = UserDto(user_id=1, name = "", is_admin=False)
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.validate_username.return_value = False
        # presenter.raise_exception_for_invalid_username.side_effect =
        interactor = UserProfileInteractor(
            storage=storage)

        # Act
        interactor.user_profile_wrapper(
            username=username,
            presenter=presenter
        )
        # Assert
        storage.validate_username.assert_called_once_with(
            username=username
        )
        presenter.user_profile_details.assert_called_once(user_profile_dto=user_dto)