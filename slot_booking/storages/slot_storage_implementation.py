from datetime import datetime

from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.models.Slot import Slot, WashingMachine
from slot_booking.dtos.dtos import SlotDto, UserSlotDto


class SlotStorageImplementation(StorageInterface):
    def list_of_avilable_slot_dtos(self, username: str, date: datetime.date):
        slot_objs = Slot.objects.filter(slot_date=date).filter(slot_status="Avilable")
        list_of_slot_dtos = self._get_list_of_slot_dto(slot_objs)
        return list_of_slot_dtos

    def _get_list_of_slot_dto(self, slot_objs):
        list_of_slot_dtos = []
        for each_slot_obj in slot_objs:
            each_slot_dto = self.get_each_slot_dto(each_slot_obj)
            list_of_slot_dtos.append(each_slot_dto)
        return list_of_slot_dtos

    def get_each_slot_dto(self, each_slot_obj):
        each_slot_dto = SlotDto(
            slot_start_time=(each_slot_obj.slot_start_time),
            slot_end_time=(each_slot_obj.slot_end_time),
            slot_day=each_slot_obj.slot_day,
            washing_machine_id=each_slot_obj.washing_machine_id_id,
        )
        return each_slot_dto

    def get_each_user_slot_dto(self, each_slot_obj):
        # print("\n"*5, each_slot_obj.user_slot_start_time)
        each_user_slot_dto = UserSlotDto(
            user_slot_start_time=each_slot_obj.user_slot_start_time,
            user_slot_end_time=each_slot_obj.user_slot_end_time,
            user_slot_date=each_slot_obj.user_slot_date,
            washing_machine_id=each_slot_obj.washing_machine_id_id
        )
        return each_user_slot_dto

    def _get_list_of_user_slot_dto(self, user_slot_objs):
        list_of_slot_dtos = []
        for each_slot_obj in user_slot_objs:
            each_slot_dto = self.get_each_user_slot_dto(each_slot_obj)
            list_of_slot_dtos.append(each_slot_dto)
        return list_of_slot_dtos

    def list_of_previous_slot_dtos(self, username: str, date: datetime.date):
        from slot_booking.models.Slot import UserSlot
        user_slot_objs = UserSlot.objects.filter(user_slot_date__lte=date).filter(user_slot_status="BOOKED")
        list_of_slot_dtos = self._get_list_of_user_slot_dto(user_slot_objs)
        return list_of_slot_dtos

    def validate_date(self, date) -> bool:
        from slot_booking.models.Slot import UserSlot
        date_valid = UserSlot.objects.filter(user_slot_date__gte=date).exists()
        if date_valid:
            return True
        else:
            return False

    def list_of_upcoming_slot_dtos(self, date: datetime.date, username: str):
        from slot_booking.models.Slot import UserSlot
        user_slot_objs = UserSlot.objects.filter(user_slot_date__gte=date).filter(user_slot_status="BOOKED")
        list_of_slot_dtos = self._get_list_of_user_slot_dto(user_slot_objs)
        return list_of_slot_dtos

    def allocated_slot_dtos(self, washing_machine_id, day):
        # print("*8888888888888888*", washing_machine_id)
        allocated_slot_objs= Slot.objects.filter(slot_day=day).filter(washing_machine_id_id=washing_machine_id)
        allocate_slot_dtos = []
        for each_slot_obj in allocated_slot_objs:
            each_slot_dto = self.get_each_slot_dto(each_slot_obj)
            allocate_slot_dtos.append(each_slot_dto)
        # print("*************************", allocate_slot_dtos)
        return allocate_slot_dtos

    def is_user_booking_slot_in_due_date(self, BookSlotDto):
        pass

    def booking_a_slot_for_user(self, BookSlotDto):
        pass

    def validate_washing_machine_id(self, washing_machine_id: str) -> bool:
        is_washing_machine_id_valid = WashingMachine.objects.filter(washing_machine_id=washing_machine_id).exists()
        if is_washing_machine_id_valid == True and washing_machine_id != "":
            return True
        else:
            return False

    def get_added_washing_machine_dto(self, washing_machine_id):
        pass

    def washing_machine_details_dto(self, washing_machine_status):
        pass

    def validate_day(self, day):
        pass

    def check_slot_exists_or_not(self, slot_id):
        slot_exists = Slot.objects.filter(slot_id=slot_id).exists()
        if slot_exists:
            return True
        else:
            return False

    def add_slot_to_washing_machine(self, each_slot, day):
        added_slot_obj = Slot.objects.create(
                slot_start_time=each_slot.slot_start_time,
                slot_end_time=each_slot.slot_end_time,
                slot_day=each_slot.slot_day,
                washing_machine_id=each_slot.washing_machine_id
        )
        added_slot_dto = self.get_each_slot_dto(added_slot_obj)
        return added_slot_dto

    def update_slot_to_washing_machine(self, each_slot, day):
        updated_slot_obj = Slot.objects.filter(id=each_slot.slot_id).update(slot_start_time=each_slot.slot_start_time,
                slot_end_time=each_slot.slot_end_time)
        updated_slot_dto = self.get_each_slot_dto(updated_slot_obj)
        return updated_slot_dto

    def validate_given_list_of_slots_dto(self, slots_dtos):
        if slots_dtos == []:
            return False
        else:
            return True