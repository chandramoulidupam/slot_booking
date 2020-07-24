

REQUEST_BODY_JSON = """
{
    "slot_from_time": "string",
    "slot_to_time": "string",
    "slot_day": "SUNDAY"
}
"""


RESPONSE_201_JSON = """
{
    "total_slots_avilable": 1,
    "list_of_slots": [
        {
            "slot_id": "string",
            "slot_start_time": "string",
            "slot_end_time": "string",
            "slot_day": "string",
            "washing_machine_id": "string"
        }
    ]
}
"""

