from datetime import datetime

from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.models.Slot import Slot
from slot_booking.dtos.dtos import SlotDto

class SlotStorageImplementation(StorageInterface):
    def list_of_avilable_slot_dtos(self, date: datetime):
        from userapp.models.models import User
        slot_objs = User.objects.filter(date=date)
        list_of_slot_dtos = self._get_list_of_slot_dto(slot_objs)
        return  list_of_slot_dtos

    def _get_list_of_slot_dto(self, slot_objs):
        list_of_slot_dtos = []
        for each_slot_obj in slot_objs:
            each_slot_dto = self.get_each_slot_dto(each_slot_obj)
            list_of_slot_dtos.append(each_slot_dto)
        return  list_of_slot_dtos

    def get_each_slot_dto(self, each_slot_obj):
        each_slot_dto = SlotDto(
            slot_id = each_slot_obj.id,
            slot_start_time=each_slot_obj.slot_start_time,
            slot_end_time=each_slot_obj.slot_end_time,
            slot_date=each_slot_obj.slot_end_time,
            washing_machine_id=each_slot_obj.washing_machine_id,
            slot_status= each_slot_obj.slot_status
        )
        return each_slot_dto