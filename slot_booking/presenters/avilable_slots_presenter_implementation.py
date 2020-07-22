from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
import json

from django.http import HttpResponse, response

class AvilableSlotsPresenterImplementation(PresenterInterface):
    def list_of_avilable_slots(self, list_of_slot_dtos):
        list_of_avilable_slots = []
        for each_slot in list_of_slot_dtos:
            each_slot_details = self._get_each_slot_details(each_slot)
            list_of_avilable_slots.append(each_slot_details)
        count_of_avilable_slots = len(list_of_avilable_slots)
        avilable_slots_response = {
            "list_of_avilable_slots" : list_of_avilable_slots,
            "number_of_slots_avilable": count_of_avilable_slots
        }
        return response.HttpResponse(json.dumps(avilable_slots_response), status= 201)

    def _get_each_slot_details(self, slot_dto):
        each_slot_details = {
                "slot_id": slot_dto.id,
                "slot_start_time": slot_dto.slot_start_time,
                "slot_end_time": slot_dto.slot_end_time,
                "slot_date": slot_dto.slot_date,
                "washing_machine_id": slot_dto.washing_machine_id_id,
                "slot_status": slot_dto.slot_status
            }
        return each_slot_details
