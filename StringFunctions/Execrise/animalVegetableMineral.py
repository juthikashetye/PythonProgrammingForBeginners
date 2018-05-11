#Write a python programme that uses three variables. The variables in your programme will be animal, vegetable & mineral.
#Assign a string value to each one of the variables.
#Your programme should display "Here is an animal, vegetable and a mineral"
#Next display the value for animal, vegetable and mineral.
#Each one of their values should be printed on their own line.
#Your programme will display four lines in total.
animal = 'dog'
vegetable = 'cabbage'
mineral = 'calcium'
print ('"Here is an animal, vegetable and a mineral"')
print (animal)
print (vegetable)
print (mineral)
print ('"Here is an animal, vegetable and a mineral on the same line"')
print (animal + ' ' + vegetable + ' ' + mineral)
print ('"Here are the first alphabets of an animal, vegetable and a mineral on the same line"')
print (animal[0] + ' ' + vegetable[0] + ' ' + mineral[0])
print ('"Here are the lengths of an animal, vegetable and a mineral on the same line"')
print (str(len(animal)) + ' ' + str(len(vegetable)) + ' ' + str(len(mineral)))
print ('"Here are the last alphabets of an animal, vegetable and a mineral on the same line"')
print (animal[len(animal)-1] + ' ' + vegetable[len(vegetable)-1] +' ' + mineral[len(mineral)-1])
print ('"Here are the last alphabets in capital of an animal, vegetable and a mineral on the same line"')
print (animal[len(animal)-1].upper() + ' ' + vegetable[len(vegetable)-1].upper() +' ' + mineral[len(mineral)-1].upper())
