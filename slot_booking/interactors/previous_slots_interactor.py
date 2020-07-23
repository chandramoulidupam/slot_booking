
from slot_booking.adapters.service_adapter import get_service_adapter
from slot_booking.constants.custom_exceptions import UserIsAdmin, DateInvalid
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.interactors.presenters.presenter_interface \
        import PresenterInterface


class PreviousSlotsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def previous_slots_wrapper(self, username: str, date: str, presenter: PresenterInterface):
        try:
            return self.previous_slots_response(date, username, presenter)
        except UserIsAdmin:
            return presenter.raise_exception_for_user_is_admin()
        except DateInvalid:
            return presenter.raise_exception_for_invalid_date()

    def previous_slots_response(self, date, username, presenter):
        list_of_slot_dtos = self.previous_slots(date, username)
        return presenter.list_of_previous_slots(list_of_slot_dtos)

    def previous_slots(self, date, username):
        service_adapter = get_service_adapter()
        is_user_admin = service_adapter.is_user_admin_adopter. \
            user_is_admin(username=username)
        if is_user_admin:
            raise UserIsAdmin
        date_is_valid = self.storage.validate_date(date)
        date_is_not_valid = not date_is_valid
        if date_is_not_valid:
            raise DateInvalid
        # date = date.strftime("%m-%d-%Y")
        previous_slots_dtos = self.storage.list_of_previous_slot_dtos(date, username)
        return previous_slots_dtos
