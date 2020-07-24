# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "adding_washing_machine"
REQUEST_METHOD = "post"
URL_SUFFIX = "admin/add_washing_machine/v1/"


from .test_case_01 import TestCase01AddingWashingMachineAPITestCase

__all__ = [
    "TestCase01AddingWashingMachineAPITestCase"
]

