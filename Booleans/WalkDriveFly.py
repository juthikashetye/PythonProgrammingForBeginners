#<3 miles walk
#>3, <300 miles drive
#>=300 miles fly

userinput = input ("How many miles do you want to travel? ")
miles = int(userinput)
mode = ""
if miles <=3:
	mode = "walk"

elif miles <300:
	mode = "drive"

else:
	mode = "fly"

print ("I suggest you to {}" . format (mode))

