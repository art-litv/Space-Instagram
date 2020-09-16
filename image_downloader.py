import requests
import os
import urllib3
from pathlib import PurePath


def download_image(url: str, path: str, verify=True):
    ''' Downloads an image into "images" directory '''
    ''' Required for fetch_spacex.py and fetch_hubble.py '''
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    response = requests.get(url, verify=verify)
    response.raise_for_status()

    filename = path.split(os.sep)[-1]
    directories = path[0:path.find(filename)]

    try:
        os.makedirs(f"images{os.sep}{directories}", exist_ok=False)
    except FileExistsError:
        pass

    path = path + '.' + url.split(".")[-1]

    with open(f"images{os.sep}{path}", 'wb') as file:
        file.write(response.content)
