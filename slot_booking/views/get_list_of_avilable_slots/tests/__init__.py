# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_list_of_avilable_slots"
REQUEST_METHOD = "get"
URL_SUFFIX = "slot/avilable_slots/{date}/v1/"


from .test_case_01 import TestCase01GetListOfAvilableSlotsAPITestCase

__all__ = [
    "TestCase01GetListOfAvilableSlotsAPITestCase"
]

