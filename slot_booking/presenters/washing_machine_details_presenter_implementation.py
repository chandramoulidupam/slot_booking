from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
import json

from django.http import response


class WashingMachineDetailsPresenterImplementation(PresenterInterface):
    def get_washing_machine_details(self, washing_machine_details_dto):
        list_of_washing_machine_details = []
        for each_washing_machine_detail in washing_machine_details_dto:
            each_washing_machine_details = self._get_each_washing_machine_details(each_washing_machine_detail)
            list_of_washing_machine_details.append(each_washing_machine_details)
        count_of_avilable_slots = len(list_of_washing_machine_details)
        washing_machine_details_response = {
            "list_of_previous_slots": list_of_washing_machine_details,
            "number_of_slots_used_in_previous": count_of_avilable_slots
        }
        return response.HttpResponse(json.dumps(washing_machine_details_response), status=200)

    def _get_each_washing_machine_details(self, each_washing_machine_detail):
        each_washing_machine_details = {
                "washing_machine_id": each_washing_machine_detail.washing_machine_id,
                "slot_end_time": each_washing_machine_detail.washing_machine_status,
            }
        return each_washing_machine_details

    def list_of_avilable_slots(self, list_of_slot_dtos):
        pass

    def get_added_washing_machine_details(self, washing_machine_dto):
        pass

    def raise_exception_for_invalid_washing_machine_id(self):
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
