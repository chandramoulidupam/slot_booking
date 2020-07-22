from userapp.constants.custom_exceptions import \
        InvalidUsername
from userapp.interactors.storages.storage_interface import StorageInterface
from userapp.interactors.presenters.presenter_interface \
        import PresenterInterface

class UserProfileInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def user_profile_wrapper(self, username=str, presenter=PresenterInterface):
        try:
            return self._get_user_profile_response(username, presenter)
        except InvalidUsername:
            return presenter.raise_exception_for_invalid_username()


    def _get_user_profile_response(self, username, presenter):
        user_profile_dto = self.get_user_profile(username)
        return presenter.user_profile_details(user_profile_dto)

    def get_user_profile(self, username):
        username_not_exists = self.storage.validate_username(username=username)
        if username_not_exists:
            raise InvalidUsername
        user_profile_dto = self.storage.user_profile_dto(username)
        return user_profile_dto