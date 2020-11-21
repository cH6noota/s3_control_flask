import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
accesskey = os.environ.get("ACCESS_KEY") 
secretkey = os.environ.get("SECRET_KEY")
bucket_name = os.environ.get("BUKET_NAME")
