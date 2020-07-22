from datetime import datetime, time

import pytest
from freezegun import freeze_time
from slot_booking.models.Slot import WashingMachine, UserSlot, Slot


@pytest.fixture()
def washing_machines():
    list_of_washing_machine = [
        WashingMachine(washing_machine_number="washing_machine_1"),
        WashingMachine(washing_machine_number="washing_machine_2")
        ]
    WashingMachine.objects.bulk_create(list_of_washing_machine)
    washing_machines = WashingMachine.objects.all()
    return washing_machines

@pytest.fixture()
def slots():
    lists_of_slots = [
        Slot(slot_date = datetime.now(), slot_start_time = time(22, 00, 00),slot_end_time =time(23, 00, 00), washing_machine_id_id = 1, slot_status = "Avilable"),
        # Slot(),
        # Slot()
    ]
    Slot.objects.bulk_create(lists_of_slots)
    slots = Slot.objects.all()
    return slots


@pytest.fixture()
def user_slots():
    list_of_user_slots = [
        UserSlot(user_slot_status="Avilable", ),
        UserSlot(),
        UserSlot()
    ]
    UserSlot.objects.bulk_create(list_of_user_slots)
    user_slots = UserSlot.objects.all()
    return user_slots
