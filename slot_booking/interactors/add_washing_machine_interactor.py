from slot_booking.adapters.service_adapter import get_service_adapter
from slot_booking.constants.custom_exceptions import InvalidWashingMachineNumber, UserIsNotAdmin
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.interactors.presenters.presenter_interface \
        import PresenterInterface


class AddWashingMachineInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_washing_machine_wrapper(self,username: str, washing_machine_id: str, presenter: PresenterInterface):
        try:
            return self.add_washing_machine_response(username, washing_machine_id, presenter)
        except UserIsNotAdmin:
            return presenter.raise_exception_for_user_is_not_admin()
        except InvalidWashingMachineNumber:
            return presenter.raise_exception_for_invalid_washing_machine_id()

    def add_washing_machine_response(self,username, washing_machine_id, presenter):
        washing_machine_dto = self.add_washing_machine(username, washing_machine_id)
        return presenter.get_added_washing_machine_details(washing_machine_dto)

    def add_washing_machine(self,username, washing_machine_id):
        service_adapter = get_service_adapter()
        is_user_admin = service_adapter.is_user_admin_adopter. \
            user_is_admin(username=username)
        if not is_user_admin:
            raise UserIsNotAdmin
        is_washing_machine_id_valid = self.storage.validate_washing_machine_id(washing_machine_id)
        is_washing_machine_id_is_not_valid = not is_washing_machine_id_valid
        if is_washing_machine_id_is_not_valid:
            raise InvalidWashingMachineNumber
        washing_machine_dto = self.storage.get_added_washing_machine_dto(washing_machine_id)
        return washing_machine_dto
