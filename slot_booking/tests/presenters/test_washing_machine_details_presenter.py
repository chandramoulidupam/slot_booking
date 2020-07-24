import datetime
import json
from slot_booking.dtos.dtos import WashingMachineDto
from slot_booking.constants.exception_messages import WASHING_MACHINE_NUMBER_INVALID
from slot_booking.presenters.washing_machine_details_presenter_implementation import \
    WashingMachineDetailsPresenterImplementation


def test_washing_machine_details_with_valid_details_returns_details_of_machine(snapshot):
    presenter = WashingMachineDetailsPresenterImplementation()
    # now.strftime("%H:%M:%S")
    washing_machine_details_dto = [
        WashingMachineDto(
            washing_machine_id="washing_machine_1",
            washing_machine_status="ACTIVE")
    ]
    response = presenter.get_washing_machine_details(washing_machine_details_dto)
    response = json.loads(response.content)
    snapshot.assert_match(response, 'response')

def test_washing_machine_details_when_user_is_not_admin_raises_exception(snapshot):
    presenter = WashingMachineDetailsPresenterImplementation()
    response = presenter.raise_exception_for_user_is_not_admin()
    response = json.loads(response.content)
    snapshot.assert_match(response, 'response')