from image_downloader import download_image
import requests
import os
import argparse


def get_spacex_launch_images_urls(max_counts: int, last_image_index=0) -> list:
    ''' Returns a list of urls of SpaceX flights images '''
    spacex_api_url = 'https://api.spacexdata.com/v4/launches'

    response = requests.get(spacex_api_url)
    response.raise_for_status()

    spacex_flights = response.json()
    spacex_images_urls = []

    count = 0
    for spacex_flight in spacex_flights:
        flight_images_urls = spacex_flight['links']['flickr']['original']
        for spacex_image_url in flight_images_urls:
            if count == int(max_counts) + last_image_index:
                break
            spacex_images_urls.append(spacex_image_url)
            count += 1

    return spacex_images_urls[last_image_index:]


def download_spacex_launch_images(max_counts):
    ''' Downloads images of SpaceX spaceships '''
    image_counter = 0

    spacex_images_urls = get_spacex_launch_images_urls(max_counts)
    if os.path.exists('images/spacex'):
        if len(os.listdir('images/spacex')) == 0:
            pass
        else:
            last_image_index = max([int(image_title.strip('spacex_img').
                                    split('.')[0]) for image_title
                                    in os.listdir('images/spacex')])
            image_counter = last_image_index
            spacex_images_urls = get_spacex_launch_images_urls(
                max_counts, last_image_index)

    for spacex_image_url in spacex_images_urls:
        image_counter += 1
        download_image(spacex_image_url, f'spacex/spacex_img{image_counter}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", help="count of spacex images to download",
    required=True)
    args = parser.parse_args()

    download_spacex_launch_images(args.count)


if __name__ == '__main__':
    main()
