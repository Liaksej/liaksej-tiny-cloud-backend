from .settings import *

REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {"anon": "5000/hour", "user": "5000/hour"}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DATABASE_NAME"),
        "HOST": "localhost",
        "PORT": os.environ.get("DATABASE_PORT"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
    }
}
