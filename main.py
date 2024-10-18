from tkinter import *                                                                                                                                                                                                                                                                                                                                
from tkinter import ttk 
from PIL import Image, ImageTk
from student import Student
import os
import tkinter
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from train import train
from  help import Help
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # first image
        img = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\Stanford.jpg")
        img = img.resize((500, 130), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg= ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        
        #second image
        img1 = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\facialrecognition.png")
        img1 = img1.resize((500, 130), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg1 = ImageTk.PhotoImage(img1)
          
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)
        
        # Third Image
        img2 = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\u.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=450, height=130)
        
        #bg image
        
        img3 = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\wp2551980.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS"
        self.photoimg3 = ImageTk.PhotoImage(img3)
    
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=44)

        #*****************************time
        def time():
          string =strftime('%H:%M:%S %p')
          lbl.config(text = string)
          lbl.after(1000,time)

        lbl = Label(title_lbl,font=('times new roman',14,'bold'),background = 'white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        # student button
        img4 = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\student.jpg")
        img4 = img4.resize((200, 200), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_detalis,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Detalis",command=self.student_detalis,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=200,y=300,width=220,height=40)
         
         # Detect face
        img5 = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\face_detector1.jpg")
        img5 = img5.resize((300, 200), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=500,y=300,width=220,height=40)
         
         # Attendace
        img6 = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\report.jpg")
        img6 = img6.resize((300, 300), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendace",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=800,y=300,width=220,height=40)
         
        # Help face button
        img7 = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\help desk.jpg")
        img7 = img7.resize((300, 300), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        # train
        img8 = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\Train.jpg")
        img8 = img8.resize((300, 300), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=360,width=220,height=200)

        b1_1=Button(bg_img,text="Train",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=200,y=530,width=220,height=40)
        
        #Photos face button
        img9 = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\train data.jpg")
        img9 = img9.resize((300, 300), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2", command=self.open_img)
        b1.place(x=500,y=360,width=220,height=200)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=500,y=530,width=220,height=40)
        
        #Developer
        img10 = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\Team-Management-Software-Development.jpg")
        img10 = img10.resize((300, 300), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,command=self.developer_data,cursor="hand2")
        b1.place(x=800,y=360,width=220,height=200)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=800,y=530,width=220,height=40)
        
         #Exit
        img11 = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\exit.jpg")
        img11 = img11.resize((300, 300), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=360,width=220,height=200)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=1100,y=530,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recogition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
           self.root.destroy()
        else:
            return
         
        #******************* Function buttons **************#
        
    def student_detalis(self):

       self.new_window=Toplevel(self.root)
       self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
   
   
        
        
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()