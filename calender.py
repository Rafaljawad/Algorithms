#Write a Python program to display calender ?
import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))
print(calendar.month(year, month))