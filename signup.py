from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatched')
    elif check.get()==0:
        messagebox.showerror('Error', 'Please accept terms and conditions')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='root')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please try again')
            return

        try:
            Query='create database userdata1'
            mycursor.execute(Query)
            Query='use userdata1'
            mycursor.execute(Query)
            Query ='create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100), password varchar(20))'
            mycursor.execute(Query)
        except:
            mycursor.execute('use userdata1')

        Query='select * from data where username=%s'
        mycursor.execute(Query, (usernameEntry.get()))

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error', 'Username already Exist')

        else:
            Query='insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(Query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('success','Registration is Successful')
            clear()
            signup_window.destroy()
            import signin


def login_page():
    signup_window.destroy()
    import signin

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsft Yahei UI Light',18,'bold')
              ,bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Microsft Yahei UI Light',10,'bold'),bg='white',
                 fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Microsft Yahei UI Light',10,'bold'),bg='firebrick1',
                 fg='white')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('Microsft Yahei UI Light',10,'bold'),bg='white',
                 fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=30,font=('Microsft Yahei UI Light',10,'bold'),bg='firebrick1',
                 fg='white')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Microsft Yahei UI Light',10,'bold'),bg='white',
                 fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=30,font=('Microsft Yahei UI Light',10,'bold'),bg='firebrick1',
                 fg='white')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmLabel=Label(frame,text='Confirm Password',font=('Microsft Yahei UI Light',10,'bold'),bg='white',
                 fg='firebrick1')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmEntry=Entry(frame,width=30,font=('Microsft Yahei UI Light',10,'bold'),bg='firebrick1',
                 fg='white')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
termsandconditions=Checkbutton(frame,text='I agree to the Terms and Conditions',font=('Microsft Yahei UI Light',9,'bold'),
                               fg='firebrick1',bg='white',activeforeground='white',activebackground='firebrick1',
                               cursor='hand2',variable=check)
termsandconditions.grid(row=9,column=0,pady=10,padx=15)

signupButton=Button(frame,text='Signup',font=('Open Sans',16,'bold'),bd=0,bg='firebrick1',
                    fg='white',activeforeground='firebrick1',activebackground='white',width=17,command=connect_database)
signupButton.grid(rows=10,column=0,pady=10)

alreadyaccount=Label(frame,text='I have account',font=('Open Sans',9,'bold'),
                     bg='white',fg='firebrick1')
alreadyaccount.grid(row=24,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Log in',font=('Open Sans',9,'bold underline'),
                   fg='blue',bg='white',activeforeground='white'
                   ,activebackground='blue',cursor='hand2',bd=0,command=login_page)
loginButton.grid(row=24,column=0,pady=10)

signup_window.mainloop()
