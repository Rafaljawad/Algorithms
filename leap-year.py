#Python program to check leap year
print("Insert the year and check if it is a leap year or not")
year = int(input("Enter year  "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not leap year")