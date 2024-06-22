list = []

n = int(input("Enter a Size of List: "))



for i in range (0, n ):
    size = int (input())
    list.append(size)



summ = sum(list)
rev = list[::-1]
num_int = sum(1 for num in list if num < 5)

if 5 in list :
    print("HELLL YEAHHH!!!")

else:
    print("NO!")

remove = list[1:-1]
remove.sort()




print("Original list: ", list)
print ("The sum of your list: ", summ)
print("The last item of your list: ", str(list[len(list) - 1]))
print("The reverse Order of your List: ", rev)
print("Number of Integer in list: ", num_int)
print("Remaining Items of the list: ", remove)
print("Sorted Remaining Item of the List: ", remove)