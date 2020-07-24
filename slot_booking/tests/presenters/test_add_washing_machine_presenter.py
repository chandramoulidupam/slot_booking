import json
from slot_booking.dtos.dtos import WashingMachineDto
from slot_booking.constants.exception_messages import WASHING_MACHINE_NUMBER_INVALID
from slot_booking.presenters.add_washing_machine_presenter_implementation \
        import AddWashingmachinePresenterImplementation


def test_add_washing_machine_with_invalid_washing_number_raises_exception(snapshot):
    presenter = AddWashingmachinePresenterImplementation()

    excepted_response = {
        "response": WASHING_MACHINE_NUMBER_INVALID[0],
        "http_status_code": WASHING_MACHINE_NUMBER_INVALID[1],
        "res_status": 403
    }

    response = presenter.raise_exception_for_invalid_washing_machine_id()
    response = json.loads(response.content)
    snapshot.assert_match(response, 'response')
    # assert response == excepted_response


def test_add_washing_machine_with_valid_washing_id_gives_returns_added_machine_details(snapshot):
    presenter = AddWashingmachinePresenterImplementation()
    washing_machine_dto = WashingMachineDto(
        washing_machine_id="washing_machine_1",
        washing_machine_status="ACTIVE"
    )
    excepted_response = {'washing_machine_id': 1, 'washing_machine_status': 'ACTIVE'}

    response = presenter.get_added_washing_machine_details(washing_machine_dto)
    response = json.loads(response.content)
    snapshot.assert_match(response, 'response')
    # assert response == excepted_response
