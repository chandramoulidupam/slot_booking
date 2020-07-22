from dataclasses import dataclass
# from typing import List, Optional
# from datetime import datetime



@dataclass
class AccessTokenDto:
    access_token:str
    is_admin: bool

@dataclass
class UserDto:
    user_id: int
    name: str
    is_admin: bool