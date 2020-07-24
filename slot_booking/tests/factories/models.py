from slot_booking.models.Slot import Slot, WashingMachine, UserSlot
import datetime
import factory

class WashingMachineFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = WashingMachine

    washing_machine_id = factory.Sequence(lambda n: "washing_machine_{0}".format(n+1))
    washing_machine_status = factory.Iterator(["ACTIVE", "INACTIVE"])

class SlotFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Slot

    slot_day = factory.Iterator(["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"])
    slot_start_time = factory.LazyFunction(datetime.datetime.now)
    slot_end_time = factory.LazyFunction(datetime.datetime.now)
    washing_machine_id = factory.SubFactory(WashingMachineFactory)

class UserSlotFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = UserSlot

    user_slot_start_time = factory.LazyFunction(datetime.datetime.now)
    user_slot_end_time = factory.LazyFunction(datetime.datetime.now)
    washing_machine_id = factory.SubFactory(WashingMachineFactory)
    user_slot_date = factory.LazyFunction(datetime.datetime.today)
    user_slot_status = factory.Iterator(["BOOKED", "NOTBOOKED"])
    slot_username = factory.Sequence(lambda n: "username_{0}".format(n+1))