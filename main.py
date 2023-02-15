from pathlib import Path
from PIL import Image
import os



def convertToWebP(currentImage):

    destination = currentImage.with_suffix(".webp")
    print(destination)
    openImage = Image.open(currentImage)
    print(currentImage)
    openImage.save(destination, format="webp")
    os.remove(currentImage)

def main():
    PNGimages = Path("D://ConvertWebp").glob("**/*.PNG")
    JPGimages = Path("D://ConvertWebp").glob("**/*.jpg")


    for image in PNGimages:
          print(image)
          convertToWebP(image)
        # try:
      
        # except:
        #     print("Exception occured")

    for image in JPGimages:
         convertToWebP(image)


main()