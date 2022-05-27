class RGB:

    red = 0
    green = 0
    blue = 0


red = RGB()
red.red = 255
green = RGB()
green.green = 255
blue = RGB()
blue.blue = 255

def rgb2tuple(rgb):
    if isinstance(rgb, RGB):
        return rgb.red, rgb.green, rgb.blue

print(rgb2tuple(42))
print(rgb2tuple(red))
print(rgb2tuple(green))
print(rgb2tuple(blue))