from dotenv import load_dotenv
import os

load_dotenv()


# Configure Database
# class db_settings:
DB_URI = os.getenv("DB_URI")
DB_NAME = os.getenv("DB_NAME")
