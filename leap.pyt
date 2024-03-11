year = int(input("Enter a Year: "))


if year  % 400 == 0 or year % 4 == 0:
    print(year, " is a Leap Year ")

else:
    print (year, "Is Not a Leap Year ")