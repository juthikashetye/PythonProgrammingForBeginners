age = 33
#print ("I'm " + age + " years old")
#The above line is wrong, it produces error.
#TypeError: must be str, not int
print ("I'm " + str(age) + " years old")
#Above line is not ideal as it uses too much "+" sign
#print ("{} {} {}" . format ("I'm" , "age" , "years old"))
#Above line is wrong as it produces output : I'm age years old
print ("{} {} {}" . format ("I'm" , age , "years old"))
#Above line is not ideal as there is unnecessary use of "{}"
print ("I'm {} years old" . format (age))
print ("I'm {} years old and my husband is also {} years old" . format (age, age + 1))
print ("I'm {0} years old and my husband is also {0} years old" . format (age))