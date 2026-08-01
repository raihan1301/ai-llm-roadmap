#import PIL
from PIL import Image
from PIL import ImageFilter

def main():
    
    #img = Image.open("in.jpg")
    #img.close()

    with Image.open("in.jpg") as img:
        print(img.size)
        print(img.format)
        
        # this will rotate image and create new image file
        #new_image = img.rotate(180)
        #new_image.save("out.jpg")

        #add filter
        new_image = img.filter(ImageFilter.BLUR)
        new_image.save("out.jpg")


main()