import json

import pytest
from userapp.presenters.presentation_implementation import \
    UserLoginPresenterImplementation, INVALIDPASSWORD, INVALIDUSERNAME
from userapp.constants.custom_exceptions import InvalidPassword,\
        InvalidUsername
from django_swagger_utils.drf_server.exceptions import NotFound
from userapp.constants.exception_messages import INVALID_PASSWORD, INVALID_USERNAME


# def test_user_login_with_valid_credentials():
#
#     # Arrange
#     presenter = UserLoginPresenterImplementation()
#     user_is_admin = False
#     token = "12345"
#     expected_output = {'access_token': '12345', 'is_admin': False}
#
#     # Act
#     response = presenter.user_login_response(token_dto=token, user_is_admin=user_is_admin)
#     response = json.loads(response.content)
#     # Assert
#     assert response == expected_output


def test_user_login_with_invalid_username_raises_exception():
    presenter = UserLoginPresenterImplementation()

    excepted_response = {
        "response": INVALIDUSERNAME[0],
        "http_status_code": INVALIDUSERNAME[1],
        "res_status": 403
    }

    response = presenter.raise_exception_for_invalid_username()
    response = json.loads(response.content)
    assert  response == excepted_response



def test_user_login_with_invalid_password_raises_exception():
    presenter = UserLoginPresenterImplementation()
    expected_response = {
        "response": INVALIDPASSWORD[0],
        "http_status_code": INVALIDPASSWORD[1],
        "res_status": 403
    }

    response = presenter.raise_exception_for_invalid_password()
    response = json.loads(response.content)
    # Assert
    assert response == expected_response
