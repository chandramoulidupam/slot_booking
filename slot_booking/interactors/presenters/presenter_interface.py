from abc import ABC
from abc import abstractmethod


class PresenterInterface(ABC):

    @abstractmethod
    def list_of_avilable_slots(self, list_of_slot_dtos):
        pass

    @abstractmethod
    def get_added_washing_machine_details(self, washing_machine_dto):
        pass

    @abstractmethod
    def raise_exception_for_invalid_washing_machine_number(self):
        pass