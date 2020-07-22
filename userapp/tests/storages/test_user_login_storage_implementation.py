import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from userapp.storages.storage_implementation import \
    LoginStorageImplementation


@pytest.mark.django_db
class TestUserLoginStorager:
    def test_username_is_valid_or_not(self, users):

        # Arrange
        user1 = users[0]
        user1 = user1.username
        storage = LoginStorageImplementation()
        username_is_valid = True
        # Act
        response = storage.validate_username(username=user1)

        # Assert
        assert response == username_is_valid

    def test_password_is_valid(self, users):
        # Arrange
        user1 = users[0]
        username1 = user1.username
        password1 = user1.password
        storage = LoginStorageImplementation()
        # Act
        response = storage.validate_password(username=username1, password=password1)
        # Assert
        assert response == False

    def test_user_name_raises_error_when_invalid_username_is_given(self, users):
        invalid_username = "lololol"
        storage = LoginStorageImplementation()
        expected_output = False
        # Act
        response = storage.validate_username(username=invalid_username)

        # Assert
        assert response == expected_output

    def test_user_password_raises_error_when_invalid_password_is_given(self, users):
        user1 = users[0]
        invalid_password = "lololol"
        storage = LoginStorageImplementation()
        expected_output = False
        username1 = user1.username
        # Act
        response = storage.validate_password(username=username1, password=invalid_password)

        # Assert
        assert response == expected_output