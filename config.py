import os
from dotenv import load_dotenv


class Config(object):
    load_dotenv()
    SQLALCHEMY_DATABASE_URI = \
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
