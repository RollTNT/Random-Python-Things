#! /usr/bin/env python
from tkinter import *
import tkinter.messagebox as box
import random
#This may not be the latest version. Rmember to find the latest version at The wiered site...
window = Tk()
window.title( 'Dice Roller 2.1.2' )
#book = IntVar()
#\/sets the atributes modifiers\/ (radio buttons)
#r0 = Radiobutton( window, text = '+0', variable = book, value = 0 )
#r1 = Radiobutton( window, text = '+1', variable = book, value = 1 )
#r2 = Radiobutton( window, text = '+2', variable = book, value = 2 )
#r3 = Radiobutton( window, text = '+3', variable = book, value = 3 )
#r4 = Radiobutton( window, text = '+4', variable = book, value = 4 )
#r5 = Radiobutton( window, text = '+5', variable = book, value = 5 )
#r6 = Radiobutton( window, text = '+6', variable = book, value = 6 )
#r7 = Radiobutton( window, text = '+7', variable = book, value = 7 )
#r8 = Radiobutton( window, text = '+8', variable = book, value = 8 )
#r9 = Radiobutton( window, text = '+9', variable = book, value = 9 )
#\/Commands for rolling the dice\/
def entry() :
	box.showinfo( 'Creator:', 'Created by Charlie Lugardo.\nAll code copyright of Charlie Lugardo 2020' )
def rtwo() :
#	var = box.askYesno( 'Are You Sure', 'Are You sure You want to roll a d2?' )
#	if var == 1 :
	nums = random.sample( range( 1, 3 ) , 1 )
	box.showinfo( 'd2 roll', 'You rolled a ' + str(nums[0]) )
#	else :
#		box.showerror( 'Cancelled', 'Cancelled' )
def rfou() :
#	var = box.askYesno( 'Are You Sure', 'Are You sure You want to roll a d4?' )
#	if var == 1 :
	nums = random.sample( range( 1, 5 ) , 1 )
	box.showinfo( 'd2 roll', 'You rolled a ' + str(nums[0]) )
#	else :
#		box.showerror( 'Cancelled', 'Cancelled' )
def rsix() :
#	var = box.askYesno( 'Are You Sure', 'Are You sure You want to roll a d6?' )
#	if var == 1 :
	nums = random.sample( range( 1, 7 ) , 1 )
	box.showinfo( 'd2 roll', 'You rolled a ' + str(nums[0]) )
#	else :
#		box.showerror( 'Cancelled', 'Cancelled' )
def reig() :
#	var = box.askYesno( 'Are You Sure', 'Are You sure You want to roll a d8?' )
#	if var == 1 :
	nums = random.sample( range( 1, 9 ) , 1 )
	if int(nums[0]) == 8 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	else :
		box.showinfo( 'd2 roll', 'You rolled a ' + str(nums[0]) )
#	else :
#		box.showerror( 'Cancelled', 'Cancelled' )
def rten() :
#	var = box.askYesno( 'Are You Sure', 'Are You sure You want to roll a d10?' )
#	if var == 1 :
	nums = random.sample( range( 1, 11 ) , 1 )
	if int(nums[0]) == 8 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	else :
		box.showinfo( 'd2 roll', 'You rolled a ' + str(nums[0]) )
#	else :
#		box.showerror( 'Cancelled', 'Cancelled' )
def rtwel() :
#	var = box.askYesno( 'Are You Sure', 'Are You sure You want to roll a d12?' )
#	if var == 1 :
	nums = random.sample( range( 1, 13 ) , 1 )
	if int(nums[0]) == 8 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 11 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	else :
		box.showinfo( 'You Rolled...', 'You rolled a ' + str(nums[0]) )
#	else :
#		box.showerror( 'Cancelled', 'Cancelled' )
def rtwen() :
#	var = box.askYesno( 'Are You Sure', 'Are You sure You want to roll a d20?' )
#	if var == 1 :
	nums = random.sample( range( 1, 21 ) , 1 )
	if int(nums[0]) == 8 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 11 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 18 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 20 :
		box.showinfo( 'CRIT!','Congrats,You rolled a '+str(nums[0])+'!' )
	elif int(nums[0]) == 1 :
		box.showinfo( 'oops!','ooh, sorrY. You rolled a '+str(nums[0])+'...' )

	else :
		box.showinfo( 'You Rolled...', 'You rolled a ' + str(nums[0]) )
#	else :
#		box.showerror( 'Cancelled', 'Cancelled' )
def rhun() :
#	var = box.askYesno( 'Are You Sure', 'Are You sure You want to roll a d100?' )
#	if var == 1 :
	nums = random.sample( range( 1, 101 ) , 1 )
	if int(nums[0]) == 8 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 11 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 100 :
		box.showinfo( 'You Rolled...', 'Wow! You rolled a ' +str(nums[0])+'!' )
	elif int(nums[0]) == 11 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 11 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 18 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 80 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 81 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 82 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 83 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 84 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 85 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 86 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 87 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 88 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	elif int(nums[0]) == 89 :
		box.showinfo( 'You Rolled...', 'You rolled an ' +str(nums[0]) )
	else :
		box.showinfo( 'You Rolled...', 'You rolled a ' + str(nums[0]) )
#	else :
#		box.showerror( 'Cancelled', 'Cancelled' )
#\/sets up the buttons\/ 
d2 = Button( window , text = '  1d2  ' , command=rtwo, bg='#97B4D2', fg='#090031' )
d4 = Button( window , text = '  1d4  ' , command=rfou, bg='#97B4D2', fg='#090031' )
d6 = Button( window , text = '  1d6  ' , command=rsix, bg='#97B4D2', fg='#090031' )
d8 = Button( window , text = '  1d8  ' , command=reig, bg='#97B4D2', fg='#090031' )
d10 = Button( window , text = ' 1d10 ' , command=rten, bg='#97B4D2', fg='#090031' )
d12 = Button( window , text = ' 1d12 ' , command=rtwel, bg='#97B4D2', fg='#090031' )
d20 = Button( window , text = ' 1d20 ' , command=rtwen, bg='#97B4D2', fg='#090031' )
d100 = Button( window , text = '1d100' , command=rhun, bg='#97B4D2', fg='#090031' )
exit = Button( window , text = '  Exit  ' , command=exit, bg='#97B4D2', fg='#090031' )
label = Label( window,text='  Created  ',bg='#97B4D2',fg='#090031' )
labela = Label( window,text=' by  Charlie',bg='#97B4D2',fg='#090031' )
labelb = Label( window,text='   lugardo ',bg='#97B4D2',fg='#090031' )
#\/places the dice\/
entry()
d2.grid( row = 1, column = 1 )
d4.grid( row = 1, column = 2 )
d6.grid( row = 1, column = 3 )
d8.grid( row = 2, column = 1 )
d10.grid( row = 2, column = 2 )
d12.grid( row = 2, column = 3 )
d20.grid( row = 3, column = 1 )
d100.grid( row = 3, column = 2 )
exit.grid( row = 3, column = 3 )
label.grid(row = 4,column=1)
labela.grid(row = 4,column=2)
labelb.grid(row = 4,column=3)
#\/places the radio buttons\/
#r0.grid( row = 1, column = 4 )
#r1.grid( row = 2, column = 4 ) 
#r2.grid( row = 3, column = 4 )
#r3.grid( row = 4, column = 4 )
#r4.grid( row = 1, column = 5 )
#r5.grid( row = 2, column = 5 )
#r6.grid( row = 3, column = 5 )
#r7.grid( row = 4, column = 5 )
#r8.grid( row = 1, column = 6 )
#r9.grid( row = 2, column = 6 )
window.mainloop()
