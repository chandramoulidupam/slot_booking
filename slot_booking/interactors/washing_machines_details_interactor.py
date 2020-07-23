from slot_booking.adapters.service_adapter import get_service_adapter
from slot_booking.constants.custom_exceptions import UserIsAdmin, UserIsNotAdmin
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.interactors.presenters.presenter_interface \
        import PresenterInterface


class WashingMachineDetailsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def washing_machine_details_wrapper(self,username: str, washing_machine_status: str, presenter: PresenterInterface):
        try:
            return self.washing_machine_details_response(username, washing_machine_status, presenter)
        except UserIsNotAdmin:
            return presenter.raise_exception_for_user_is_not_admin()

    def washing_machine_details_response(self,username, washing_machine_status, presenter):
        washing_machine_details_dto = self.washing_machine_details(username, washing_machine_status)
        return presenter.get_washing_machine_details(washing_machine_details_dto)

    def washing_machine_details(self,username, washing_machine_status):
        service_adapter = get_service_adapter()
        is_user_admin = service_adapter.is_user_admin_adopter. \
            user_is_admin(username=username)
        if not is_user_admin:
            raise UserIsNotAdmin
        washing_machine_details_dto = self.storage.washing_machine_details_dto(washing_machine_status)
        return washing_machine_details_dto
