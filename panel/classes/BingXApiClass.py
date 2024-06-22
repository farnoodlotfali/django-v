from bingx.api import BingxAPI
from dotenv import load_dotenv
import os


load_dotenv()
# ****************************************************************************************************************************

# bingx = BingxAPI(API_KEY, SECRET_KEY, timestamp="local")

class BingXApiClass:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = BingxAPI(os.getenv("API_KEY"), os.getenv("SECRET_KEY"), timestamp="local")
        return cls._instance
