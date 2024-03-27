from color import Color

orange = Color("orange")

red = orange.red * 255
green = orange.green * 255
blue = orange.blue * 255

htmlColor = "#" + "{0:02X}{1:02X}{2:02X}"\
    .format(int(red), int(green), int(blue))
# htmlColor is #00AFCA
print("style=\"color: " + htmlColor + "\"")

# with transparency
htmlColor += "{0:02X}".format(128)
# htmlColor is #00AFCA80
print("htmlColor is", htmlColor)