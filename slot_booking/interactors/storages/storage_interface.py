# from datetime import datetime
from abc import abstractmethod
# from typing import Optional, List
# from slot_booking.dtos.dtos import BookSlotDto


class StorageInterface:

    @abstractmethod
    def list_of_avilable_slot_dtos(self, username, date):
        pass

    @abstractmethod
    def validate_washing_machine_id(self, washing_machine_id: str) -> bool:
        pass

    @abstractmethod
    def get_added_washing_machine_dto(self, washing_machine_id):
        pass

    @abstractmethod
    def list_of_upcoming_slot_dtos(self, date, username):
        pass

    @abstractmethod
    def is_user_booking_slot_in_due_date(self, BookSlotDto) -> bool:
        pass

    @abstractmethod
    def booking_a_slot_for_user(self, BookSlotDto):
        pass

    @abstractmethod
    def list_of_previous_slot_dtos(self, username: str, date: str):
        pass

    @abstractmethod
    def validate_date(self, date) -> bool:
        pass

    @abstractmethod
    def washing_machine_details_dto(self, washing_machine_status):
        pass

    @abstractmethod
    def allocated_slot_dtos(self, washing_machine_id, day):
        pass

#++++++++++++++++++++
    @abstractmethod
    def check_slot_exists_or_not(self, slot_id):
        pass

    @abstractmethod
    def add_slot_to_washing_machine(self, each_slot, day):
        pass

    @abstractmethod
    def update_slot_to_washing_machine(self, each_slot, day):
        pass

    @abstractmethod
    def validate_given_list_of_slots_dto(self, slots_dtos):
        pass