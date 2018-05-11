animal = 'dog'
vegetable = 'cabbage'
mineral = 'calcium'
print ('"Here is an animal, vegetable and a mineral"')
print ("Animal : {}" . format (animal))
print ("Vegetable : {}" . format (vegetable))
print ("Mineral : {}" . format (mineral))
print ("{} : {}" . format ("Animal" , animal))
print ("{} : {}" . format ("Vegetable" , vegetable))
print ("{} : {}" . format ("Mineral" , mineral))
print ("{:9} : {}" . format ("Animal" , animal))
print ("{:9} : {}" . format ("Vegetable" , vegetable))
print ("{:9} : {}" . format ("Mineral" , mineral))
print ("{:<15} : {:<15}" . format ("Animal" , animal))
print ("{:^15} : {:^15}" . format ("Vegetable" , vegetable))
print ("{:>15} : {:>15}" . format ("Mineral" , mineral))

age = 32
print ("My age : {}" . format (age))
print ("My age : {:.2f}" . format (age))
print ("My age : {:10.4f}" . format (age))

print ("{:5}" .format ("dog"))