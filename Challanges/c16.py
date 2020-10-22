print("Is it raining?")
raining = input("yes/no: ").lower()

if raining == "yes":
    print("Is it windy?")
    windy = input("yes/no: ").lower()
    if windy == "yes":
        print("It's too windy for an umbrella")
    else:
        print("Take an umbrella!")
else:
    print("Enjoy your day!")