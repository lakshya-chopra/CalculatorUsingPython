from tkinter import *
import tkinter.messagebox as tmsg

#Initialisation
root = Tk()
root.geometry('700x650')
root.title('Calculator - Made by Lakshya Chopra')
root.resizable(0, 0)

#Functions
def click(event):
    global scval
    text = event.widget.cget('text')
    if text == "=":
        if scval.get().isdigit():
            value = int(scval.get())
        else:
            try:
                value = eval(scval.get()) 
                scval.set(f"= {value}")
            except Exception as e:
                value = "Error"
                scval.set(f"= {value}")
                tmsg.showinfo('Message','Click on "C" button to clear the error and perform next operation')
    elif text == "C":
        scval.set('')
        screen.update()
    else:
        scval.set(scval.get() + text) 
        screen.update()
        



#GUI Variables    
scval = StringVar()
scval.set('')
screen = Entry(root, textvar=scval, font='lucida 40 bold', bg='#eee') 
screen.grid(row=0, column=0)
screen.pack(fill=X, ipady=7)

f1 = Frame(root, bg='grey' ,bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
f1.pack()

btn = Button(f1, text='C', font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",padx=180)
btn.grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
btn.bind('<Button-1>', click)

btn = Button(f1, text="%", font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
btn.grid(row = 0, column =3, padx = 1, pady = 1)
btn.bind('<Button-1>', click)

btn = Button(f1, text='.', font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
btn.grid(row = 1, column = 0, padx = 1, pady = 1)
btn.bind('<Button-1>', click)


btn = Button(f1, text='9', font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
btn.grid(row = 1, column = 1, padx = 1, pady = 1)
btn.bind('<Button-1>', click)

btn = Button(f1, text='8', font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 1, bg = "#fff", cursor = "hand2")
btn.grid(row = 1, column = 2, padx = 1, pady = 1)
btn.bind('<Button-1>', click)

btn = Button(f1, text='7', font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
btn.grid(row = 1, column = 3, padx = 1, pady = 1)
btn.bind('<Button-1>',click)


btn = Button(f1, text='6', font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
btn.grid(row = 2, column = 0, padx = 1, pady = 1)
btn.bind('<Button-1>', click)

btn = Button(f1, text='5', font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
btn.grid(row = 2, column = 1, padx = 1, pady = 1)
btn.bind('<Button-1>', click)

btn = Button(f1, text='4', font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
btn.grid(row = 2, column = 2, padx = 1, pady = 1)
btn.bind('<Button-1>', click)

btn = Button(f1, text='3', font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
btn.grid(row = 2, column = 3, padx = 1, pady = 1)
btn.bind('<Button-1>', click)

btn = Button(f1, text='2', font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
btn.grid(row = 3, column = 0, padx = 1, pady = 1)
btn.bind('<Button-1>', click)

btn = Button(f1, text='1', font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
btn.grid(row = 3, column = 1, padx = 1, pady = 1)
btn.bind('<Button-1>', click)

btn = Button(f1, text='0', font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
btn.grid(row=3,column=2,padx=1,pady=1)
btn.bind('<Button-1>', click)

btn = Button(f1, text='/', font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
btn.grid(row = 3, column = 3, padx = 1, pady = 1)
btn.bind('<Button-1>', click)

btn = Button(f1, text="*", font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
btn.grid(row = 4, column = 0, padx = 1, pady = 1)
btn.bind('<Button-1>', click)


btn = Button(f1, text='-', font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
btn.grid(row = 4, column = 1, padx = 1, pady = 1)
btn.bind('<Button-1>', click)

btn = Button(f1, text="+", font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
btn.grid(row = 4, column = 2, padx = 1, pady = 1)
btn.bind('<Button-1>', click)

btn = Button(f1, text="=", font='lucida 20 bold',fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
btn.grid(row = 4, column = 3, padx = 1, pady = 1)
btn.bind('<Button-1>', click)


root.mainloop()