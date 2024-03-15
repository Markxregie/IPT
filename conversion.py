temp = (float(input("Enter Temperature: ")))
unit = (str(input("Enter Units F or C: ")))

if unit == "F":
    temp = (temp - 32) * (5 / 9)
    print(temp, " C")

elif unit == "C":
    temp = (temp * (9 / 5)) + 32
    print(temp, " F")