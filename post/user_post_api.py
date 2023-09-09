from fastapi import APIRouter, UploadFile, Body

from post import PublicPostModel, EditPostModel

# Создать компонент
posts_router = APIRouter(prefix='/user_post', tags=['Работа с публикациями'])

@posts_router.post('/public_post')
async def public_post(data: PublicPostModel):
    pass

@posts_router.put('/change_post')
async def change_post(data: EditPostModel):
    pass

@posts_router.delete('/delete_post')
async def delete_post(post_id: int, user_id: int):
    pass

@posts_router.get('/get_all_posts')
async def get_all_posts():
    pass

@posts_router.post('/add_photo')
async def add_photo(post_id: int = Body(),
                    user_id: int = Body(),
                    photo_file: UploadFile = None):
    pass

@posts_router.delete('/delete_photo')
async def delete_photo(photo_id: int, user_id: int):
    pass



