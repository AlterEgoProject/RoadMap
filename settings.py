import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

UNITY_PORT = os.environ.get('UNITY_PORT')
OBS_PORT = os.environ.get('OBS_PORT')
OBS_PASSWORD = os.environ.get('OBS_PASSWORD')
SERIAL_PORT = os.environ.get('SERIAL_PORT')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
SEIKA_PORT = os.environ.get('SEIKA_PORT')
YOUTUBE_API_ID = os.environ.get('YOUTUBE_API_ID')
YOUTUBE_API_SECRET = os.environ.get('YOUTUBE_API_SECRET')
