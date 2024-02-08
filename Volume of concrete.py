import depth as depth

building_type = input("Is this for a Residential or Commercial building? ")
depth = 0
if building_type == "Residential":
    depth = 25
elif building_type == "Commercial":
    depth = 50
else:
    building_type = input("Is it a residential or Commercial building? ")

length = int(input("What is the length specification? "))
width = int(input("What is the width specification? "))
volume = length*width*depth