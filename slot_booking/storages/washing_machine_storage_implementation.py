# from datetime import datetime

from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.models.Slot import WashingMachine, Slot
from slot_booking.dtos.dtos import WashingMachineDto


class WashingMachineStorageImplementation(StorageInterface):
    def get_added_washing_machine_dto(self, washing_machine_id):

        washing_machine_obj = WashingMachine.objects.create(washing_machine_id=washing_machine_id)
        return WashingMachineDto(
                washing_machine_id=washing_machine_obj.washing_machine_id,
                washing_machine_status=washing_machine_obj.washing_machine_status)

    def validate_washing_machine_id(self, washing_machine_id: str)-> bool:
        is_washing_machine_id_valid = WashingMachine.objects.filter(washing_machine_id=washing_machine_id).exists()
        if is_washing_machine_id_valid == True or washing_machine_id != "":
            return True
        else:
            return False
    def _get_washing_machine_dto(self, each_washing_machine_obj):
        each_washing_machine_dto = WashingMachineDto(
            washing_machine_id=each_washing_machine_obj.washing_machine_id,
            washing_machine_status=each_washing_machine_obj.washing_machine_status
            )
        return each_washing_machine_dto

    def _get_washing_machine_details_dto(self, washing_machine_objs):
        list_of_washing_machine_dtos = []
        for each_washing_machine_obj in washing_machine_objs:
            each_washing_machine_dto = self._get_washing_machine_dto(each_washing_machine_obj)
            list_of_washing_machine_dtos.append(each_washing_machine_dto)
        return list_of_washing_machine_dtos

    def washing_machine_details_dto(self, washing_machine_status):
        if washing_machine_status == "ACTIVE":
            washing_machine_objs = WashingMachine.objects.filter(washing_machine_status="ACTIVE")
        else:
            washing_machine_objs = WashingMachine.objects.filter(washing_machine_status="INACTIVE")
        washing_machine_dtos = self._get_washing_machine_details_dto(washing_machine_objs)
        return washing_machine_dtos

    def allocated_slot_dtos(self, washing_machine_id, day):
        pass

    def list_of_avilable_slot_dtos(self, username, date):
        pass

    def list_of_upcoming_slot_dtos(self, date, username):
        pass

    def is_user_booking_slot_in_due_date(self, BookSlotDto) -> bool:
        pass

    def booking_a_slot_for_user(self, BookSlotDto):
        pass

    def list_of_previous_slot_dtos(self, username: str, date: str):
        pass

    def validate_date(self, date) -> bool:
        pass

    def validate_day(self, day):
        pass
