from django.db import models
from slot_booking.constants.enums import SlotStatus, BookedStatus


class WashingMachine(models.Model):
    washing_machine_number = models.CharField(max_length=30)


class Slot(models.Model):
    slot_date = models.DateField()
    slot_start_time = models.TimeField()
    slot_end_time = models.TimeField()
    washing_machine_id = models.ForeignKey(WashingMachine, on_delete=models.CASCADE)
    slot_status = models.CharField(max_length=100, choices=SlotStatus.get_list_of_tuples())
    slot_username = models.CharField(max_length=40)


class UserSlot(models.Model):
    user_slot_status = models.CharField(max_length=100, choices=BookedStatus.get_list_of_tuples())
    user_booked_slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    slot_username = models.CharField(max_length=40)
