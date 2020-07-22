import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from userapp.storages.storage_implementation import \
    LoginStorageImplementation


@pytest.mark.django_db
class TestUserSignupStorager:
    def test_username_is_duplicate_or_not(self, users):

        # Arrange
        user1 = users[0]
        username = "user1"
        storage = LoginStorageImplementation()
        username_is_duplicate = True
        # Act
        response = storage.validate_username_for_dupilicate(username=username)

        # Assert
        assert response == username_is_duplicate

    def test_password_is_assigned_to_given_username(self):
        username = "user1"
        password = "password"
        storage = LoginStorageImplementation()
        # Act
        response = storage.assigning_password(username=username, password=password)
        # print(response)
        # Assert
        # assert  response.password == password
