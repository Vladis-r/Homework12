from flask import Blueprint, render_template, request
import logging

from main import utils
from loader.utils import *

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")
logging.basicConfig(filename="logger.log", level=logging.INFO)

@loader_blueprint.route("/post")
def create_new_post_page():
    """
    Страница для отправки поста
    """
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def create_new_post_by_user():
    """
    Форма для создания поста.
    Проверки:
        - для создания поста хватает данных
        - подходящий формат изображения
    """
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        logging.info("Данные не загружены, отсутствует часть данных")
        return "Отсутствует часть данных"

    posts = utils.load_json_date(POST_PATH)

    try:
        new_post = {"pic": save_picture(picture), "content": content}
    except WrongImgType:
        return "Неверный формат файла"

    add_post(posts, new_post)
    return render_template("post_uploaded.html", new_post=new_post)
