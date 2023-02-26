from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle
class admin_page:
    def __init__(self,root):
        self.window=root
# root = Tk()
        self.window.title("ADMIN CRUD")
        self.window.geometry("1920x1080+0+0")
        self.window.config(bg="white")
        self.window.state("zoomed")

        Fname = StringVar()
        Lname = StringVar()
        gender = StringVar()
        email = StringVar()
        contact = StringVar()
        doj = StringVar()
        Sal= StringVar()
        job= StringVar()
        add=StringVar()

# Entries Frame
        self.entries_frame = Frame(root, bg="#3d434a")
        self.entries_frame.pack(side=TOP, fill=X)
        self.title = Label(self.entries_frame, text="Employee Management System(Admin-Page)", font=("Calibri", 15, "bold"), bg="#3d434a", fg="white")
        self.title.grid(row=0, columns=2, padx=10, pady=15, sticky="w")

        self.lblName = Label(self.entries_frame, text="First name", font=("Calibri", 16), bg="#3d434a", fg="white")
        self.lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.Fname = Entry(self.entries_frame, textvariable=Fname, font=("Calibri", 16), width=30)
        self.Fname.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.lname = Label(self.entries_frame, text="Last Name", font=("Calibri", 16), bg="#3d434a", fg="white")
        self.lname.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.lname = Entry(self.entries_frame, textvariable=Lname, font=("Calibri", 16), width=30)
        self.lname.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        self.lblGender = Label(self.entries_frame, text="Gender", font=("Calibri", 16), bg="#3d434a", fg="white")
        self.lblGender.grid(row=1, column=4, padx=10, pady=10, sticky="w")
        self.lblGender = ttk.Combobox(self.entries_frame, font=("Calibri", 16), width=15, textvariable=gender, state="readonly")
        self.lblGender['values'] = ("Male","Female")
        self.lblGender.grid(row=1, column=5, padx=10, sticky="w")

        self.lblEmail = Label(self.entries_frame, text="Email", font=("Calibri", 16), bg="#3d434a", fg="white")
        self.lblEmail.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.lblEmail = Entry(self.entries_frame, textvariable=email, font=("Calibri", 16), width=30)
        self.lblEmail.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.lblContact = Label(self.entries_frame, text="Contact No", font=("Calibri", 16), bg="#3d434a", fg="white")
        self.lblContact.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.lblContact = Entry(self.entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
        self.lblContact.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        self.lbldoj = Label(self.entries_frame, text="D-O-J", font=("Calibri", 16), bg="#3d434a", fg="white")
        self.lbldoj.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.lblDoj = Entry(self.entries_frame, textvariable=doj, font=("Calibri", 16), width=30)
        self.lblDoj.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.lblSal = Label(self.entries_frame, text="Salary", font=("Calibri", 16), bg="#3d434a", fg="white")
        self.lblSal.grid(row=3, column=2, padx=10, pady=10, sticky="w")
        self.lblSal = Entry(self.entries_frame, textvariable=Sal, font=("Calibri", 16), width=30)
        self.lblSal.grid(row=3, column=3, padx=10, pady=10, sticky="w")


        self.lbljob = Label(self.entries_frame, text="Job", font=("Calibri", 16), bg="#3d434a", fg="white")
        self.lbljob.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.lbljob = ttk.Combobox(self.entries_frame, font=("Calibri", 16), width=29, textvariable=job, state="readonly")
        self.lbljob['values'] = ("Manager","Designer","Developer","Accountent","Salesman")
        self.lbljob.grid(row=4, column=1, padx=10, sticky="w")

        btn_frame = Frame(self.entries_frame, bg="#3d434a")
        btn_frame.grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky="w")
        self.btnAdd = Button(btn_frame,command=self.add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",bg="#16a085", bd=0).grid(row=0, column=0)
        self.btnEdit = Button(btn_frame,command=self.update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#2980b9",bd=0).grid(row=0, column=1, padx=10)
        self.btnDelete = Button(btn_frame,command=self.delete_employee ,text="Delete Details", width=15, font=("Calibri", 16, "bold"),fg="white", bg="#c0392b",bd=0).grid(row=0, column=2, padx=10)
        self.btnClear = Button(btn_frame,command=self.clearAll,  text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",bg="#f39c12",bd=0).grid(row=0, column=3, padx=10)
# Table Frame

        # scroll_x=Scrollbar(root,orient=HORIZONTAL)
        # scroll_y=Scrollbar(root,orient=VERTICAL)
        # scroll_x.pack(side=BOTTOM,fill=X)
        # scroll_y.pack(side=RIGHT,fill=Y)


    
        # scroll_x.config(command=self.tv.xview)
        # scroll_x.config(command=self.tv.yview)


        tree_frame = Frame(root, bg="#ecf0f1")
        tree_frame.place(x=0, y=330, width=1980, height=520)
        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Calibri', 18), rowheight=50)  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
        self.tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8,9), style="mystyle.Treeview")
        self.tv.heading("1", text="FName")
        self.tv.column("1", width=5)
        self.tv.heading("2", text="LName")
        self.tv.column("2", width=5)
        self.tv.heading("3", text="Gender")
        self.tv.column("3", width=5)
        self.tv.heading("4", text="Email")
        self.tv.column("4", width=7)
        self.tv.heading("5", text="Contact")
        self.tv.column("5", width=7)
        self.tv.heading("6", text="D-O-J")
        self.tv.column("6", width=3)
        self.tv.heading("7", text="Salary")
        self.tv.column("7", width=5)
        self.tv.heading("8", text="Job")
        self.tv.column("8", width=5)
        self.tv['show'] = 'headings'
        self.tv.bind("<ButtonRelease-1>",self.getData)
        self.tv.pack(fill=BOTH,expand=1) 
        self.fetch_data()


    def getData(self,event):
        cursor_row=self.tv.focus()
        data = self.tv.item(cursor_row)
        row = data["values"]
        self.Fname.set(row[1])
        self.lname.set(row[2])
        self.lblGender.set(row[3])
        self.lblEmail.set(row[4])
        self.lblContact.set(row[5])
        self.lbldoj.set(row[6])
        self.lblSal.set(row[7])
        self.lbljob.set(row[8])
     

    def dispalyAll(self):
        con=cx_Oracle.connect("ems/abhinav")
        cursor=con.cursor()
        cursor.execute("select Fname,lname,lblGender,lblEmail,lblContact,lbldoj,lblSal,lbljob from details")
        rows=cursor.fetchall()
        if(rows)!=0:
            self.tv.delete(*self.tv.get_children())
        # self.tv.delete(self.tv.get_children())
            for row in rows():
                self.tv.insert("", END, values=row)
            con.commit()
        con.close()

    def fetch_data(self):
            con=cx_Oracle.connect("EMS/abhinav")
            cursor=con.cursor()
            cursor.execute("select Fname,lname,lblGender,lblEmail,lblContact,lbldoj,lblSal,lbljob from details")
            rows=cursor.fetchall()
            if(rows)!=0:
                self.tv.delete(*self.tv.get_children())
                for row in rows:
                    self.tv.insert('',END,values=row)
                con.commit()    
            con.close()
    
    def add_employee(self):
        if self.Fname.get() == "" and self.lname.get() == "" and self.lblGender.get() == "" and self.lblEmail.get() == "" and self.lblContact.get() == "" and self.lblDoj.get() == "" and self.lblSal.get() and self.lbljob.get(1.0, END):
            messagebox.showerror("Erorr in Input", "Please Fill All the Details")
            
        else:
            connection=cx_Oracle.connect('ems/abhinav')
            cur=connection.cursor()
            f=self.Fname.get()
            l=self.lname.get()
            g=self.lblGender.get()
            e=self.lblEmail.get()
            c=self.lblContact.get()
            d=self.lblDoj.get()
            s=self.lblSal.get()
            j=self.lbljob.get()
            cur.execute("insert into DETAILS values('%s','%s','%s','%s','%s','%s','%s','%s')"%(f,l,g,e,c,d,s,j))
            # cur.close()
            connection.commit()
            self.fetch_data()
            connection.close()
            messagebox.showinfo("Success", "Record Inserted")
            self.dispalyAll
        self.clearAll()
        self.fetch_data()
        self.dispalyAll()   
    
    # def fetch_data(self)

    def update_employee(self):
        if self.Fname.get() == "" and self.lname.get() == "" and self.lblGender.get() == "" and self.lblEmail.get() == "" and self.lblContact.get() == "" and self.lblDoj.get() == "" and self.lblSal.get() and self.lbljob.get():
            messagebox.showerror("Erorr in Input", "Please Fill All the Details")
       
        else:
            connection=cx_Oracle.connect('ems/abhinav')
            cur=connection.cursor()
            f=self.Fname.get()
            l=self.lname.get()
            g=self.lblGender.get()
            e=self.lblEmail.get()
            c=self.lblContact.get()
            d=self.lblDoj.get()
            s=self.lblSal.get()
            j=self.lbljob.get()
            cur.execute("update DETAILS set Fname=:n,lname=:ln,lblGender=:gn,lblContact=:cn,lblDoj=:do,lblSal=:sl,lbljob=:jb where lblEmail=:eo",n=f,ln=l,gn=g,cn=c,do=d,sl=s,jb=j,eo=e)
            connection.commit()
            self.fetch_data()
            connection.close()
            messagebox.showinfo("Success", "Record update")
            self.dispalyAll
        self.clearAll()
        self.dispalyAll()


    def delete_employee(self):
         e=self.lblEmail.get()
         con=cx_Oracle.connect("EMS/abhinav")
         print(con.version)
         cur=con.cursor()
         cur.execute("DELETE FROM details WHERE lblEmail=:E",E=e)
         con.commit()
         self.fetch_data()
         con.close()
         messagebox.showinfo("SUCCESS","RECORD DELETED SUCCESSFULLY")



    def clearAll(self):
        self.lblName.set("")
        self.lname.set("")
        self.lblGender.set("")
        self.lblEmail.set("")
        self.lblContact.set("")
        self.lbldoj.set("")
        self.lblSal.set("")
        self.lbljob.set("")

if __name__=="__main__":
    root=Tk()
    obj=admin_page(root)
    root.mainloop()