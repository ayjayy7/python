from datetime import *

today = date.today()
#date1=date(today.year,today.month,today.day)
#date2=date(year,month,day)

def check_birthdate(year , month , day):
	
	if (year < today.year): 
				return calculate_age
	else:
		return check_birthdate

def calculate_age(year , month , day):
	year=today.year-int(year)
	month=today.month-int(month)
	day=today.day-int(day)
	print("You are" , year , "years, " , month , "months, and " , day , "days")


year=input('Enter year of birth: ')
month=input('Enter month of birth: ')
day=input('Enter day of birth: ')

if (today.year - year >=0):
	calculate_age(year,month,day)
else:
	print("False")

#check_birthdate(year , month , day)
#calculate_age(year,month,day)

#print("You are" , year , "years, " , month , "months, and " , day , "days")

