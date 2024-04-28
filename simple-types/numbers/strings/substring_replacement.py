startString = "3, 2, 1, go!"
startString = startString\
    .replace("1", "one")\
    .replace("2", "two")\
    .replace("3", "three")
# startString is "three, two, one, go!"

print(startString)