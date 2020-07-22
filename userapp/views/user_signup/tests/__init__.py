# pylint: disable=wrong-import-position

APP_NAME = "userapp"
OPERATION_NAME = "user_signup"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/signup/v1/"

from .test_case_01 import TestCase01UserSignupAPITestCase

__all__ = [
    "TestCase01UserSignupAPITestCase"
]
