# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_washing_machine_details_with_valid_details_returns_details_of_machine response'] = {
    'list_of_washing_machine_details': [
        {
            'washing_machine_id': 'washing_machine_1',
            'washing_machine_status': 'ACTIVE'
        }
    ]
}

snapshots['test_washing_machine_details_when_user_is_not_admin_raises_exception response'] = {
    'http_status_code': 'USER_IS_NOT_ADMIN',
    'res_status': 404,
    'response': 'user is not admin'
}
