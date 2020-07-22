from dataclasses import dataclass
# from typing import List, Optional
from datetime import datetime
from slot_booking.constants.enums import SlotStatus


@dataclass
class SlotDto:
    slot_id: int
    slot_start_time: datetime
    slot_end_time: datetime
    slot_date: datetime
    washing_machine_id: int
    slot_status: SlotStatus

@dataclass
class WashingMachineDto:
    washing_machine_number: str

