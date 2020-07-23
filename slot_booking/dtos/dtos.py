from dataclasses import dataclass
# from typing import List, Optional
from datetime import datetime
from slot_booking.constants.enums import SlotStatus


@dataclass
class SlotDto:
    slot_start_time: datetime
    slot_end_time: datetime
    slot_day: datetime
    washing_machine_id: str

@dataclass
class WashingMachineDto:
    washing_machine_id: str
    washing_machine_status: str

@dataclass
class BookSlotDto:
    username: str
    slot_start_time: datetime.time
    slot_end_time: datetime.time
    slot_date: datetime.date

@dataclass
class UserSlotDto:
    slot_date: datetime
    slot_start_time: datetime.time
    slot_end_time: datetime.time
    washing_machine_id: str
