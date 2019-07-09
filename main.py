from tkinter import *

window= Tk()

window.title("Simple GUI")

window.geometry("500x300")

label1 = Label(window, text ="Welcome to this program!", fg ='blue',bg ='yellow', relief ="solid", font =("arial",16,"bold"))
label1.pack()

lblURL = Label(window, text='Input URL:',font =("arial",12,"bold")).place(x=37,y=55)
lblExpression = Label(window, text='Input Key:',font =("arial",12,"bold")).place(x=37,y=110)

t = Text(window, width=35, height=2,font =("arial",12,"bold")).place(x=130,y=50)
t = Text(window, width=35, height=2,font =("arial",12,"bold")).place(x=130,y=110)


button1 =Button(window, text="Click Me!",fg='white',bg='brown', relief=GROOVE, font =("arial",16,"bold"))
button1.place(x=200,y=210)

button1.bind('<Double-1>', lambda e: label1.configure(text='Moved mouse inside'))






window.mainloop()
