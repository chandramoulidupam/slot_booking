from userapp.interactors.storages.storage_interface import StorageInterface
from oauth2_provider.models import AccessToken
from django.contrib.auth.hashers import check_password
from userapp.interactors.storages.dtos import AccessTokenDto, UserDto
from userapp.constants.custom_exceptions import InvalidPassword,\
        InvalidUsername
from django.core.exceptions import ObjectDoesNotExist

from userapp.models.models import User


class LoginStorageImplementation(StorageInterface):

    def validate_username(self, username: str):
        is_user_exists = User.objects.filter(username=username).exists()

        if is_user_exists:
            return True
        else :
            return False


    def validate_password(self, username: str, password: str) :
        from userapp.models.models import User
        user = User.objects.get(username=username)
        return user.check_password(password)

    def get_user_id(self, username: str):
        from userapp.models.models import User
        user_obj = User.objects.get(username=username)
        user_dto = self._get_user_dto(user_obj)
        print("*" * 10, user_dto)
        return user_dto

    def _get_user_dto(self, user_obj):
        user_dto = UserDto(
            user_id = user_obj.id,
            name = user_obj.name,
            is_admin = user_obj.is_admin
        )
        return user_dto

    def validate_username_for_dupilicate(self, username: str) -> bool:
        from userapp.models.models import User
        return User.objects.filter(username=username).exists()

    def assigning_password(self, username: str, password: str) :
        # from django.contrib.auth.models import User
        from userapp.models.models import User
        user = User.objects.create_user(username=username,password=password)
        user.save()
        # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%", user.password)
        user_obj = User.objects.get(username=username)
        user_obj.set_password(password)
        user_obj.save()
        # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%", user.password)
        return  user_obj

    def user_profile_dto(self, username):
        user_obj = User.objects.get(username=username)
        response_user_dto = self._get_user_dto(user_obj)
        return response_user_dto