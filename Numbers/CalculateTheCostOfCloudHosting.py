hour = 0.51

#Because day has 24 hrs
day = hour * 24
#Month has 30 days
month = day * 30

#Both should be strings so str is used
print ("Cost of day is " + str(day))
print ("Cost of month is " + str(month))

#Solution from the textbook
print ("Cost of day is ${:.2f}".format(day))
print ("Cost of month is ${:.2f}".format(month))