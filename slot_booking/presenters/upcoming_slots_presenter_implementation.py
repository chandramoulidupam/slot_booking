from slot_booking.constants.exception_messages import USER_IS_ADMIN
from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
import json

from django.http import response


class UpcomingSlotsPresenterImplementation(PresenterInterface):
    def list_of_upcoming_slots(self, list_of_slot_dtos):
        list_of_upcoming_slots = []
        for each_slot in list_of_slot_dtos:
            each_slot_details = self._get_each_slot_details(each_slot)
            list_of_upcoming_slots.append(each_slot_details)
        count_of_avilable_slots = len(list_of_upcoming_slots)
        previous_slots_response = {
            "list_of_upcoming_slots": list_of_upcoming_slots,
            "number_of_slots_yet_to_be_used": count_of_avilable_slots
        }
        return response.HttpResponse(json.dumps(previous_slots_response), status=200)

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

    def raise_exception_for_invalid_washing_machine_id(self):
        pass

    def raise_exception_for_user_is_admin(self):
        response_object = response.HttpResponse(json.dumps(
            {
                "response": USER_IS_ADMIN[0],
                "http_status_code": USER_IS_ADMIN[1],
                "res_status": 404
            }
        ), status=404)
        return response_object

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
