# Lab 9 – Image Processing
# Name: Jaylen Atsou
# Date: April 5, 2026
# Assignment: Lab

from PIL import Image


def swapGreenBlue(img):
    """Swap the green and blue values for every pixel in the image."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue, alpha = pixels[x, y]
            pixels[x, y] = (red, blue, green, alpha)

    img.save("swapGB.png")


def darken(img, amount):
    """Darken the image by reducing RGB values by the given amount."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue, alpha = pixels[x, y]

            red = max(0, red - amount)
            green = max(0, green - amount)
            blue = max(0, blue - amount)

            pixels[x, y] = (red, green, blue, alpha)

    img.save("darkImg.png")


def bwFilter(img):
    """Example function: converts image to grayscale."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue, alpha = pixels[x, y]
            avg = (red + green + blue) // 3
            pixels[x, y] = (avg, avg, avg, alpha)

    img.save("bwImg.png")


def main():
    myImg = Image.open("durango.png").convert("RGBA")

    swapGreenBlue(myImg.copy())
    darken(myImg.copy(), 20)


if __name__ == "__main__":
    main()