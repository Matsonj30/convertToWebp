from pathlib import Path
from PIL import Image
import os



def convertToWebP(currentImage):

    destination = currentImage.with_suffix(".webp")
    openImage = Image.open(currentImage)

    openImage.save(destination, format="webp")
    os.remove(currentImage)

def main():
    PNGimages = Path("D://ConvertWebp").glob("**/*.PNG")
    JPGimages = Path("D://ConvertWebp").glob("**/*.jpg")


    for image in PNGimages:
          convertToWebP(image)


    for image in JPGimages:
         convertToWebP(image)


main()