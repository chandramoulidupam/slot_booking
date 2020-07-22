from slot_booking.constants.custom_exceptions import  InvalidWashingMachineNumber
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.interactors.presenters.presenter_interface \
        import PresenterInterface

class AddWashingMachineInteractor:
        def __init__(self, storage: StorageInterface):
                self.storage = storage

        def add_washing_machine_wrapper(self,washing_machine_number: str, presenter: PresenterInterface):
                try:
                        return self.add_washing_machine_response(washing_machine_number, presenter)
                except InvalidWashingMachineNumber:
                        return presenter.raise_exception_for_invalid_washing_machine_number()


        def add_washing_machine_response(self, washing_machine_number, presenter):
                washing_machine_dto = self.add_washing_machine(washing_machine_number)
                return presenter.get_added_washing_machine_details(washing_machine_dto)

        def add_washing_machine(self, washing_machine_number):
                is_washing_machine_number_valid = self.storage.validate_washing_machine_number(washing_machine_number)
                is_washing_machine_number_is_not_valid = not is_washing_machine_number_valid
                if is_washing_machine_number_is_not_valid:
                        raise InvalidWashingMachineNumber
                washing_machine_dto = self.storage.get_added_washing_machine_dto(washing_machine_number)
                return washing_machine_dto