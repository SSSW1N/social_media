from pydantic import BaseModel
from typing import Optional

class RegisterModel(BaseModel):
    name: str
    first_name: str
    phone_number: int
    e_mail: str
    password: str

class ChangeInfoModel(BaseModel):
    user_id: int
    new_name: Optional[str]
    new_first_name: Optional[str]
    new_phone_number: Optional[int]
    new_email: Optional[str]
    new_password: Optional[str]
