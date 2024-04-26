# create an empty set and assign it  to a variable
my_set = set()

# Add six items to your empty set using either several add calls, or a single first set
my_set.update([11, 12, 13, 14 ,15 , 16])
print("-----------------------------------------------")
print("First set: ", my_set)
print("-----------------------------------------------")
print()
#create a second set which include at least two common element with first set.
set_2 = {11, 12, 33, 44, 55, 66}
print("-----------------------------------------------")
print("Second set: ", set_2)
print("-----------------------------------------------")
print()

#find the union, difference,  symmetric difference, and intersection of 2 sets.
print("-----------------------------------------------")
print("Union: ", (my_set | set_2))
print("Difference: ", (my_set - set_2))
print("Symmetric Difference : ", (my_set ^ set_2))
print("Intersection: ", (my_set & set_2))
print("-----------------------------------------------")
print()

# remove two common elements of two sets
my_set.remove(11)
my_set.remove(12)
print("-----------------------------------------------")
print("We removed two common elements from First set")
print("Updated first set: ", my_set)
print("-----------------------------------------------")
print()

set_2.remove(11)
set_2.remove(12)
print("-----------------------------------------------")
print("We removed two common elements from Second set")
print("Updated second set: ", set_2)
print("-----------------------------------------------")
print()

print("-----------------------------------------------")
my_set.clear()
print("Cleared First set: ", my_set)
print("-----------------------------------------------")
print()

print("-----------------------------------------------")
set_2.clear()
print("Cleared Second set:", set_2 )
print("-----------------------------------------------")
print()
