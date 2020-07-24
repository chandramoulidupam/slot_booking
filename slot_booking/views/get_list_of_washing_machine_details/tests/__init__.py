# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_list_of_washing_machine_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "admin/get_washing_machines_details/v1/"


from .test_case_01 import TestCase01GetListOfWashingMachineDetailsAPITestCase

__all__ = [
    "TestCase01GetListOfWashingMachineDetailsAPITestCase"
]

