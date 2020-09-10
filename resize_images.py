from PIL import Image, PngImagePlugin
import os


def save_resized_image(image):
    ''' Resizes image and saves '''
    PngImagePlugin.MAX_TEXT_CHUNK = 100 * (1024**2)
    Image.MAX_IMAGE_PIXELS = None
    pil_image = Image.open(image)

    pil_image.thumbnail((1080, 1080))

    if pil_image.width == 1080:
        resized_image = 'resized_images/' + image.split('/')[-1].replace(".png", ".jpg")
        # Некоторые .png картинки имеют формат RGBA 
        # и при форматировании в .jpg бросают исключение
        try:
            pil_image.save(resized_image, format="JPEG")
        except OSError:
            pass
        except MemoryError:
            pass


def save_resized_images_in_directory(path):
    images = []
    try:
        images = os.listdir(path)
    except FileNotFoundError:
        pass

    try:
        os.makedirs("resized_images", exist_ok=False)
    except FileExistsError:
        pass

    for image in images:
        if ".jpg" in image or ".png" in image:
            save_resized_image(path + image)
        

def main():
    pathes = ['images/hubble/',
              'images/hubble/spacecraft/',
              'images/hubble/news/',
              'images/spacex/']

    for path in pathes:
        save_resized_images_in_directory(path)


if __name__ == "__main__":
    main()