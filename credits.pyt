credits = int(input("Please Input Your Credits: "))

if credits <= 23:
    print(credits, " The student is Freshman. ")

elif credits >= 24 and credits <= 53:
    print(credits, " The student is Sophomore. ")

elif credits >= 54 and credits <= 83:
    print(credits, " The student is Juniors. ")

elif credits > 84:
    print(credits, " The student is Seniors. ")