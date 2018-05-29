hour = 0.51

#Because day has 24 hrs
day = hour * 24
#Month has 30 days
month = day * 30
servers = 20
budget = 918

#Both should be strings so str is used
print ("Cost of day is $" + str(day))
print ("Cost of month is $" + str(month))
print ("Cost of {} servers per day is ${:.2f}".format(servers,day*servers))
print ("Cost of {} servers per month is ${:.2f}".format(servers,month*servers))
print ("1 server with ${} can run for {:.2f} days".format(budget,budget/day))