from fastapi import APIRouter
from user import RegisterUserModel, EditUserModel, LoginUserModel

# Создать компонент
user_router = APIRouter(prefix='/user', tags=['Управление пользователями'])


# Запрос на вход в аккаунт
@user_router.post('/login')
async def login_user(data: LoginUserModel):
    pass

@user_router.post('/register')
async def register_user(data: RegisterUserModel):
    pass

@user_router.put('/change_info')
async def change_user_info(data: EditUserModel):
    pass

@user_router.get('/get_user')
async def get_user(user_id: int):
    pass



