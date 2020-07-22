import pytest
from freezegun import freeze_time
from slot_booking.models.Slot import WashingMachine


@pytest.fixture()
def washing_machines():
    list_of_washing_machine = [
        WashingMachine(washing_machine_number="washing_machine_1"),
        WashingMachine(washing_machine_number="washing_machine_2")
        ]
    WashingMachine.objects.bulk_create(list_of_washing_machine)
    washing_machines = WashingMachine.objects.all()
    return washing_machines
