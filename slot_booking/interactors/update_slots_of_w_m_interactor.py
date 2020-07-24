from typing import List
from slot_booking.dtos.dtos import SlotDto
from slot_booking.adapters.service_adapter import get_service_adapter
from slot_booking.constants.custom_exceptions import InvalidWashingMachineId, DayIsInvalid, UserIsNotAdmin, \
    InvalidInputsGiven
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.interactors.presenters.presenter_interface \
        import PresenterInterface


class UpdateSlotsForWashingMachineInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def update_slots_wrapper(self,username: str, washing_machine_id: str, day: str,slots_dtos: List[SlotDto], presenter: PresenterInterface):
        try:
            return self.update_slots_response(username, slots_dtos, washing_machine_id, day, presenter)
        except UserIsNotAdmin:
            return presenter.raise_exception_for_user_is_not_admin()
        except InvalidWashingMachineId:
            return presenter.raise_exception_for_invalid_washing_machine_id()
        except InvalidInputsGiven:
            return presenter.raise_exception_for_invalid_inputs()

    def update_slots_response(self,username,slots_dtos, washing_machine_id, day, presenter):
        list_of_slot_dtos = self.update_slots(username, slots_dtos, washing_machine_id, day)
        return presenter.alter_slots_for_washing_machine_returns_slots_details(list_of_slot_dtos)

    def update_slots(self,username, slots_dtos, washing_machine_id, day):
        service_adapter = get_service_adapter()
        is_user_admin = service_adapter.is_user_admin_adopter. \
            user_is_admin(username=username)
        if not is_user_admin:
            raise UserIsNotAdmin
        machine_id_is_valid = self.storage.validate_washing_machine_id(washing_machine_id)
        machine_id_is_invalid = not machine_id_is_valid
        if machine_id_is_invalid:
            raise InvalidWashingMachineId
        validate_given_slots = self.storage.validate_given_list_of_slots_dto(slots_dtos)
        if not validate_given_slots:
            raise InvalidInputsGiven
        list_of_added_or_updated_slot_dtos = []
        for each_slot in slots_dtos:
            is_slot_exists = self.storage.check_slot_exists_or_not(each_slot.slot_id)
            slot_not_exists = not is_slot_exists
            if slot_not_exists:
                alter_slot_dto = self.storage.add_slot_to_washing_machine(each_slot, day)
            else:
                alter_slot_dto = self.storage.update_slot_to_washing_machine(each_slot, day)
            list_of_added_or_updated_slot_dtos.append(alter_slot_dto)
        return list_of_added_or_updated_slot_dtos
