red = 51
green = 255
blue = 51
alpha = 128

htmlColor = "#" + "{0:02X}{1:02X}{2:02X}"\
    .format(red, green, blue)
# htmlColor is #33ff33
print("style\"color: " + htmlColor + "\"")

# with transparency
htmlColor += "{0:02X}".format(alpha)
# htmlColor is #33ff3380
print("htmlColor is", htmlColor)