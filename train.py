from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np
from tkinter import messagebox



class train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x780+0+0")
        self.root.title("Face Recognition System")

        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1400,height=44)
        
        img_top = Image.open(r"C:college_images\facialrecognition.png")
        img_top = img_top.resize((1530, 325), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

         # button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="white",fg="black")
        b1_1.place(x=0,y=380,width=1530,height=60)

        img_bottom = Image.open(r"C:college_images\detection1.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)




    def train_classifier(self):
        data_dir=("data")
        path=[ os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        face_image=[]
        ids=[]


        for image in path:
            img=Image.open(image).convert('L')    #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            face_image.append(imageNp)
            ids.append(id)
            cv2.imshow("Tranning",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Initialize the face recognizer
        
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(face_image,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Tranning datasets completed!!")
    def load_classifier():
        return cv2.face.LBPHFaceRecognizer_create().read("classifier.xml")      

        
        
        

        




if __name__ == "__main__": 
    root = Tk() 
    obj = train(root) 
    root.mainloop()