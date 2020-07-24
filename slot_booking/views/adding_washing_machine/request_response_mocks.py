

REQUEST_BODY_JSON = """
{
    "washing_machine_number": "string"
}
"""


RESPONSE_201_JSON = """
{
    "slot_id": 1,
    "slot_time": "00:00:00",
    "slot_date": "2099-12-31",
    "washing_machine_id": "string"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_WASHING_MACHINE_ID"
}
"""

