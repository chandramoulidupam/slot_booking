from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.interactors.presenters.presenter_interface \
        import PresenterInterface


class AvilableSlotsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def avilable_slots_wrapper(self, date: str, presenter: PresenterInterface):
        return self.avilable_slots_response(date, presenter)

    def avilable_slots_response(self, date, presenter):
        list_of_slot_dtos = self.avilable_slots(date)
        return  presenter.list_of_avilable_slots(list_of_slot_dtos)

    def avilable_slots(self, date):
        avilable_slots_dtos = self.storage.list_of_avilable_slot_dtos(date)
        return  avilable_slots_dtos