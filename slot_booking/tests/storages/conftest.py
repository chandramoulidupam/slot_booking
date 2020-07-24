from datetime import time, date

import pytest
from slot_booking.models.Slot import WashingMachine, UserSlot, Slot


@pytest.fixture()
def washing_machines():
    list_of_washing_machine = [
        WashingMachine(washing_machine_id="washing_machine_1"),
        WashingMachine(washing_machine_id="washing_machine_3"),
        WashingMachine(washing_machine_id="washing_machine_2")
    ]
    WashingMachine.objects.bulk_create(list_of_washing_machine)
    washing_machines = WashingMachine.objects.all()
    return washing_machines


@pytest.fixture()
def slots(washing_machines):
    lists_of_slots = [
        Slot(
            slot_day="SUNDAY",
            slot_start_time=time(6, 00, 00),
            slot_end_time=time(8, 00, 00),
            washing_machine_id_id="washing_machine_1"
            ),
        Slot(
            slot_day="SUNDAY",
            slot_start_time=time(8, 00, 00),
            slot_end_time=time(10, 00, 00),
            washing_machine_id_id="washing_machine_2"
            ),
        Slot(
            slot_day="SUNDAY",
            slot_start_time=time(10, 00, 00),
            slot_end_time=time(12, 00, 00),
            washing_machine_id_id="washing_machine_1"
            ),
        ]
    Slot.objects.bulk_create(lists_of_slots)
    slots = Slot.objects.all()
    return slots


@pytest.fixture()
def user_slots():
    list_of_user_slots = [
        UserSlot(
                user_slot_date=date(25, 7, 2020),
                user_slot_start_time=time(6, 00, 00),
                user_slot_end_time=time(8, 00, 00),
                washing_machine_id_id=1,
                user_slot_status="BOOKED",
                slot_username="mouli"
            ),
        UserSlot(
                user_slot_date=date(10, 8, 2020),
                user_slot_start_time=time(6, 00, 00),
                user_slot_end_time=time(8, 00, 00),
                washing_machine_id_id=2,
                user_slot_status="BOOKED",
                slot_username="mouli"
            ),
        UserSlot(
                user_slot_date=date(17, 8, 2020),
                user_slot_start_time=time(6, 00, 00),
                user_slot_end_time=time(8, 00, 00),
                washing_machine_id_id=1,
                user_slot_status="BOOKED",
                slot_username="mouli"
            )
        ]
    UserSlot.objects.bulk_create(list_of_user_slots)
    user_slots = UserSlot.objects.all()
    return user_slots
