# from datetime import date, time
from slot_booking.dtos.dtos import BookSlotDto
from slot_booking.constants.custom_exceptions import  UserCanNotBookASlot
from slot_booking.interactors.storages.storage_interface import StorageInterface
from slot_booking.interactors.presenters.presenter_interface \
        import PresenterInterface

class BookingSlotInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def book_slot_wrapper(self, BookSlotDto:BookSlotDto, presenter: PresenterInterface):
        try:
            return self.book_slot_response(BookSlotDto, presenter)
        except UserCanNotBookASlot:
            return presenter.raise_exception_for_user_cannot_book_a_slot()

    def book_slot_response(self, BookSlotDto, presenter):
        booked_slot_dto = self.book_slot(BookSlotDto)
        return presenter.get_booked_slot_details(booked_slot_dto)

    def book_slot(self,BookSlotDto):
        is_user_booking_slot_in_due_date = self.storage.is_user_booking_slot_in_due_date(BookSlotDto)
        # Assume True if he has booked a slot
        if is_user_booking_slot_in_due_date:
            raise UserCanNotBookASlot
        booked_slot_dto = self.storage.booking_a_slot_for_user(BookSlotDto)
        return booked_slot_dto
