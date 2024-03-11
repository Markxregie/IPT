weight = float(input("Enter your Weight in Kilos: "))

while weight <= 0:
    print("invalid input")
    weight = float(input("Enter your Weight in Kilos: "))
    
x = weight * 2.2
print(x, " Is Your Weight in Pounds: ")