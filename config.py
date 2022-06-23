class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///movies.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_JSON_AS_ASCII = False
    JSON_SORT_KEYS = False
