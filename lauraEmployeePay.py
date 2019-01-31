#Using a text editor, write a program that calculates the salary for the week of the employees listed below. 
#If an employee worked more than 40 hours that week, then calculate the remaining hours as time and a half 
#(1.5x the normal rate).The program should print their name and salary earned.
#Upload your finished script to Github and use its URL for your assignment submission.

#
import sys
employeeName = sys.argv[1]
HourlyPayRate = sys.argv[2]
numHours = sys.argv[3]
if (int(numHours) <= 40):
	weeklySal = numHours * int(HourlyPayRate)
else:
	weeklySal = 40 * int(HourlyPayRate) + ((int(numHours) - 40) * 1.5*(int(HourlyPayRate)))

import locale
#locale.setlocale( locale.LC_ALL, '' )
#'English_United States.1252'
#weeklySal = locale.currency(weeklySal, grouping=True)
#locale.currency(weeklySal, grouping=True)
print ("Pay for " + employeeName + " is $", weeklySal.lstrip) 
#print ("Pay for " + employeeName + " is $", locale.currency(weeklySal, grouping=True)) 