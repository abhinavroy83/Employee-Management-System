from tkinter import *
from tkinter import ttk, messagebox

# import os
import cx_Oracle
from signup import SignUp
from admin_page import admin_page
# import signup1
# import credentials as cr

class login_page:
    def __init__(self, root):
        self.window = root
        self.window.title("EMS") 
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")

        #==============================DESIGN PART===================================

        self.frame1 = Frame(self.window, bg="skyblue")
        self.frame1.place(x=0, y=0, width=450, relheight = 1)

        label1 = Label(self.frame1, text= "EMS", font=("times new roman", 40, "bold"), bg="skyblue" ,fg="red").place(x=100,y=300)
        label3 = Label(self.frame1, text= "Employee Management System", font=("times new roman", 13, "bold"),bg="skyblue" , fg="red").place(x=100,y=360)

        #=============Entry Field & Buttons============

        self.frame2 = Frame(self.window, bg = "gray90")
        self.frame2.place(x=450,y=0,relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=200,y=170,width=400,height=420)

        self.email_label = Label(self.frame3,text="Email", font=("helvetica",15),bg="white", fg="black").place(x=50,y=40)
        self.email_entry = Entry(self.frame3,font=("times new roman",15),bg="cadet blue2",fg="black")
        self.email_entry.place(x=50, y=80, width=300)

        self.password_label = Label(self.frame3,text="Password", font=("helvetica",15),bg="white", fg="black").place(x=50,y=120)
        self.password_entry = Entry(self.frame3,font=("times new roman",15,"bold"),bg="cadet blue2",fg="black",show="*")
        self.password_entry.place(x=50, y=160, width=300)

        #================Buttons===================
        self.login_button = Button(self.frame3,text="Sign in",command=self.login_func,font=("times new roman",15, "bold"),bd=0,cursor="hand2",bg="black",fg="white").place(x=50,y=220,width=300)
        self.create_button = Button(self.frame3,text="New To EMS?Sign Up",command=self.redirect_window,font=("times new roman",18,),bd=0,cursor="hand2",bg="white",fg="black").place(x=80,y=320,width=250)

#backend
    def login_func(self):
        flag=0
        if self.email_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Error!","All fields are required",parent=self.window)
        elif self.email_entry.get()!='' and self.password_entry.get()!='':
            connection=cx_Oracle.connect('ems/abhinav')
            cur = connection.cursor()
            cur.execute("select * from REGISTER ")
            row=cur.fetchall()
            for i in row:
                    if(self.email_entry.get()==i[3]) and (self.password_entry.get()==i[4]):
                        print('user has accessed the system ')
                        flag=1
                        break
        
            if(flag==1):
                print('user has accessed the system')
                self.redirect_dashboard()
            else:
                messagebox.showerror("ERROR","EMAIL AND PASSWORD INVALID")    
            
    def redirect_window(self):
        self.window.destroy()
        # Importing the signup window.
        # The page must be in the same directory
        root = Tk()
        obj = SignUp(root)
        root.mainloop()

    def redirect_dashboard(self):
        self.window.destroy()
        root=Tk()
        obj=admin_page(root)
        root.mainloop()

    def reset_fields(self):
        self.email_entry.delete(0,END)
        self.password_entry.delete(0,END)
# The main function
if __name__ == "__main__":
    root = Tk()
    obj = login_page(root)
    root.mainloop()