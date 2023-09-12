import random
a = []
def algarismos(a):

    z = input("Enter something to randomize:")
    a.append(z)

    c = input("Do you want to put something more?:")
    c = c.upper()
    b = "NO", "YES"

    while c not in b:
        c = input("Do you want to put something more?:")
        c = c.upper()

    if c == "YES":
        algarismos(a)
    else:
        print("From "+ str(a) + " my choice is " + str(random.choice(a)))




algarismos(a)

print("Bye!!")

