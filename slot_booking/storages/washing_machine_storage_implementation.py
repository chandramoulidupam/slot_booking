from datetime import datetime

from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.models.Slot import Slot, WashingMachine
from slot_booking.dtos.dtos import SlotDto, WashingMachineDto

class WashingMachineStorageImplementation(StorageInterface):
    def get_added_washing_machine_dto(self, washing_machine_number):

        washing_machine_obj = WashingMachine.objects.create(washing_machine_number=washing_machine_number)
        return WashingMachineDto(washing_machine_number=washing_machine_obj.washing_machine_number)

    def validate_washing_machine_number(self, washing_machine_number: str)-> bool:
        is_washing_machine_number_valid = WashingMachine.objects.filter(washing_machine_number=washing_machine_number).exists()
        if is_washing_machine_number_valid == True or washing_machine_number != "":
            return True
        else:
            return False

