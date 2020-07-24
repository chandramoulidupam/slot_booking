import datetime
import json
from slot_booking.dtos.dtos import UserSlotDto
from slot_booking.constants.exception_messages import WASHING_MACHINE_NUMBER_INVALID
from slot_booking.presenters.previous_slots_prensenter_implementation \
        import PreviousSlotsPresenterImplementation


def test_previous_slots_with_valid_details_returns_list_of_slots(snapshot):
    presenter = PreviousSlotsPresenterImplementation()
    # now.strftime("%H:%M:%S")
    list_of_slot_dtos = [
        UserSlotDto(
            slot_start_time=datetime.time(7, 25, 00),
            slot_end_time=datetime.time(8, 25, 00),
            slot_date=datetime.date(2020, 11, 2),
            washing_machine_id="washing_machine_1",
        )
    ]
    response = presenter.list_of_previous_slots(list_of_slot_dtos)
    response = json.loads(response.content)
    snapshot.assert_match(response, 'response')

# date = datetime.time(7, 25, 00)
def test_previous_slots_with_invalid_date_raises_exception(snapshot):
    presenter = PreviousSlotsPresenterImplementation()
    # excepted_response = {'washing_machine_id': 1, 'washing_machine_status': 'ACTIVE'}

    response = presenter.raise_exception_for_invalid_date()
    response = json.loads(response.content)
    snapshot.assert_match(response, 'response')
    # assert response == excepted_response

def test_previous_slots_when_user_is_not_admin_raises_exception(snapshot):
    presenter = PreviousSlotsPresenterImplementation()
    # excepted_response = {'washing_machine_id': 1, 'washing_machine_status': 'ACTIVE'}

    response = presenter.raise_exception_for_user_is_admin()
    response = json.loads(response.content)
    snapshot.assert_match(response, 'response')