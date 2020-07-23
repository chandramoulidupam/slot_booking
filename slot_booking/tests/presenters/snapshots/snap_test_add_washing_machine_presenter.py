# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_add_washing_machine_with_invalid_washing_number_raises_exception response'] = {
    'http_status_code': 'WASHING_MACHINE_NUMBER_INVALID',
    'res_status': 403,
    'response': 'washing machine_number already exists'
}

snapshots['test_add_washing_machine_with_valid_washing_id_gives_returns_added_machine_details response'] = {
    'washing_machine_id': 1,
    'washing_machine_status': 'ACTIVE'
}
