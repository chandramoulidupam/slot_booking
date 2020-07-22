from slot_booking.constants.exception_messages import USER_CANNOT_BOOK_A_SLOT
from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
import json

from django.http import HttpResponse, response

class SlotBookingPresenterImplementation(PresenterInterface):
    def get_booked_slot_details(self, booked_slot_dto):
        slot_booking_response = {
            "slot_start_time": booked_slot_dto.slot_start_time,
            "slot_end_time": booked_slot_dto.slot_end_time,
            "slot_date": booked_slot_dto.slot_date,
            "washing_machine_id": booked_slot_dto.washing_machine_id,
            "slot_status": booked_slot_dto.slot_status,
        }
        return response.HttpResponse(json.dumps(slot_booking_response), status=200)

    def raise_exception_for_user_cannot_book_a_slot(self):
        response_object = response.HttpResponse(json.dumps(
            {
                "response": USER_CANNOT_BOOK_A_SLOT[0],
                "http_status_code": USER_CANNOT_BOOK_A_SLOT[1],
                "res_status": 404
            }
        ), status=404)
        return response_object

    def list_of_avilable_slots(self, list_of_slot_dtos):
        pass
