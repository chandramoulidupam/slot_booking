# pylint: disable=wrong-import-position

APP_NAME = "userapp"
OPERATION_NAME = "get_user_profile"
REQUEST_METHOD = "get"
URL_SUFFIX = "user/profile/v1/"


from .test_case_01 import TestCase01GetUserProfileAPITestCase

__all__ = [
    "TestCase01GetUserProfileAPITestCase"
]

