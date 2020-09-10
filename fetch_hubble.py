import requests
import os
import urllib3
import argparse
from image_downloader import download_image


def get_hubble_images_urls(id=0, collection=False, page="all") -> list:
  ''' returns a list of urls of Hubble images'''
  payload = {
    "page": page
  }

  hubble_api_url_image = 'http://hubblesite.org/api/v3/image/'
  hubble_images_urls = []

  if collection == False:
    response = requests.get(hubble_api_url_image + str(id))
    response.raise_for_status()

    hubble_files = response.json()
    if len(hubble_files) > 0:
      hubble_images_urls = [image_file['file_url'] for image_file in hubble_files['image_files']]

    return hubble_images_urls
  else:
    hubble_api_url_images = f'http://hubblesite.org/api/v3/images/{collection}'

    response = requests.get(hubble_api_url_images, params=payload)
    response.raise_for_status()

    hubble_files_collection = response.json()
    ids = [hubble_file['id'] for hubble_file in hubble_files_collection]
    for id in ids:
      response = requests.get(hubble_api_url_image + str(id))
      response.raise_for_status()

      hubble_files = response.json()
      if len(hubble_files) > 0:
        image_urls_list = [image_file['file_url'] for image_file in hubble_files['image_files']]
        for image_url in image_urls_list:
          hubble_images_urls.append(image_url)

    return hubble_images_urls


def download_hubble_images(id=0, collection=False, page="all"):
  ''' Downloads Hubble images '''
  hubble_images_urls = get_hubble_images_urls(id, collection, page)

  status_counter = 0
  for hubble_image_url in hubble_images_urls:
    image_id = hubble_image_url.split('/')[-2]
    if collection == False:
      download_image('http:'+ hubble_image_url, f'hubble/{image_id}',
      verify=False)
      status_counter += 1
      if status_counter == 1:
        print(f"Downloaded {status_counter} Hubble image")
      elif status_counter > 1:
        print(f"Downloaded {status_counter} Hubble images")
    else:
      download_image('http:'+ hubble_image_url, f'hubble/{collection}/{image_id}',
      verify=False)
      status_counter += 1
      if status_counter == 1:
        print(f"Downloaded {status_counter} Hubble {collection} image")
      elif status_counter > 1:
        print(f"Downloaded {status_counter} Hubble {collection} images")


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--id", help="count of hubble images by id to download")
  parser.add_argument("--collection", help="collection of hubble images to download")
  parser.add_argument("--page", help="collection of hubble images to download")
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

  print("\nDone")


if __name__ == '__main__':
  main()
