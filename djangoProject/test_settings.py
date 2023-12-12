from .settings import *

REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {"anon": "5000/hour", "user": "5000/hour"}
