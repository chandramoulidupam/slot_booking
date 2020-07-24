from slot_booking.constants.exception_messages import WASHING_MACHINE_NUMBER_INVALID
from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
import json

from django.http import response


class AddWashingmachinePresenterImplementation(PresenterInterface):
    def get_added_washing_machine_details(self, washing_machine_dto):
        added_washing_machine_response = {
            "washing_machine_id": washing_machine_dto.washing_machine_id,
            "washing_machine_status": washing_machine_dto.washing_machine_status
        }
        return response.HttpResponse(json.dumps(added_washing_machine_response), status=200)

    def raise_exception_for_invalid_washing_machine_id(self):
        response_object = response.HttpResponse(json.dumps(
            {
                "response": WASHING_MACHINE_NUMBER_INVALID[0],
                "http_status_code": WASHING_MACHINE_NUMBER_INVALID[1],
                "res_status": 403
            }
        ), status=403)
        return response_object

    def list_of_avilable_slots(self, list_of_slot_dtos):
        pass

    def list_of_upcoming_slots(self, list_of_slot_dtos):
        pass

    def raise_exception_for_user_is_admin(self):
        pass

    def raise_exception_for_user_cannot_book_a_slot(self):
        pass

    def get_booked_slot_details(self, booked_slot_dto):
        pass

    def list_of_previous_slots(self, list_of_slot_dtos):
        pass

    def raise_exception_for_invalid_date(self):
        pass

    def raise_exception_for_no_slots_avilable_to_user(self):
        pass

    def get_washing_machine_details(self, washing_machine_details_dto):
        pass

    def raise_exception_for_invalid_day(self):
        pass

    def get_allocated_slots_for_washing_machine(self, list_of_slot_dtos):
        pass

    def raise_exception_for_user_is_not_admin(self):
        pass

    def alter_slots_for_washing_machine_returns_slots_details(self, list_of_slot_dtos):
        pass

    def raise_exception_for_invalid_inputs(self):
        pass