#!/usr/bin/env python3

from tkinter import *
import random

# I initialized game window and score
score = 0
color2 = ""
start_num = 60
root = Tk()
root.title("Color Game")
root.geometry("600x500")
root_word_label = Label(root, text="", font=("Helvetica", 50))
root_word_label.pack(pady=20)


# function for initializing functions
def start():
    global start_num
    if start_num == 60:
        text_and_color()
        start_num -= 1
    else:
        answer_checker()


# function for random color and word
def text_and_color():
    global color2
    root_entry.delete(0, END)
    colors = ["red", "yellow", "brown", "blue", "orange", "purple", "pink", "black", "green"]
    index_num1 = random.randint(0, len(colors) - 1)
    color1 = colors[index_num1]
    index_num2 = random.randint(0, len(colors) - 1)
    color2 = colors[index_num2]
    root_word_label.config(text=str(color1), fg=str(color2))


# function for check answer and count score
def answer_checker():
    global score
    if color2.lower().strip() == root_entry.get():
        score += 1
        root_ans_label.config(text="score: " + str(score))
        text_and_color()
    else:
        text_and_color()


# Takes Entries
root_entry = Entry(root, font=("Helvatica", 25))
root_entry.pack(pady=25, padx=25)

# Button for operate functions
root_button = Button(root, text="another word", command=start)
root_button.pack()

# label for score count
root_ans_label = Label(root, text="score:", font=("Helvatica", 20))
root_ans_label.pack(padx=20, pady=20)

# Code for window stay open
root.mainloop()
