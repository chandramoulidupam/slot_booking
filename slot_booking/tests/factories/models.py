from slot_booking.models.Slot import Slot, WashingMachine
from datetime import datetime
import factory

class WashingMachineFactory(factory.Factory):

    class Meta:
        model = WashingMachine

    washing_machine_id = factory.Sequence(lambda n: 'washing_machine_%d' %n)
    washing_machine_status = factory.fuzzy.FuzzyChoice(WashingMachineStatus.PRODUCT_TYPES)
    washing_machine_status = models.CharField(max_length=100, choices=WashingMachineStatus.get_list_of_tuples(),
                                              default="ACTIVE")
    user_id = factory.Sequence(lambda n: '%d' %n)
    name = factory.Sequence(lambda n: 'user%d' %n)