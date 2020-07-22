
from userapp.interactors.get_user_details_interactor import UserProfileInteractor
from userapp.storages.storage_implementation import LoginStorageImplementation


class ServiceInterface:

    @staticmethod
    def user_is_admin(username: str):
        storage = LoginStorageImplementation()
        interactor = UserProfileInteractor(storage=storage)
        user_dto = interactor.user_profile_wrapper(username=username)
        return user_dto.is_admin