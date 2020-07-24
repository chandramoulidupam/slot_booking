# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_alllocated_slots_with_valid_details_returns_list_of_slots response'] = {
    'list_of_allocated_slot_details': [
        {
            'slot_date': '02-11-2020',
            'slot_end_time': '08:25:00',
            'slot_start_time': '07:25:00',
            'washing_machine_id': 'washing_machine_1'
        }
    ],
    'number_of_slots_allocated_to_washing_machine': 1
}

snapshots['test_get_allocated_slots_when_user_is_not_admin_raises_exception response'] = {
    'http_status_code': 'USER_IS_NOT_ADMIN',
    'res_status': 404,
    'response': 'user is not admin'
}

snapshots['test_get_allocated_slots_with_invalid_washing_number_raises_exception response'] = {
    'http_status_code': 'WASHING_MACHINE_NUMBER_INVALID',
    'res_status': 403,
    'response': 'washing machine_number already exists'
}
