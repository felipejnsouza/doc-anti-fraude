import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOIT = os.getenv('ENDPOINT')
    KEY = os.getenv('KEY')
    AZURE_STORAGE_CONNECTION_STRING = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    CONTAINER_NAME = os.getenv('CONTAINER_NAME')
