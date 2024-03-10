temp = (float(input("Enter Temperature in celsius: ")))


if temp < -273.15:
    print("Invalid!!! Becasue it is Below Absolute Zero! ")

elif temp == -273.15:
    print("The Temperature is Absolute Zero. ")

elif temp == -273.15 and 0:
    print("The Temperature is Below Freezing. ")

elif temp == 0:
    print("The temperature is at the Freezing Point. ")

elif temp == 0 and 100:
    print("The Temperature is in Normal Range. ")
    
elif temp == 100:
    print("The Temperature is at the boiling point. ")

elif temp > 100:
    print("The Temperature is Above Boiling point. ")

