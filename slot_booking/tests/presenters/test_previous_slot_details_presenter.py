import datetime
import json
from slot_booking.dtos.dtos import WashingMachineDto
from slot_booking.constants.exception_messages import WASHING_MACHINE_NUMBER_INVALID
from slot_booking.presenters.previous_slots_prensenter_implementation \
        import PreviousSlotsPresenterImplementation


def test_add_washing_machine_with_invalid_washing_number_raises_exception(snapshot):
    presenter = PreviousSlotsPresenterImplementation()
    list_of_slot_dtos = [
        SlotDto(
            slot_start_time=datetime.time(7, 25, 00),
            slot_end_time=datetime.time(8, 25, 00),
            slot_day="SUNDAY",
            washing_machine_id="washing_machine_1",
        )
    ]
    response = presenter.list_of_previous_slots(list_of_slot_dtos)
    response = json.loads(response.content)
    snapshot.assert_match(response, 'response')
    # assert response == excepted_response
# Can't instantiate abstract class PreviousSlotsPresenterImplementation with abstract methods get_allocated_slots_for_washing_machine, raise_exception_for_invalid_day, raise_exception_for_user_is_not_admin

# date = datetime.time(7, 25, 00)
# def test_add_washing_machine_with_valid_washing_id_gives_returns_added_machine_details(snapshot):
#     presenter = AddWashingmachinePresenterImplementation()
#     washing_machine_dto = WashingMachineDto(
#         washing_machine_id=1,
#         washing_machine_status="ACTIVE"
#     )
#     excepted_response = {'washing_machine_id': 1, 'washing_machine_status': 'ACTIVE'}
#
#     response = presenter.get_added_washing_machine_details(washing_machine_dto)
#     response = json.loads(response.content)
#     snapshot.assert_match(response, 'response')
#     # assert response == excepted_response
