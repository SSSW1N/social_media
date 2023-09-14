from pydantic import BaseModel


# Валидатор публикации комментариев
class CommentModel(BaseModel):
    comment_text: str
    user_id: int
    post_id: int


# Валидатор на изменения коммента
class EditCommentModel(BaseModel):
    new_text: str
    comment_id: int




