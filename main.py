from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognise import Face_Recognition


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

#first image
        img=Image.open(r"D:\Desktop\Computer Science\Facial Recognition based attendance system\collect_images\stanford_image.jpg")
        img=img.resize((520,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=520,height=130)

#second image

        img1=Image.open(r"D:\Desktop\Computer Science\Facial Recognition based attendance system\collect_images\fc_recog.jpg")
        img1=img1.resize((520,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=520,height=130)

#third image

        img2=Image.open(r"D:\Desktop\Computer Science\Facial Recognition based attendance system\collect_images\college.jpg")
        img2=img2.resize((530,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=530,height=130)

    

#bg image
        img3=Image.open(r"D:\Desktop\Computer Science\Facial Recognition based attendance system\collect_images\bg_img.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bgimg=Label(self.root,image=self.photoimg3)
        bgimg.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bgimg,text="FACIAL RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

#student button

        img4=Image.open(r"D:\Desktop\Computer Science\Facial Recognition based attendance system\collect_images\student.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bgimg,image=self.photoimg4,command=self.student_details,cursor="hand2")  
        b1.place(x=200,y=100,width=220,height=220)

        b1=Button(bgimg,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")  
        b1.place(x=200,y=300,width=220,height=40)

#detect face button

        img5=Image.open(r"D:\Desktop\Computer Science\Facial Recognition based attendance system\collect_images\face_dect.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bgimg,image=self.photoimg5,cursor="hand2",command=self.face_data)  
        b1.place(x=500,y=100,width=220,height=220)

        b1=Button(bgimg,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")  
        b1.place(x=500,y=300,width=220,height=40)

#attendance face button

        img6=Image.open(r"D:\Desktop\Computer Science\Facial Recognition based attendance system\collect_images\attendance.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bgimg,image=self.photoimg6,cursor="hand2")  
        b1.place(x=800,y=100,width=220,height=220)

        b1=Button(bgimg,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")  
        b1.place(x=800,y=300,width=220,height=40)

#Help desk button

        img7=Image.open(r"D:\Desktop\Computer Science\Facial Recognition based attendance system\collect_images\help.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bgimg,image=self.photoimg7,cursor="hand2")  
        b1.place(x=1100,y=100,width=220,height=220)

        b1=Button(bgimg,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")  
        b1.place(x=1100,y=300,width=220,height=40)

        #Train button

        img8=Image.open(r"D:\Desktop\Computer Science\Facial Recognition based attendance system\collect_images\train.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bgimg,image=self.photoimg8,cursor="hand2",command=self.train_data)  
        b1.place(x=200,y=380,width=220,height=220)

        b1=Button(bgimg,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")  
        b1.place(x=200,y=580,width=220,height=40)

         #Photos

        img9=Image.open(r"D:\Desktop\Computer Science\Facial Recognition based attendance system\collect_images\photos.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bgimg,image=self.photoimg9,cursor="hand2",command=self.open_img)  
        b1.place(x=500,y=380,width=220,height=220)

        b1=Button(bgimg,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")  
        b1.place(x=500,y=580,width=220,height=40)

        #Developer button

        img10=Image.open(r"D:\Desktop\Computer Science\Facial Recognition based attendance system\collect_images\developer.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bgimg,image=self.photoimg10,cursor="hand2")  
        b1.place(x=800,y=380,width=220,height=220)

        b1=Button(bgimg,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")  
        b1.place(x=800,y=580,width=220,height=40)

        #Exit button

        img11=Image.open(r"D:\Desktop\Computer Science\Facial Recognition based attendance system\collect_images\exit.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bgimg,image=self.photoimg11,cursor="hand2")  
        b1.place(x=1100,y=380,width=220,height=220)

        b1=Button(bgimg,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")  
        b1.place(x=1100,y=580,width=220,height=40)
    
    def open_img(self):
        os.startfile("data")
# ===================Function buttons===================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()




    

