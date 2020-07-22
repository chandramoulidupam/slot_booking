from datetime import datetime
from abc import abstractmethod, ABC
from typing import Optional, List

class StorageInterface(ABC):

    @abstractmethod
    def validate_username(self, username: str) -> bool:
        pass

    @abstractmethod
    def validate_password(self, username: str, password: str) ->bool:
        pass

    # @abstractmethod
    # def user_login(self, username: str, password: str) ->bool:
    #     pass

    @abstractmethod
    def get_user_id(self, username):
        pass

    @abstractmethod
    def validate_username_for_dupilicate(self, username: str) -> bool:
        pass

    @abstractmethod
    def assigning_password(self, username: str, password: str) :
        pass

    @abstractmethod
    def user_profile_dto(self, username):
        pass