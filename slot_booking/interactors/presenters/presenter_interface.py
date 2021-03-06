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
    def raise_exception_for_invalid_washing_machine_id(self):
        pass

    @abstractmethod
    def list_of_upcoming_slots(self, list_of_slot_dtos):
        pass

    @abstractmethod
    def raise_exception_for_user_is_admin(self):
        pass

    @abstractmethod
    def raise_exception_for_user_cannot_book_a_slot(self):
        pass

    @abstractmethod
    def get_booked_slot_details(self, booked_slot_dto):
        pass

    @abstractmethod
    def list_of_previous_slots(self, list_of_slot_dtos):
        pass

    @abstractmethod
    def raise_exception_for_invalid_date(self):
        pass

    @abstractmethod
    def raise_exception_for_no_slots_avilable_to_user(self):
        pass

    @abstractmethod
    def get_washing_machine_details(self, washing_machine_details_dto):
        pass

    @abstractmethod
    def raise_exception_for_invalid_day(self):
        pass

    @abstractmethod
    def get_allocated_slots_for_washing_machine(self, list_of_slot_dtos):
        pass

    @abstractmethod
    def raise_exception_for_user_is_not_admin(self):
        pass

    @abstractmethod
    def alter_slots_for_washing_machine_returns_slots_details(self, list_of_slot_dtos):
        pass

    @abstractmethod
    def raise_exception_for_invalid_inputs(self):
        pass