from pydantic import BaseModel

# Валидатор регистрации в аккаунт
class RegisterUserModel(BaseModel):
    name: str
    surname: str
    phone_number: int
    email: str
    city: str
    password: str

# Валидатор входа в аккаунт
class LoginUserModel(BaseModel):
    user_email: str
    password: str



# Валидатор изменения данных пользователя
class EditUserModel(BaseModel):
    user_id: int
    edit_data: str
    new_data: str

