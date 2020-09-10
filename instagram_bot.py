from instabot import Bot
from dotenv import load_dotenv
import os
import time


def user_login(bot):
    load_dotenv()
    username = os.getenv("INSTAGRAM_LOGIN")
    password = os.getenv("INSTAGRAM_PASSWORD")
    bot.login(username=username, password=password)


upload_space_image = lambda bot, path: bot.upload_photo(path)


def main():
    bot = Bot()
    user_login(bot)

    try:
        images = os.listdir("resized_images")
    except FileNotFoundError:
        exit("resized_images directory does not exist")

    for image in images:
        try:
            upload_space_image(bot, "resized_images/" + image)
            time.sleep(15)
        except:
            continue
    

if __name__ == "__main__":
    main()