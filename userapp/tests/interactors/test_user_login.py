import pytest
from userapp.constants.custom_exceptions import InvalidPassword,\
        InvalidUsername
from unittest.mock import create_autospec, patch, Mock
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from userapp.interactors.user_login_interactor import LoginInteractor
from userapp.interactors.presenters.presenter_interface import PresenterInterface
from userapp.interactors.storages.storage_interface import StorageInterface
from userapp.interactors.storages.dtos import AccessTokenDto, UserDto
# @pytest.fixture()
from userapp.presenters.presentation_implementation import INVALIDPASSWORD


class TestUserLoginInteractor:

    def test_given_invalid_username_raises_exception(self):
        # Arrange
        username = "mouli"
        password = "lolololo"
        invalid_username = "mouli"
        # oauth_storage = OAuth2SQLStorage()
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        oauth_storage = create_autospec(OAuth2SQLStorage)
        storage.validate_username.return_value = False
        # presenter.raise_exception_for_invalid_username.side_effect = InvalidUsername
        interactor = LoginInteractor(
            storage=storage,
            oauth_storage=oauth_storage)

        # Act
        with pytest.raises(InvalidUsername):
            interactor.user_login_wrapper(
                username=username,
                password=password,
                presenter=presenter
            )
        # Assert
        storage.validate_username.assert_called_once_with(
            username=invalid_username
        )
        presenter.raise_exception_for_invalid_username.assert_called_once()

    def test_given_invalid_password_raises_exception(self):
        # Arrange
        username = "mouli"
        password = "lololololl"

        oauth_storage = OAuth2SQLStorage(
        )
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        oauth_storage = create_autospec(OAuth2SQLStorage)
        storage.validate_password.return_value = False
        storage.validate_username.return_value = True
        # presenter.raise_exception_for_invalid_password.return_value = mock

        interactor = LoginInteractor(
            storage=storage,
            oauth_storage=oauth_storage
        )

        response = interactor.user_login_wrapper(
            username=username,
            password=password,
            presenter=presenter
        )
        # Assert
        storage.validate_username.assert_called_once_with(
            username=username
        )
        storage.validate_password.assert_called_once_with(
            username=username,
            password=password
        )
        presenter.raise_exception_for_invalid_password.assert_called_once()
        # assert response == mock

    def test_given_valid_username_and_password_returns_tokens(self):
        # Arrange
        username = "un"
        password = "123"
        user_is_admin = True
        user_dto = UserDto(name="mouli",user_id="1",is_admin="False")
        access_token = "12345"
        access_token_dto = {
            "access_token":"12345",
            "refresh_token":"123",
            "expires_in":1000000000}

        storage = create_autospec(StorageInterface)
        storage.validate_password.return_value = True
        storage.validate_username.return_value = True
        oauth_storage = OAuth2SQLStorage()
        # storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.get_user_id.return_value = user_dto

        interactor = LoginInteractor(
            storage=storage,
            oauth_storage=oauth_storage
        )
        # Act
        with patch.object(OAuthUserAuthTokensService,'create_user_auth_tokens', return_value=access_token_dto):
            interactor.user_login_wrapper(
                    username=username,
                    password=password,
                    presenter=presenter
                )

        # Assert
        storage.validate_username.assert_called_once_with(
            username=username
        )
        storage.validate_password.assert_called_once_with(
            username=username,
            password=password
        )
        presenter.user_login_response.assert_called_once_with(token_dto=access_token_dto, user_is_admin=user_dto.is_admin)

