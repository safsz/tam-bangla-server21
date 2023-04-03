from pydantic import BaseModel
from typing import Optional

class TCCTeam(BaseModel):
    team_name : str
    base_city: str
    captain: str
    captain_phone_no: str
    manager_name: str
    manager_phone_no: str
    manager_email: str
    comments: str
    registration_time : str


class Users(BaseModel):
    name: str
    email: str
    picture: Optional[str]
    tcc: Optional[TCCTeam] = None