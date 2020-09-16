from instabot import Bot
from dotenv import load_dotenv
import os
import time


def main():
    bot = Bot()

    load_dotenv()
    username = os.getenv("INSTAGRAM_LOGIN")
    password = os.getenv("INSTAGRAM_PASSWORD")

    bot.login(username=username, password=password)

    try:
        images = os.listdir("resized_images")
    except FileNotFoundError:
        exit("resized_images directory does not exist")

    for image in images:
        bot.upload_photo(f"resized_images{os.sep}" + image)
        time.sleep(60)


if __name__ == "__main__":
    main()
