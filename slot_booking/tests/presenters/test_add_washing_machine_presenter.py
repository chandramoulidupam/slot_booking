import json

import pytest

from slot_booking.constants.exception_messages import WASHING_MACHINE_NUMBER_INVALID
from slot_booking.presenters.add_washing_machine_presenter_implementation import AddWashingmachinePresenterImplementation
from slot_booking.constants.custom_exceptions import InvalidWashingMachineNumber


def test_add_washing_machine_with_invalid_washing_number_raises_exception():
    presenter = AddWashingmachinePresenterImplementation()

    excepted_response = {
        "response": WASHING_MACHINE_NUMBER_INVALID[0],
        "http_status_code": WASHING_MACHINE_NUMBER_INVALID[1],
        "res_status": 403
    }

    response = presenter.raise_exception_for_invalid_washing_machine_number()
    response = json.loads(response.content)
    assert  response == excepted_response

