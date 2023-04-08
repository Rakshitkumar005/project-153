from tkinter import *
import random

root=Tk()
root.title("TESTING RANDOM FUNCTION")
root.geometry("500x500")

input_password=Entry(root)
guessed_password_label=Label(root)
generated_password=Label(root)

array_3d=[[["0","1","2","3","4","5","6"],["Head","Tail"],["A","B","C","D","E","F","G","H"]]]


def generatePassword():
    random1=random.randint(0, 5)
    random2=random.randint(0, 1)
    random3=random.randint(0, 7)
    
    letter1=array_3d[0][0][random1]
    letter2=array_3d[0][1][random2]
    letter3=array_3d[0][2][random3]
    
    guessed_password_label["text"]="Guessed Password : "+input_password.get()
    generated_password["text"]="Generated Password : "+letter1+""+letter2+""+letter3

btn=Button(root,text="New Password",command=generatePassword)  

input_password.place(relx=0.5,rely=0.3,anchor=CENTER)
guessed_password_label.place(relx=0.5,rely=0.4,anchor=CENTER)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
generated_password.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()  