import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from userapp.storages.storage_implementation import LoginStorageImplementation
from userapp.interactors.storages.dtos import UserDto


@pytest.mark.django_db
class TestUserProfileStorager:
    def test_user_profile_get_user_dto(self, users):
        user1 = users[0]
        username = user1.username
        expected_user_dto = UserDto(user_id =1, name="", is_admin=True)
        storage = LoginStorageImplementation()
        response_user_dto = storage.user_profile_dto(username=username)
        # Assert
        assert  response_user_dto == expected_user_dto