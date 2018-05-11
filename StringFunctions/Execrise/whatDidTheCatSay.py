#Write a python programme that prompts for input and displays a cat "saying"
# what was provided by the user. Place the input provided by the user inside a speech bubble.
#Make the speech bubble expand or contract to fit around the input provided by the user.
command = input ("Type something here and press enter ")
commandlength = len(command)
print (" "*11 + "_"*commandlength)
print (" "*9 + "< "+ command + " >")
print (" "*11 + "-"*commandlength)
print (" "*10 + "/")
print (" /\_/\   / ")
print ("( o.o )")
print (" > ^ < ")


message = input ("Type here and press enter ")
messagelength = len(message)
print ("{}{}" . format (" " * 9, "_" * messagelength))
print ("{}< {} >" . format (" " * 7, message))
print ("{}{}" . format (" " * 9, "-" * messagelength))
print ("{}/ " . format (" " * 8))
print (" /\_/\ / ")
print ("( o.o ) ")
print (" > ^ < ")