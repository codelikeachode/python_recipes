latitude = 91

if latitude == 0:
    location = "Equator"
elif latitude == 90:
    location = "North Pole"
elif latitude == -90:
    location = "South Pole"
else:
    location = "Somewhere else"

print(f"{location = }")