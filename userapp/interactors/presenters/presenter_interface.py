from abc import abstractmethod
from typing import List

class PresenterInterface:

    @abstractmethod
    def raise_exception_for_invalid_username(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_password(self):
        pass

    @abstractmethod
    def user_login_response(self, token_dto, user_is_admin):
        pass

    @abstractmethod
    def raise_exception_for_username_already_exists(self):
        pass

    @abstractmethod
    def user_signup_response(self, token_dto, user_is_admin):
        pass

    @abstractmethod
    def user_profile_details(self, user_profile_dto):
        pass