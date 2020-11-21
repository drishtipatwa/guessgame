from tkinter import *
import random as r
win = Tk()
f = ("Algerian",16)
win.title("Guessing Game")
num = StringVar()
l1 = Label(win, font= f,text = 'Enter your guess:')
en = Entry(win,font = f,width=4,textvariable=num)
l1.grid(column=0,row=1)
en.grid(column = 1, row = 1)
l2 = Label(win, font = f,text = 'Won / Lose',fg = 'red')
n = r.randint(1000,9999)
guesses = 0
temp = n
def click():
	global l3, b1, b2, l2
	l2.configure(text = "Play Again")
	l3.configure(text = "")
	b1.destroy()
	b2.destroy()
	n = r.randint(1000,9999)
	global guesses
	guesses = 0
	global temp
	temp = n
def closee():
	res = "Thank you for playing"
	l2.configure(text = res)
	global b1,b2,bt, en
	b1.destroy()
	b2.destroy()
	bt.destroy()
	en.destroy()
	res=" "
	l1.configure(text = res)
	l3.configure(text = res)
	win.after(5000, lambda: win.destroy())
def clicked():
	global guesses
	guesses += 1
	x = num.get()
	global n
	global temp
	n = temp
	y=''
	if x==str(n):
		res = 'Won in '+str(guesses)+ ' Guesses'
		l2.configure(text = res)
		global l3, b1, b2
		l3 = Label(win, font = f, text= " Do you wanna continue?")
		b1 = Button(win, text = 'yes', command = click)
		b2 = Button(win, text = 'no', command= closee)
		l3.grid(row=5, column=0)
		b1.grid(row=5, column =1)
		b2.grid(row=5, column = 2)

	else:
		c =0
		if len(x)==4:
			y = str(x)
			m = str(n)
			for i in range(4):
				if y[i]==m[i]:
					c+=1
			res = str(c) +" points. Try again"+str(n)
			l2.configure(text = res)
		else:
			res='Enter 4 digit number'
			l2.configure(text=res)

bt = Button(win, text = 'Check', command = clicked)
l3 = Label(win, font = f, text= " Do you wanna continue?")
b1 = Button(win, text = 'yes', command = click)
b2 = Button(win, text = 'no', command= closee)
l2.grid(row = 6, column = 1)
bt.grid(row =4, column = 1)
win.geometry('600x200')
win.mainloop()
