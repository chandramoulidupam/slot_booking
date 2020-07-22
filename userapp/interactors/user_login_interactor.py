from userapp.constants.custom_exceptions import InvalidPassword,\
        InvalidUsername
from userapp.interactors.storages.storage_interface import StorageInterface
from userapp.interactors.presenters.presenter_interface \
        import PresenterInterface
from common.oauth_user_auth_tokens_service import *


class LoginInteractor:
    def __init__(self, storage: StorageInterface,
                 oauth_storage: OAuth2SQLStorage):
        self.storage = storage
        self.oauth_storage = oauth_storage


    def user_login_wrapper(self,
                           username: str,
                           password: str,
                           presenter: PresenterInterface):
        try:
            return self._get_user_login_response(username, password, presenter)
        except InvalidUsername:
            return presenter.raise_exception_for_invalid_username()
        except InvalidPassword:
            return presenter.raise_exception_for_invalid_password()

    def _get_user_login_response(self, username, password, presenter):
        access_token_dto, user_dto = self.user_login(username, password)
        return presenter.user_login_response(access_token_dto, user_dto.is_admin)

    def user_login(self, username, password):
        username_not_exists = self.storage.validate_username(username=username)
        if not username_not_exists:
            raise InvalidUsername
        check_password = self.storage.validate_password(username=username, password=password)
        if not check_password:
            raise InvalidPassword
        user_dto = self.storage.get_user_id(username)
        storage = OAuth2SQLStorage()
        service = OAuthUserAuthTokensService(oauth2_storage=storage)
        token_dto = service.create_user_auth_tokens(user_id=user_dto.user_id)
        return (token_dto, user_dto)

