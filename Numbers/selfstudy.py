age = input ("What is your age?")

#difference = 2018 - age
#TypeError: unsupported operand type(s) for -: 'int' and 'str'

#difference = "2018" - age
#TypeError: unsupported operand type(s) for -: 'str' and 'str'

if age.isdigit() :
	difference = 2018 - int(age)

	print ("You are " + str (age) + " years old")
	print ("You were born in " + str (difference))

else : 
	print ("You are an idiot. Write your age in whole numbers")

"""https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float"""