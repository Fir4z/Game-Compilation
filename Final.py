Nomes = ["calculadora","random","quizz","rps"]
import random


e = input("What do you wanna play?: ")

while e not in Nomes:
    e = input("What do you wanna play?: ")


#============================================
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

#=========================================

def new_game():

    question_number = 1
    player_score = 0
    guesses = []
    a = ["A","B","C","D"]
    player_answers: []




    for key in Questions:
        print("______________________________")
        print(key)
        for i in Answers[question_number-1]:
            print (i)

        player_answers = input("Resposta: ")
        player_answers = player_answers.upper()
        while player_answers not in a:
            player_answers = input("Resposta: ")
            player_answers = player_answers.upper()

        guesses.append(player_answers)



        player_score  += check_answer(Questions.get(key),player_answers)

    display_score(player_score,guesses)




def check_answer(answer,guess):
    if answer == guess:
        print ("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def display_score(player_score,guesses):
    print("______________________________")
    print("Results : ", end = "")

    for i in guesses:
        print( i, end = " " )
    print ()

    print ("Answers: ", end = " ")

    for i in Questions:
        print( Questions.get(i), end = " " )
    print ()

    a = int(player_score / len(Questions) * 100 )

    print ("Your score was: " + str(a) + "%" )


def play_again():
    a = input("Do you want to play again?:")
    a = a.upper()
    b = "NO","YES"

    while a not in b:
        a = input("Do you want to play again?:")
        a = a.upper()

    if a == "YES":
        return True
    else:
        return False



Questions= {"Quantos dias tem um ano?":"A",
            "Quantos dias tem um mês?":"B",
            "Quantas horas tem um dia?":"C",
            "Quantos minutos tem uma hora?":"D"}

Answers = [["A. 365","B. 200","C.400","D.500"],["A.20","B.31","C.25","D.10"],["A.20","B.21","C.24","D.19"],["A.30","B.50","C.55","D.60"]]







#===========================================
import random

score = 0
loses = 0


def materials():
    a = ["rock", "paper", "scissors"]
    z = random.choice(a)

    choice = input("Enter a material: ").lower()

    while choice not in a:
        choice = input("Enter a material: ").lower()

    if choice == z:

        print("___________________________")
        print("Your choice: " + choice)
        print("Game choice: " + z)
        print("___________________________")
        print("Its a draw!")




    elif choice == "rock":
        if z == "paper":
            print("___________________________")
            print("Your choice: " + choice)
            print("Game choice: " + z)
            print("___________________________")
            print("You Win!!")

            return 2

        if z == "scissors":
            print("___________________________")
            print("Your choice: " + choice)
            print("Game choice: " + z)
            print("___________________________")
            print("You lost!")

            return 0


    elif choice == "paper":
        if z == "rock":
            print("___________________________")
            print("Your choice: " + choice)
            print("Game choice: " + z)
            print("___________________________")
            print("You Win!!")

            return 2

        if z == "scissors":
            print("___________________________")
            print("Your choice: " + choice)
            print("Game choice: " + z)
            print("___________________________")
            print("You lost!")

            return 0



    elif choice == "scissors":
        if z == "paper":
            print("___________________________")
            print("Your choice: " + choice)
            print("Game choice: " + z)
            print("___________________________")
            print("You Win!!")

            return 2

        if z == "rock":
            print("___________________________")
            print("Your choice: " + choice)
            print("Game choice: " + z)
            print("___________________________")
            print("You lost!")

            return 0


def play_again():
    a = ["yes", "no"]

    b = input("Do you want to play again: ").lower()

    while b not in a:
        b = input("Do you want to play again: ").lower()

    if b == "yes":
        return True
    else:
        return False


#=======================================

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



if e == "calculadora":
    number1 = numInput(number1)
    Simbolo = symbol(Simbolo)
    number2 = numInput2(number2)
    Resultado = calc(number1, number2, Simbolo, Resultado)
    resultado(Resultado)

    while replay():
        number1 = numInput(number1)
        Simbolo = symbol(Simbolo)
        number2 = numInput2(number2)
        Resultado = calc(number1, number2, Simbolo, Resultado)
        resultado(Resultado)

    print("Bye!!")


elif e == "random":
    algarismos(a)

    print("Bye!!")

elif e == "quizz":
    new_game()

    while play_again():
        new_game()

    print("Bye!!")

else:
    if materials() == 0:
        loses = loses + 1


    else:
        score = score + 1

    print("You have lost :" + str(loses) + " times ")
    print("And You have won :" + str(score) + " times ")

    while play_again():
        if materials() == 0:
            loses = loses + 1
        else:
            score = score + 1

        print("You have lost :" + str(loses) + " times ")
        print("And You have won :" + str(score) + " times ")

    print("Bye!!")




 #=====================================











