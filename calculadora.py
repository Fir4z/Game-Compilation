
number1 = None
number2 = None
Resultado = 0
Simbolo = None




def numInput(number1):
    number1 = input("Tell me a number: ").lower()
    if number1 == "x":
        return Resultado
    elif number1.isdigit():
        return number1
    else:
        print ("You must enter a number (i.e. 0,1,2...or x for the previews result)")
        numInput(number1)

def numInput2(number2):
    number2 = input("Tell me a second number: ").lower()
    if number2 == "x":
        return Resultado
    elif number2.isdigit():
        return number2
    else:
        print("You must enter a number (i.e. 0,1,2... or x for the previews result)")
        numInput2(number2)

def symbol(Simbolo):
    a = ["+","-","*","/"]
    Simbolo = input("Enter an operation symbol: ")
    if Simbolo not in a:
        print ("Enter a valid symbol!!")
        symbol(Simbolo)
    else:
        return Simbolo

def calc(n1,n2,s,r):
    n1 = int(n1)
    n2 = int(n2)
    if s == "+":
        r = n1+n2
        return r
    elif s == "-":
        r = n1-n2
        return r
    elif s == "*":
        r = n1* n2
        return r
    elif s == "/":
        r = n1/n2
        return r

def replay():
    a = input("Do you want to play again?:")
    a = a.upper()
    b = "NO", "YES"

    while a not in b:
        a = input("Do you want to play again?:")
        a = a.upper()

    if a == "YES":
        return True
    else:
        return False

def resultado(a):
    a = str(a)
    print("The total is : "+a)

number1 = numInput(number1)
Simbolo = symbol(Simbolo)
number2 = numInput2(number2)
Resultado = calc(number1,number2,Simbolo,Resultado)
resultado(Resultado)

while replay():
    number1 = numInput(number1)
    Simbolo = symbol(Simbolo)
    number2 = numInput2(number2)
    Resultado = calc(number1, number2, Simbolo, Resultado)
    resultado(Resultado)

print ("Bye!!")

