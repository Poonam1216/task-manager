import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Application configuration.

    Using SQLite for simplicity and portability.
    Easy to replace with Postgres/MySQL later.
    """

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + os.path.join(BASE_DIR, "..", "tasks.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
