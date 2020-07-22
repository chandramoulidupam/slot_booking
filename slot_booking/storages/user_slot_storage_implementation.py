from datetime import datetime

from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.models.Slot import Slot
from slot_booking.dtos.dtos import SlotDto

class UserSlotStorageImplementation(StorageInterface):
    def list_of_upcoming_slot_dtos(self, date, username):
        pass