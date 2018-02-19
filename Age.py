def start():
    your_age=input("Enter your Age")
    age = float(your_age)
    if age > 13:
        print("You are %s years too old" % (age - 13))
    elif age < 13:
        print("You are %s years too young" % (13-age))
    elif age == 13:
        print("You are just the right age!!")
    start()
