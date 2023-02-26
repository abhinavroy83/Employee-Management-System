from cgitb import grey
from msilib import text
from tkinter import *

from tkinter import ttk, messagebox
import cx_Oracle
class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Sign Up")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")
        frame1=Frame(self.window,bg="cadetblue",)
        frame1.place(x=0,y=0,relwidth=1,relheight=1)


        frame = Frame(self.window, bg="white")
        frame.place(x=400,y=100,width=500,height=600)

        title1 = Label(frame, text="Sign Up", font=("times new roman",25,"bold"),bg="white").place(x=170, y=10)
        fname1=StringVar()

        f_name = Label(frame, text="First name", font=("helvetica",15),bg="white").place(x=20, y=100)
        self.fname = Entry(frame,font=("arial"),bg="skyblue",textvariable=fname1)
        self.fname.place(x=20, y=130, width=200)

        lname1 = StringVar()
        l_name = Label(frame, text="Last name", font=("helvetica",15),bg="white").place(x=240, y=100)
        self.lname= Entry(frame,font=("arial"),bg="skyblue",textvariable=lname1)
        self.lname.place(x=240, y=130, width=200)

        username1= StringVar()
        username = Label(frame, text="Username", font=("helvetica",15),bg="white").place(x=20, y=180)
        self.username = Entry(frame,font=("arial"),bg="skyblue",textvariable=username1)
        self.username.place(x=20, y=210, width=420)

        email1=StringVar()
        email = Label(frame, text="Email", font=("helvetica",15),bg="white").place(x=20, y=260)
        self.email = Entry(frame,font=("arial"),bg="skyblue",textvariable=email1)
        self.email.place(x=20, y=290, width=420)

        password =  Label(frame, text="Password", font=("helvetica",15),bg="white").place(x=20, y=340)
        password1=StringVar()
        self.password= Entry(frame,font=("arial"),bg="skyblue",textvariable=password1)
        self.password.place(x=20, y=370, width=420)

        self.terms = IntVar()
        terms_and_con = Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.terms,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=20,y=420)
        self.signup = Button(frame,text="Sign Up",command=self.signup_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="grey50",fg="white").place(x=120,y=470,width=250)

    #BACKEND
    def signup_func(self):
        if self.fname.get()=="" and self.lname.get()=="" and self.username.get()=="" and self.email.get()==""  and self.password.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
   
        elif self.terms.get() == 0:
            messagebox.showerror("Error!","Please Agree with our Terms & Conditions",parent=self.window)

        else:
            connection=cx_Oracle.connect('ems/abhinav')
            cur=connection.cursor()
            row=cur.execute("select * from register")
            for i in row:
                if self.email.get()==i[3]:
                    messagebox.showerror("Error","The email id is already exists,please try again with another email id",parent=self.window)
                else:
                        print('data insert')
            f=self.fname.get()
            l=self.lname.get()
            u=self.username.get()
            e=self.email.get()                                     
            p=self.password.get()
            cur.execute("insert into register values(:fn,:ln,:us,:em,:pa)",{":fn":f,":ln":l,":us":u,":em":e,":pa":p})
            cur.close()
            connection.commit()
            connection.close()
            messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
            self.reset_fields()

    def reset_fields(self):
        self.fname.delete(0, END)
        self.lname.delete(0, END)
        self.username.delete(0, END)
        self.email.delete(0, END)
        self.password.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()