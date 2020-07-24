# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_list_of_upcoming_slots"
REQUEST_METHOD = "get"
URL_SUFFIX = "slot/upcoming_slots/{date}/v1/"


from .test_case_01 import TestCase01GetListOfUpcomingSlotsAPITestCase

__all__ = [
    "TestCase01GetListOfUpcomingSlotsAPITestCase"
]

