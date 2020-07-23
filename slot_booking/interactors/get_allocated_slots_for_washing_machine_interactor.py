
from slot_booking.adapters.service_adapter import get_service_adapter
from slot_booking.constants.custom_exceptions import InvalidWashingMachineId, DayIsInvalid
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.interactors.presenters.presenter_interface \
        import PresenterInterface


class AllocatedSlotsForWashingMachineInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_allocated_slots_wrapper(self, washing_machine_id: str, day: str, presenter: PresenterInterface):
        try:
            return self.get_allocated_slots_response(washing_machine_id, day, presenter)
        except InvalidWashingMachineId:
            return presenter.raise_exception_for_invalid_washing_machine_id()

    def get_allocated_slots_response(self, washing_machine_id, day, presenter):
        list_of_slot_dtos = self.get_allocated_slots(washing_machine_id, day)
        return presenter.get_allocated_slots_for_washing_machine(list_of_slot_dtos)

    def get_allocated_slots(self, washing_machine_id, day):
        machine_id_is_valid = self.storage.validate_washing_machine_id(washing_machine_id)
        machine_id_is_invalid = not machine_id_is_valid
        if machine_id_is_invalid:
            raise InvalidWashingMachineId
        allocated_slots_dtos = self.storage.allocated_slot_dtos( washing_machine_id, day)
        return allocated_slots_dtos
