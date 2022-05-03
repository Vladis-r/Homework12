import json

from config import UPLOAD_FOLDER, POST_PATH
from exceptions import WrongImgType


def save_picture(picture):
    """
    Функция сохраняет картинку и делает проверку на допустимый формат
    """
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in ["jpeg", "png"]:
        raise WrongImgType("Неверный формат файла. Допустимые форматы: jpeg, png")

    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)
    return picture_path


def add_post(post_list, post):
    """
    Функция добавляет пост в json файл
    """
    post_list.append(post)
    with open(POST_PATH, "w", encoding="utf-8") as file:
        json.dump(post_list, file)