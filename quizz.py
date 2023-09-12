
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



new_game()

while play_again():
    new_game()

print("Bye!!")




