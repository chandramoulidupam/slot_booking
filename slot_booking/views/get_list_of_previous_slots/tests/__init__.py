# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_list_of_previous_slots"
REQUEST_METHOD = "get"
URL_SUFFIX = "slot/previous_slots/v1/"


from .test_case_01 import TestCase01GetListOfPreviousSlotsAPITestCase

__all__ = [
    "TestCase01GetListOfPreviousSlotsAPITestCase"
]

