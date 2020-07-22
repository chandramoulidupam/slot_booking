from datetime import datetime
from abc import abstractmethod
from typing import Optional, List
from slot_booking.dtos.dtos import BookSlotDto

class StorageInterface:

    @abstractmethod
    def list_of_avilable_slot_dtos(self,username, date) :
        pass

    @abstractmethod
    def validate_washing_machine_number(self, washing_machine_number: str)-> bool:
        pass

    @abstractmethod
    def get_added_washing_machine_dto(self, washing_machine_number):
        pass

    @abstractmethod
    def list_of_upcoming_slot_dtos(self, date, username):
        pass

    @abstractmethod
    def is_user_booking_slot_in_due_date(self, BookSlotDto)-> bool:
        pass

    @abstractmethod
    def booking_a_slot_for_user(self, BookSlotDto):
        pass

    @abstractmethod
    def list_of_previous_slot_dtos(self, username: str, date: str):
        pass

    @abstractmethod
    def validate_date(self, date)-> bool:
        pass

