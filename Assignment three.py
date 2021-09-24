from tkinter import *
root=Tk()
root.title("Question and Answer")
root.geometry("800x600")
root.configure(bg="blue")




welcome=("Welcome\n Press next to read Game Rules")
rules=("""
A lives in the corner’s house 
C is between E and G,
There is 1 house between D and F
F is neighbor of G and,
There are two houses between A and G.
""")

questions=("""
1. Who lives in the second corner?\n
2. Who lives in the middle?\n
3. Who lives between B and G?\n
4. Who is the neighbor of A?\n
5. How many houses are there between B and E?\n
""")

def question():
    label.configure(text=questions)
    label.place(x=10,y=100)
    buttun.configure(command=evaluation)
    entry_1.place(x=500, y=125)
    entry_2.place(x=500, y=180)
    entry_3.place(x=500, y=235)
    entry_4.place(x=500, y=290)
    entry_5.place(x=500, y=345)


def show():
    label.configure(text=rules)
    label.place(x=100, y=100)
    buttun.configure(command=question)

def evaluation():
    Q1 = str(entry_1.get())
    Q2 = str(entry_2.get())
    Q3 = str(entry_3.get())
    Q4 = str(entry_4.get())
    Q5 = str(entry_5.get())

    if Q1 == "D" or Q1 == "d":
        output_label1.configure(text="You are correct",bg="green")
    elif Q1 != "D" or Q1 != "d":
        output_label1.configure(text="You are wrong! Try again",bg="red")
    if Q2 == "G" or Q2 == "g":
        output_label2.configure(text="You are correct",bg="green")
    elif Q2 != "G" or Q2 != "g":
        output_label2.configure(text="You are wrong! Try again",bg="red")
    if Q3 == "F" or Q3 == "f":
        output_label3.configure(text="You are correct",bg="green")
    elif Q3 != "F" or Q3 != "f":
        output_label3.configure(text="You are wrong! Try again",bg="red")
    if Q4 == "E" or Q4 == "e":
        output_label4.configure(text="You are correct",bg="green")
    elif Q4 != "E" or Q4 != "e":
        output_label4.configure(text="You are wrong! Try again",bg="red")
    if Q5 == "3":
        output_label5.configure(text="You are correct",bg="green")
    elif Q5 != "3":
        output_label5.configure(text="You are wrong! Try again",bg="red")

    output_label1.place(x=500, y=125)
    output_label2.place(x=500, y=180)
    output_label3.place(x=500, y=235)
    output_label4.place(x=500, y=290)
    output_label5.place(x=500, y=345)




label=Label(root, text=welcome, font=("times new roman", 18), bg="blue", fg="white")
label.place(x=200,y=200 )
entry_1 = Entry(font="algerian", width=5)
entry_2 = Entry(font="algerian", width=5)
entry_3 = Entry(font="algerian", width=5)
entry_4 = Entry(font="algerian", width=5)
entry_5 = Entry(font="algerian", width=5)


output_label1 = Label(font="liberation 15 ")
output_label2 = Label(font="liberation 15 ")
output_label3 = Label(font="liberation 15 ")
output_label4 = Label(font="liberation 15 ")
output_label5 = Label(font="liberation 15 ")


buttun=Button(root, text="Next", font=("times new roman", 18), bg="white", fg="black", command=show)
buttun.place(x=300, y=400)

root.mainloop()