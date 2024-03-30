x = int(input("Enter a Number: "))

list =[]

for i in range (1, x +1):
    if x%i == 0:
        list.append(i)
print( "The List of factors of", str(x) + " is: ", list) 