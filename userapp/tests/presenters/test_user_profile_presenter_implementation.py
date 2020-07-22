import json

import pytest
from userapp.presenters.presentation_implementation import \
    UserLoginPresenterImplementation, INVALIDUSERNAME
from userapp.interactors.storages.dtos import UserDto


def test_get_user_profile_returns_user_profile_details():
    presenter = UserLoginPresenterImplementation()
    user_profile_dto = UserDto(user_id =1, name="", is_admin=True)

    expected_user_profile = {'is_admin': True, 'name': '', 'user_id': 1}
    response_profile_details = presenter.user_profile_details(user_profile_dto=user_profile_dto)
    response = json.loads(response_profile_details.content)

    # Assert
    assert response == expected_user_profile