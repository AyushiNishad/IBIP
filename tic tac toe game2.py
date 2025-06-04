
from tkinter import *
import tkinter.messagebox as mb

# Initialize window
tk = Tk()
tk.title('Tic Tac Toe')
p1 = StringVar()
p2 = StringVar()
p1_turn = True
flag = 0

def btn_click(bu):
    global p1_turn, flag
    if bu['text'] == '' and p1_turn:
        bu['text'] = 'X'
        p1_turn = False
        flag += 1
        check_winner()
    elif bu['text'] == '' and not p1_turn:
        bu['text'] = '0'
        p1_turn = True
        flag += 1
        check_winner()
    else:
        mb.showinfo('Tic Tac Toe', 'Grid already filled')

def check_winner():
    combos = [
        (btn1, btn2, btn3),
        (btn4, btn5, btn6),
        (btn7, btn8, btn9),
        (btn1, btn4, btn7),
        (btn2, btn5, btn8),
        (btn3, btn6, btn9),
        (btn1, btn5, btn9),
        (btn3, btn5, btn7),
    ]

    for combo in combos:
        if combo[0]['text'] == combo[1]['text'] == combo[2]['text'] != '':
            winner = p1.get() if combo[0]['text'] == 'X' else p2.get()
            if not winner:
                winner = "Player 1" if combo[0]['text'] == 'X' else "Player 2"
            mb.showinfo('Tic Tac Toe', winner + " Wins!")
            disable_buttons()
            return

    if flag == 8:
        mb.showinfo('Tic Tac Toe', 'It is a Tie')
        disable_buttons()

def disable_buttons():
    for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
        btn.configure(state=DISABLED)

def restart_button():
    global flag, p1_turn
    flag = 0
    p1_turn = True
    player1.delete(0, END)
    player2.delete(0, END)
    for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
        btn['text'] = ''
        btn.configure(state=NORMAL)

# UI setup
l1 = Label(tk, text='Player 1 (X):', font='Times 12 bold', fg='black')
l1.grid(row=0, column=0)
player1 = Entry(tk, textvariable=p1, bd=5)
player1.grid(row=0, column=1)

l2 = Label(tk, text='Player 2 (0):', font='Times 12 bold', fg='black')
l2.grid(row=1, column=0)
player2 = Entry(tk, textvariable=p2, bd=5)
player2.grid(row=1, column=1)

restart = Button(tk, text='Restart', font='Times 15 bold', bg='brown', fg='white', command=restart_button)
restart.grid(row=1, column=2)

# Game board buttons
btn1 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn1))
btn1.grid(row=2, column=0)

btn2 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn2))
btn2.grid(row=2, column=1)

btn3 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn3))
btn3.grid(row=2, column=2)

btn4 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn4))
btn4.grid(row=3, column=0)

btn5 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn5))
btn5.grid(row=3, column=1)

btn6 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn6))
btn6.grid(row=3, column=2)

btn7 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn7))
btn7.grid(row=4, column=0)

btn8 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn8))
btn8.grid(row=4, column=1)

btn9 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn9))
btn9.grid(row=4, column=2)

tk.mainloop()




   
   


   


