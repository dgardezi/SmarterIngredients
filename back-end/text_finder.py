import io
import os

from google.oauth2 import service_account



# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def get_text_from_img(img):
    # Instantiates a client
    credentials = service_account.Credentials. from_service_account_file(r"Allergy App-ed240eab809c.json")
    client = vision.ImageAnnotatorClient(credentials=credentials)

    # The name of the image file to annotate
    # file_name = os.path.abspath(r'C:\Users\Duncan\Desktop\python-getting-started\test2.jpg')

    # Loads the image into memory

    image = types.Image(content=img)

    # Performs label detection on the image file
    response = client.text_detection(image=image)
    texts = response.text_annotations


    return(texts[0].description)
