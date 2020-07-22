

REQUEST_BODY_JSON = """
{
    "username": "string",
    "password": "string"
}
"""


RESPONSE_201_JSON = """
{
    "acces_token": "string",
    "refresh_token": "string",
    "is_admin": true
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_CREDENTAILS"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_USERNAME"
}
"""

