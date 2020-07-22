from userapp.constants.custom_exceptions import UsernameAlreadyExists,\
        InvalidPassword, InvalidUsername
from userapp.interactors.storages.storage_interface import StorageInterface
from userapp.interactors.presenters.presenter_interface \
        import PresenterInterface
from common.oauth_user_auth_tokens_service import *
from userapp.interactors.user_login_interactor import LoginInteractor

class SignUpInteractor:
    def __init__(self, storage: StorageInterface,
                 oauth_storage: OAuth2SQLStorage):
        self.storage = storage
        self.oauth_storage = oauth_storage


    def user_signup_wrapper(self,
                           username: str,
                           password: str,
                           presenter: PresenterInterface):
        try:
            return self._user_signup_response(username, password, presenter)
        except UsernameAlreadyExists:
            print("*************************")
            return presenter.raise_exception_for_username_already_exists()
        except InvalidUsername:
            print("*************************")
            return presenter.raise_exception_for_invalid_username()
        except InvalidPassword:
            return presenter.raise_exception_for_invalid_password()


    def _user_signup_response(self, username, password, presenter):
        access_token_dto, user_dto = self.user_signup(username, password)
        return presenter.user_signup_response(access_token_dto, user_dto.is_admin)

    def user_signup(self, username, password):
        check_username_is_already_exists = self.storage.validate_username_for_dupilicate(username=username)
        print(check_username_is_already_exists)
        if check_username_is_already_exists:
            raise UsernameAlreadyExists
        new_user_obj = self.storage.assigning_password(username=username, password=password)
        user_dto = self.storage.get_user_id(username)
        storage = OAuth2SQLStorage()
        service = OAuthUserAuthTokensService(oauth2_storage=storage)
        token_dto = service.create_user_auth_tokens(user_id=user_dto.user_id)
        return (token_dto, user_dto)