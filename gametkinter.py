from tkinter import *
import random

num = random.randint (1 , 100)

def Check() :
    guess = int(number.get())
    if guess == num :
        result_label.config(text="congratulation  , you win 👏🏻!!")
    elif guess < num :
        result_label.config(text=" try More !")
    else:
        result_label.config(text="try Less !")
game =Tk()
game.title("GUESS THE NUMBER !")

Label(game, text="Guess a Nunmber Between 1 And 100").pack()
number = Entry(game)
number.pack()

Button ( game, text="Check!", command=Check).pack()

result_label = Label (game, text="")
result_label.pack()
game.mainloop()