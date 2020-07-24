# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_list_of_allocated_slots_for_washing_machine"
REQUEST_METHOD = "get"
URL_SUFFIX = "admin/get_allocated_slots_for_washing_machine/{washing_machine_name}/{day}/v1/"


from .test_case_01 import TestCase01GetListOfAllocatedSlotsForWashingMachineAPITestCase

__all__ = [
    "TestCase01GetListOfAllocatedSlotsForWashingMachineAPITestCase"
]

