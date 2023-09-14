from database import get_db
from database.models import Comment


# Опубликовать комментарий
def add_comment_db(post_id, comment_text, user_id):
    db = next(get_db())

    new_comment = Comment(post_id=post_id, comment_text=comment_text, user_id=user_id)
    db.add(new_comment)
    db.commit()

    return "Комментарий оставлен"


# Удалить комментарий
def delete_comment_db(comment_id):
    db = next(get_db())

    exact_comment = db.query(Comment).filter_by(id=comment_id).first()

    if exact_comment:
        db.delete(exact_comment)
        db.commit()

        return 'Успешно удалено'

    return False

# Изменить определенный комментарий
def change_comment_db(comment_id, new_text):
    db = next(get_db())

    exact_comment = db.query(Comment).filter_by(id=comment_id).first()

    if exact_comment:
        exact_comment.comment_text = new_text
        db.commit()

        return 'Комментарий изменен'

    return False

# Получить все комменты определенного поста
def get_post_comment(post_id):
    db = next(get_db())

    exact_post_comment = db.query(Comment).filter_by(post_id=post_id).all()

    return exact_post_comment
