tuple_list = []
while True:
    user_input = input("Enter a tuple (or type 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    else:
        try:
            tuple_values = tuple(map(int, user_input.split(',')))
            if len(tuple_values) >= 2:  # Ensure that the tuple has at least 2 elements
                tuple_list.append(tuple_values)
            else:
                print("Invalid input. Tuple should have at least two elements.")
        except ValueError:
            print("Invalid input. Please enter integers separated by comma.")

k = int(input("Enter the value of K: "))

filtered_tuples = [(tup[0], tup[1]) for tup in tuple_list if len(tup) >= 2 and tup[0] % k == 0 and tup[1] % k == 0]

if filtered_tuples:
    print("Tuples divisible by {}: {}".format(k, filtered_tuples))
else:
    print("There are no tuples in the list that are divisible by {}.".format(k))
