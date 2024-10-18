from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x780+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="BLUE")
        title_lbl.place(x=0,y=0,width=1400,height=44)
        
        img_top = Image.open(r"C:college_images\help3.jpeg")
        img_top = img_top.resize((1530, 720), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1530, height=720)

        dep_label=Label(f_lbl,text="Email:minalwaghmode2@gmail.com",font=("times new roman",20,"bold"),fg="white",bg="black")
        dep_label.place(x=650,y=200)

        dep_label=Label(f_lbl,text=" Contact us:- +91 9529334378",font=("times new roman",20,"bold"),fg="white",bg="black")
        dep_label.place(x=700,y=250)









if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()