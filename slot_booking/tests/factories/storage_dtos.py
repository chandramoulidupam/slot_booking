from datetime import datetime
import factory
from slot_booking.dtos.dtos import SlotDto, UserSlotDto, WashingMachineDto, UpdateSlotInputDto

class SlotDtoFactory(factory.Factory):

    class Meta:
        model = SlotDto

    slot_day = factory.Iterator(["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"])
    slot_start_time = factory.LazyFunction(datetime.now)
    slot_end_time = factory.LazyFunction(datetime.now)
    washing_machine_id = factory.Sequence(lambda n: 'washing_machine_%d' %n)


class WashingMachineDtofactory(factory.Factory):

    class Meta:
        model = WashingMachineDto

    washing_machine_id = factory.Sequence(lambda n: 'washing_machine_%d' % n)
    washing_machine_status = factory.Iterator(["ACTIVE", "INACTIVE"])


class UserSlotDtoFactory(factory.Factory):

    class Meta:
        model = UserSlotDto

    user_slot_date = factory.LazyFunction(datetime.today)
    slot_start_time = factory.LazyFunction(datetime.now)
    slot_end_time = factory.LazyFunction(datetime.now)
    washing_machine_id = factory.Sequence(lambda n: 'washing_machine_%d' %n)

class UpdatedSlotInputDtoFactory(factory.Factory):

    class Meta:
        model = UpdateSlotInputDto

    slot_day = factory.Iterator(["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"])
    slot_start_time = factory.LazyFunction(datetime.now)
    slot_end_time = factory.LazyFunction(datetime.now)
    washing_machine_id = factory.Sequence(lambda n: 'washing_machine_%d' %n)