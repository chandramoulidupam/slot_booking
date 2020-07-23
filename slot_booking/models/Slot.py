from django.db import models
from slot_booking.constants.enums import WashingMachineStatus, SlotDays, BookedStatus


class WashingMachine(models.Model):
    washing_machine_id = models.CharField(max_length=30)
    washing_machine_status = models.CharField(max_length=100, choices=WashingMachineStatus.get_list_of_tuples(), default="ACTIVE")


class Slot(models.Model):
    slot_day =  models.CharField(max_length=100, choices=SlotDays.get_list_of_tuples())
    slot_start_time = models.TimeField()
    slot_end_time = models.TimeField()
    washing_machine_id = models.ForeignKey(WashingMachine, on_delete=models.CASCADE)


class UserSlot(models.Model):
    user_slot_date = models.DateField()
    user_slot_start_time = models.TimeField()
    user_slot_end_time = models.TimeField()
    user_slot_status = models.CharField(max_length=100, choices=BookedStatus.get_list_of_tuples())
    washing_machine_id = models.ForeignKey(WashingMachine, on_delete=models.CASCADE)
    slot_username = models.CharField(max_length=40)
