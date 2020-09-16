from PIL import Image, PngImagePlugin
import os


def save_resized_image(image):
    ''' Resizes image and saves '''
    PngImagePlugin.MAX_TEXT_CHUNK = 100 * (1024**2)
    Image.MAX_IMAGE_PIXELS = None
    pil_image = Image.open(image)

    pil_image = pil_image.convert('RGB')
    pil_image.thumbnail((1080, 1080))

    # Несмотря на то, что thumbnail должен давать картинку
    # с 1080 по большей стороне, попадаються "аномалии" вида 1000x600,
    # которые нужно отсеять
    if pil_image.width == 1080 or pil_image.height == 1080:
        resized_image = f'resized_images{os.sep}' + \
            image.split(os.sep)[-1].replace(".png", ".jpg")
        pil_image.save(resized_image, format="JPEG")


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
    pathes = [f'images{os.sep}hubble{os.sep}',
              f'images{os.sep}hubble{os.sep}spacecraft{os.sep}',
              f'images{os.sep}hubble{os.sep}news{os.sep}',
              f'images{os.sep}spacex{os.sep}']

    for path in pathes:
        save_resized_images_in_directory(path)


if __name__ == "__main__":
    main()
