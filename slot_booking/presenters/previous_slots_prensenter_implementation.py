from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
import json

from django.http import HttpResponse, response

class PreviousSlotsPresenterImplementation(PresenterInterface):
    def list_of_previous_slots(self, list_of_slot_dtos):
        list_of_previous_slots = []
        for each_slot in list_of_slot_dtos:
            each_slot_details = self._get_each_slot_details(each_slot)
            list_of_previous_slots.append(each_slot_details)
        count_of_avilable_slots = len(list_of_previous_slots)
        previous_slots_response = {
            "list_of_previous_slots" : list_of_previous_slots,
            "number_of_slots_used_in_previous": count_of_avilable_slots
        }
        return response.HttpResponse(json.dumps(previous_slots_response), status= 200)

    def _get_each_slot_details(self, slot_dto):
        each_slot_details = {
                "slot_start_time": slot_dto.slot_start_time,
                "slot_end_time": slot_dto.slot_end_time,
                "slot_date": slot_dto.slot_date,
                "washing_machine_id": slot_dto.washing_machine_id_id,
                "slot_status": slot_dto.slot_status
            }
        return each_slot_details
