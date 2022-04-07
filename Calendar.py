# prompt the user to enter the data 
m, d, y = map(int, input("ENTER THE DATE as MM DD YYYY: ").split())
# Create a list of weekdays in upper case
weekdays = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
# Every number in months dictionary refer to it's month for example 1->January , 2->February, etc..
# and every number in the dictionary have a number that refer to the doomsdays position in the month
# doomsdays are the same for all the days in the dictionary  
months = {
    "1": 3,
    "2": 28,
    "3": 7,
    "4": 4,
    "5": 9,
    "6": 6,
    "7": 11,
    "8": 8,
    "9": 5,
    "10": 10,
    "11": 7,
    "12" :12,
}
# cntury will be used to find the anchor day
# Calendars repeat themselves every 400 years
century = int(str(y)[:2]) + 1
if century % 4 == 0:
    anchor = weekdays[3] # anchor day is Wednesday
elif century % 4 == 1:
    anchor = weekdays[2] # anchor day is Tuesday
elif century % 4 == 2:
    anchor = weekdays[0] # anchor day is Sunday
elif century % 4 == 3:
    anchor = weekdays[5] # anchor day is Friday 
# Geting the first two digits in date, for example if y = 1976, num will be 76
num = y % 100
# Calculating the doomsday algorithm
doomsday = ((num % 12) + (num // 12) + ((num % 12) // 4 ) % 7 + weekdays.index(anchor)) % 7
# Check if it is a leap year
# doomsdays for January and February will be changed if it's a leap year 
if (y % 4 == 0) or ( (y % 100 == 0) and (y % 400 == 0) ):
    months["1"] = 4
    months["2"] = 29
# month refer to the doomsday of the month
month = months[str(m)]
# Calculating the index of the day
# index here refer to the index of weekdays 
if month > d:
    ans_idx = (doomsday - (month - d)) % 7 
elif month < d:
    ans_idx = (doomsday + (d - month)) % 7
else:
    ans_idx = doomsday

print(weekdays[ans_idx])