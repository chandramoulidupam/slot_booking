import enum

from ib_common.constants import BaseEnumClass


class SlotStatus(BaseEnumClass, enum.Enum):
    Avilable = "Avilable"
    Unavilable = "Unavilable"


class BookedStatus(BaseEnumClass, enum.Enum):
    BOOKED = "BOOKED"
    NOTBOOKED = "NOTBOOKED"

class WashingMachineStatus(BaseEnumClass, enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class SlotDays(BaseEnumClass, enum.Enum):
    SUNDAY = "SUNDAY"
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
