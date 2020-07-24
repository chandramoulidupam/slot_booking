# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_previous_slots_with_invalid_date_raises_exception response'] = {
    'http_status_code': 'DATE_INVALID',
    'res_status': 404,
    'response': 'date is invalid'
}

snapshots['test_previous_slots_when_user_is_not_admin_raises_exception response'] = {
    'http_status_code': 'USER_IS_ADMIN',
    'res_status': 404,
    'response': 'user is admin'
}

snapshots['test_previous_slots_with_valid_details_returns_list_of_slots response'] = {
    'list_of_previous_slots': [
        {
            'slot_date': '02-11-2020',
            'slot_end_time': '08:25:00',
            'slot_start_time': '07:25:00',
            'washing_machine_id': 'washing_machine_1'
        }
    ],
    'number_of_slots_used_in_previous': 1
}
