from slot_booking.constants.exception_messages import USER_IS_NOT_ADMIN, WASHING_MACHINE_NUMBER_INVALID
from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
import json

from django.http import response


class GetAllocatedSlotsPresenterImplementation(PresenterInterface):
    def get_allocated_slots_for_washing_machine(self, list_of_slot_dtos):
        list_of_allocated_slot_details = []
        for each_slot in list_of_slot_dtos:
            each_slot_details = self._get_each_slot_details(each_slot)
            list_of_allocated_slot_details.append(each_slot_details)
        count_of_avilable_slots = len(list_of_allocated_slot_details)
        list_of_allocated_slot_reponse = {
            "list_of_allocated_slot_details": list_of_allocated_slot_details,
            "number_of_slots_allocated_to_washing_machine": count_of_avilable_slots
        }
        return response.HttpResponse(json.dumps(list_of_allocated_slot_reponse), status=200)

    def list_of_previous_slots(self, list_of_slot_dtos):
        pass

    def _get_each_slot_details(self, slot_dto):
        each_slot_details = {
                "slot_start_time": (slot_dto.slot_start_time).strftime("%H:%M:%S"),
                "slot_end_time": (slot_dto.slot_end_time).strftime("%H:%M:%S"),
                "slot_date": (slot_dto.slot_date).strftime("%d-%m-%Y"),
                "washing_machine_id": slot_dto.washing_machine_id
            }
        return each_slot_details

    def list_of_avilable_slots(self, list_of_slot_dtos):
        pass

    def get_added_washing_machine_details(self, washing_machine_dto):
        pass

    def list_of_upcoming_slots(self, list_of_slot_dtos):
        pass

    def raise_exception_for_user_is_admin(self):
        pass

    def raise_exception_for_user_cannot_book_a_slot(self):
        pass

    def get_booked_slot_details(self, booked_slot_dto):
        pass

    def raise_exception_for_invalid_date(self):
        pass

    def raise_exception_for_no_slots_avilable_to_user(self):
        pass

    def get_washing_machine_details(self, washing_machine_details_dto):
        pass

    def raise_exception_for_invalid_day(self):
        pass

    def raise_exception_for_user_is_not_admin(self):
        response_object = response.HttpResponse(json.dumps(
            {
                "response": USER_IS_NOT_ADMIN[0],
                "http_status_code": USER_IS_NOT_ADMIN[1],
                "res_status": 404
            }
        ), status=404)
        return response_object

    def raise_exception_for_invalid_washing_machine_id(self):
        response_object = response.HttpResponse(json.dumps(
            {
                "response": WASHING_MACHINE_NUMBER_INVALID[0],
                "http_status_code": WASHING_MACHINE_NUMBER_INVALID[1],
                "res_status": 403
            }
        ), status=403)
        return response_object

    def alter_slots_for_washing_machine_returns_slots_details(self, list_of_slot_dtos):
        pass

    def raise_exception_for_invalid_inputs(self):
        pass