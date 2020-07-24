# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "alter_a_slot_for_washing_machine"
REQUEST_METHOD = "post"
URL_SUFFIX = "admin/add_update_washing_machine_slots/{washing_machine_name}/{day}/v1/"


from .test_case_01 import TestCase01AlterASlotForWashingMachineAPITestCase

__all__ = [
    "TestCase01AlterASlotForWashingMachineAPITestCase"
]

