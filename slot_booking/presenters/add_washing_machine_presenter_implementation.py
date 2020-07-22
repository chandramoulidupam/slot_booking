from slot_booking.constants.exception_messages import WASHING_MACHINE_NUMBER_INVALID
from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
import json

from django.http import HttpResponse, response

class AddWashingmachinePresenterImplementation(PresenterInterface):
    def get_added_washing_machine_details(self, washing_machine_dto):
        added_washing_machine_response = {
            "washing_machine_number" : washing_machine_dto.washing_machine_number
        }
        return response.HttpResponse(json.dumps(added_washing_machine_response), status=200)

    def raise_exception_for_invalid_washing_machine_number(self):
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
