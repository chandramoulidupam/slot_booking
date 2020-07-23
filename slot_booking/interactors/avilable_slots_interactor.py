import datetime

from slot_booking.adapters.service_adapter import get_service_adapter
from slot_booking.constants.custom_exceptions import UserIsAdmin, DateInvalid
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.interactors.presenters.presenter_interface \
        import PresenterInterface


class AvilableSlotsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def avilable_slots_wrapper(self, username: str, date: datetime.date, presenter: PresenterInterface):
        try:
            return self.avilable_slots_response(username, date, presenter)
        except UserIsAdmin:
            return presenter.raise_exception_for_user_is_admin()
        except DateInvalid:
            return presenter.raise_exception_for_invalid_date()

    def avilable_slots_response(self, username, date, presenter):
        list_of_slot_dtos = self.avilable_slots(username, date)
        return presenter.list_of_avilable_slots(list_of_slot_dtos)

    def avilable_slots(self, username, date):
        service_adapter = get_service_adapter()
        is_user_admin = service_adapter.is_user_admin_adopter. \
            user_is_admin(username=username)
        if is_user_admin:
            raise UserIsAdmin
        date_is_valid = self.storage.validate_date(date)
        date_is_not_valid = not date_is_valid
        if date_is_not_valid:
            raise DateInvalid
        # date = datetime.datetime.strptime(date, "%d-%m-%Y").date()
        avilable_slots_dtos = self.storage.list_of_avilable_slot_dtos(username, date)
        return avilable_slots_dtos
