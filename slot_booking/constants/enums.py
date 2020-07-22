import enum

from ib_common.constants import BaseEnumClass


class SlotStatus(BaseEnumClass, enum.Enum):
    Avilable = "Avilable"
    Unavilable = "Unavilable"


class BookedStatus(BaseEnumClass, enum.Enum):
    Booked = "Booked"
    NotBooked = "NotBooked"