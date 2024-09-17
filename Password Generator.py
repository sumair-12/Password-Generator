from tkinter import *
from tkinter import messagebox
import os



root = Tk()
root.configure(bg="#282828")

root.geometry("400x400")
root.title("Folder Generator")
root.resizable(height=False,width=False)
icon_image = PhotoImage(file="F:/newfil/Folder Generator.png")
root.iconphoto(True,icon_image)

folder_gen = Label(root,text="Folder Generator",bg="#282828",fg="#3eb3d4",font=("Mogra","30"))

path_name = Label(root,text="Enter Path :",bg="#282828",fg="#ffffff")
path_entry = Entry(root,width=20,borderwidth=0)

fname = Label(root,text="Enter folder name :",bg="#282828",fg="#ffffff")
fentry = Entry(root,width=20,borderwidth=0)

tname = Label(root,text="Enter how many folders\n you want to create :",bg="#282828",fg="#ffffff")
tentry = Entry(root,width=20,borderwidth=0)

subname = Label(root,text="Enter Sub Folders Name :",bg="#282828",fg="#ffffff")
subentry = Entry(root,width=20,borderwidth=0)


def working():
    folder = os.path.join(path_entry.get(),fentry.get())
    number = tentry.get()
    if (not os.path.exists(f"{folder}")):
        os.mkdir(f"{folder}")
    for x in range(0,int(number)):
        os.mkdir(f"{folder}/{subentry.get()} {x+1}")
    path_entry.delete(0,END)
    fentry.delete(0,END)
    tentry.delete(0, END)
    subentry.delete(0, END)

    messagebox.showinfo("Folders Generated",f"{number} folders generated successfully!")


generate = Button(root,text="Generate",borderwidth=0,
                  bg="#3eb3d4",
                  activebackground="#34c1ea",
                  fg="#ffffff",
                  activeforeground="#ffffff",
                  height=1,
                  width=15,
                  command=working
                  )
folder_gen.pack(pady=30)
path_name.place(x=85,y=110)
path_entry.place(x=220,y=110)
fname.place(x=65,y=160)
fentry.place(x=220,y=160)
tname.place(x=50,y=205)
tentry.place(x=220,y=210)
subname.place(x=50,y=260)
subentry.place(x=220,y=260)
generate.place(x=150,y=330)

root.mainloop()