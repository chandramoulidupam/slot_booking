from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
import json

from django.http import response


class AvilableSlotsPresenterImplementation(PresenterInterface):
    def list_of_avilable_slots(self, list_of_slot_dtos):
        list_of_avilable_slots = []
        for each_slot in list_of_slot_dtos:
            each_slot_details = self._get_each_slot_details(each_slot)
            list_of_avilable_slots.append(each_slot_details)
        count_of_avilable_slots = len(list_of_avilable_slots)
        avilable_slots_response = {
            "list_of_avilable_slots": list_of_avilable_slots,
            "number_of_slots_avilable": count_of_avilable_slots
        }
        return response.HttpResponse(json.dumps(avilable_slots_response), status=200)

    def _get_each_slot_details(self, slot_dto):
        each_slot_details = {
                "slot_start_time": slot_dto.slot_start_time,
                "slot_end_time": slot_dto.slot_end_time,
                "slot_date": slot_dto.slot_date,
                "washing_machine_id": slot_dto.washing_machine_id_id,
                "slot_status": slot_dto.slot_status
            }
        return each_slot_details

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

    def alter_slots_for_washing_machine_returns_slots_details(self, list_of_slot_dtos):
        pass

    def raise_exception_for_invalid_inputs(self):
        pass