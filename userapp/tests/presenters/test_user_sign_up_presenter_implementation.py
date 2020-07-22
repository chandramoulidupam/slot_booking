import json

import pytest
from userapp.presenters.presentation_implementation import \
    UserLoginPresenterImplementation
from userapp.constants.custom_exceptions import InvalidPassword,\
        InvalidUsername, UsernameAlreadyExists
from django_swagger_utils.drf_server.exceptions import NotFound
from userapp.constants.exception_messages import INVALID_PASSWORD, INVALID_USERNAME, USERNAME_ALREADY_EXISTS


# def test_user_to_login_when_sign_up_is_success():
#     presenter = UserLoginPresenterImplementation()
#     token = "12345"
#     user_is_admin = False
#     expected_output = {'access_token': '12345', 'is_admin': False}
#     response = presenter.user_signup_response(token_dto=token, user_is_admin=user_is_admin)
#     response = json.loads(response.content)
#     # Assert
#     assert response == expected_output


@pytest.mark.django_db
def test_user_signup_with_duplicate_username_raises_exception():
    presenter = UserLoginPresenterImplementation()
    expected_message = {
                "response": USERNAME_ALREADY_EXISTS[0],
                "http_status_code": USERNAME_ALREADY_EXISTS[1],
                "res_status": 403
            }

    response = presenter.raise_exception_for_username_already_exists()
    response = json.loads(response.content)

    assert  response == expected_message
