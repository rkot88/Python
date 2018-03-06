import os
import requests
import shutil


def get_cat(folder, name):
    url = "http://consuming-python-services-api.azurewebsites.net/cats/random"
    data = get_data_from_url(url)
    save_image(folder, name, data)


def get_data_from_url(url):
    response = requests.get(url, stream=True) # change streaming mode to true to raw work properly
    return response.raw


def save_image(folder, name, data):
    file_name = os.path.join(folder, name + ".jpg")
    with open(file_name, "wb") as fout:  # wb - write binary
        shutil.copyfileobj(data, fout)  # shutil module to copy file object from data stream to fout stream
