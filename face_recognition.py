from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
from tkinter import messagebox

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x780+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1400, height=44)

        img_top_path = os.path.join(os.getcwd(), "college_images", "face_detector1.jpg")
        if os.path.isfile(img_top_path):
            img_top = Image.open(img_top_path)
        else:
            messagebox.showerror("Error", f"File not found: {img_top_path}")
            img_top = Image.open(os.path.join(os.getcwd(), "default_image.jpg"))  # Use a default image if the specified image is not found

        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_bottom_path = os.path.join(os.getcwd(), "college_images", "detection1.jpg")
        if os.path.isfile(img_bottom_path):
            img_bottom = Image.open(img_bottom_path)
        else:
            messagebox.showerror("Error", f"File not found: {img_bottom_path}")
            img_bottom = Image.open(os.path.join(os.getcwd(), "default_image.jpg"))  # Use a default image if the specified image is not found

        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="black", command=self.face_recognition)
        b1_1.place(x=350, y=600, width=200, height=40)

    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
        coords = []
        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
            id, confidence = clf.predict(gray_image[y:y + h, x:x + w])
            print(f"Detected ID: {id}, Confidence: {confidence}")
            if confidence < 100:
                confidence = 100 - confidence  # Adjust confidence to a more intuitive range (0-100)
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="programmer@123", database="face_recognizer")
                    cur = conn.cursor()

                    cur.execute("SELECT Name FROM student WHERE Student_id = %s", (id,))
                    n = cur.fetchone()
                    n = n[0] if n else "Unknown"
                    print(f"Name: {n}")

                    cur.execute("SELECT Roll FROM student WHERE Student_id = %s", (id,))
                    r = cur.fetchone()
                    r = r[0] if r else "Unknown"
                    print(f"Roll: {r}")

                    cur.execute("SELECT Dep FROM student WHERE Student_id = %s", (id,))
                    d = cur.fetchone()
                    d = d[0] if d else "Unknown"
                    print(f"Department: {d}")

                    if confidence > 77:
                        cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Confidence:{confidence:.2f}%", (x, y + h + 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                except Exception as e:
                    messagebox.showerror("Error", f"Database error: {str(e)}")
                finally:
                    conn.close()
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            coords = [x, y, w, h]
        return coords

    def recognize(self, img, clf, faceCascade):
        coords = self.draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face", clf)
        return img

    def face_recognition(self):
        faceCascade_path = os.path.join(os.getcwd(), "haarcascade_frontalface_default.xml")
        if os.path.isfile(faceCascade_path):
            faceCascade = cv2.CascadeClassifier(faceCascade_path)
        else:
            messagebox.showerror("Error", f"File not found: {faceCascade_path}")
            return

        classifier_path = os.path.join(os.getcwd(), "classifier.xml")
        if os.path.isfile(classifier_path):
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read(classifier_path)
        else:
            messagebox.showerror("Error", f"File not found: {classifier_path}")
            return

        video_cap = cv2.VideoCapture(0)

        if not video_cap.isOpened():
            messagebox.showerror("Error", "Unable to open camera")
            return

        while True:
            ret, img = video_cap.read()
            if not ret:
                messagebox.showerror("Error", "Unable to capture frame from camera")
                break
            img = self.recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)
            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break
        video_cap.release()
        