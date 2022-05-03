import json
from exceptions import *


def load_json_date(path):
    """
    Функция для преобразования json файла
    При неверном преобразовании вызывает ошибку
    """
    try:
        with open(path, encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def search_posts_by_substring(posts, substring):
    """
    Функция для поиска постов
    """
    posts_founded = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            posts_founded.append(post)
    return posts_founded
