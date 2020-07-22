from datetime import datetime
from abc import abstractmethod
from typing import Optional, List

class StorageInterface:

    @abstractmethod
    def list_of_avilable_slot_dtos(self, date: str) :
        pass

    @abstractmethod
    def validate_washing_machine_number(self, washing_machine_number: str)-> bool:
        pass

    @abstractmethod
    def get_added_washing_machine_dto(self, washing_machine_number):
        pass