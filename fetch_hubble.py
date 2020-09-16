import requests
import os
import urllib3
import argparse
from image_downloader import download_image


def get_hubble_images_urls(image_id=0, collection=False, page="all") -> list:
    ''' returns a list of urls of Hubble images'''
    payload = {
        "page": page
    }

    hubble_api_url_image = 'http://hubblesite.org/api/v3/image/'
    hubble_images_urls = []

    if not collection:
        response = requests.get(hubble_api_url_image + str(image_id))
        response.raise_for_status()

        hubble_files = response.json()
        if len(hubble_files) > 0:
            hubble_images_urls = [
                image_file['file_url']
                for image_file in hubble_files['image_files']
            ]

        return hubble_images_urls

    elif collection:
        hubble_api_url_images = f'http://hubblesite.org/api/v3/images/{collection}'

        response = requests.get(hubble_api_url_images, params=payload)
        response.raise_for_status()

        hubble_files_collection = response.json()
        image_ids = [hubble_file['id']
                     for hubble_file in hubble_files_collection]
        for image_id in image_ids:
            response = requests.get(hubble_api_url_image + str(image_id))
            response.raise_for_status()

            hubble_files = response.json()
            if len(hubble_files) > 0:
                image_urls_list = [
                    image_file['file_url']
                    for image_file in hubble_files['image_files']
                ]
                for image_url in image_urls_list:
                    hubble_images_urls.append(image_url)

        return hubble_images_urls


def download_hubble_images(image_id=0, collection=False, page="all"):
    ''' Downloads Hubble images '''
    hubble_images_urls = get_hubble_images_urls(image_id, collection, page)

    for hubble_image_url in hubble_images_urls:
        image_id = hubble_image_url.split('/')[-2]
        if not collection:
            download_image('http:' + hubble_image_url, f'hubble{os.sep}{image_id}',
                           verify=False)
        elif collection:
            download_image('http:' + hubble_image_url,
                           f'hubble{os.sep}{collection}{os.sep}{image_id}',
                           verify=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", help="download all hubble images by id")
    parser.add_argument(
        "--collection", help="collection of hubble images to download")
    parser.add_argument(
        "--page", help="page of collection of hubble images to download")
    args = parser.parse_args()

    if args.id is None and args.collection is None and args.page is None:
        exit("You haven't choosen any arguments")
    if args.id is None:
        args.id = 0
    if args.collection is None:
        args.collection = 'nothing'
    if args.page is None:
        args.page = "all"

    if args.collection is not None:
        download_hubble_images(collection=args.collection, page=args.page)

    download_hubble_images(args.id)


if __name__ == '__main__':
    main()
