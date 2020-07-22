import pytest
from django_swagger_utils.drf_server.exceptions import NotFound

from userapp.constants.custom_exceptions import InvalidPassword,\
        UsernameAlreadyExists
from unittest.mock import create_autospec, patch, Mock
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from userapp.interactors.user_sign_up_interactor import SignUpInteractor
from userapp.interactors.presenters.presenter_interface import PresenterInterface
from userapp.interactors.storages.storage_interface import StorageInterface
from userapp.interactors.storages.dtos import UserDto
@pytest.mark.django_db
class TestUserSignupInteractor:

    def test_given_username_already_exists_then_raises_exception(self, users):
        # Arrange
        user1 = users[0]
        username = user1.username
        password = "000000000"
        mock = Mock()
        # oauth_storage = OAuth2SQLStorage()
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        oauth_storage = create_autospec(OAuth2SQLStorage)
        storage.validate_username_for_dupilicate.return_value = True
        # presenter.raise_exception_for_username_already_exists.side_effect = NotFound
        interactor = SignUpInteractor(
            storage=storage,
            oauth_storage=oauth_storage
        )

        # Act
        # with pytest.raises(UsernameAlreadyExists):
        response = interactor.user_signup_wrapper(
                    username=username,
                    password=password,
                    presenter=presenter
                )
        print(response)

        # Assert
        storage.validate_username_for_dupilicate.assert_called_once_with(
            username=username
        )
        presenter.raise_exception_for_username_already_exists.assert_called_once()
        # assert response == mock

    def test_given_valid_username_and_password_returns_tokens(self):
        # Arrange
        username = "un"
        password = "123"
        user_dto = UserDto( user_id=1, name="mouli",is_admin="False")
        access_token = "12345"
        access_token_dto = {
            "access_token":"12345",
            "refresh_token":"123",
            "expires_in":1000000000}
        oauth_storage = OAuth2SQLStorage()
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.validate_username_for_dupilicate.return_value = False
        storage.get_user_id.return_value = user_dto

        interactor = SignUpInteractor(
            storage=storage,
            oauth_storage=oauth_storage
        )
        mock_response = {
            "access_token": "some_access_token",
            "refresh_token": "some_refresh_token"
        }

        # Act
        with patch.object(OAuthUserAuthTokensService,'create_user_auth_tokens', return_value=access_token_dto):
            interactor.user_signup_wrapper(username=username, password=password, presenter=presenter)

        storage.validate_username_for_dupilicate.assert_called_once_with(
            username=username
        )

        presenter.user_signup_response.assert_called_once_with(token_dto=access_token_dto, user_is_admin=user_dto.is_admin)

