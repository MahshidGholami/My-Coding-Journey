from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


# ----------------------------------------------------
def is_username_unique(username):
    with open('all_user.txt', 'r') as file:
        for line in file:
            username_unique,_= line.strip().split(':')
            if username_unique == username:
                return False
    return True


# -----------------------------------------------------

def Singin():
    windows = Tk()
    windows.title(' National Entrance Exam ')
    windows.geometry('800x600')
    windows.resizable(False, False)
    windows.iconbitmap('image/add-user.ico')
    windows_image = PhotoImage(file='image/background.png')
    image1 = Label(windows, i=windows_image)
    image1.image = windows_image
    image1.place(x=200, y=200)
    image1.pack()
    # -----------------------------singin-------------------------------
    text_sing_in = Label(windows, text='Sing in', bg='white', fg='black')
    text_sing_in.pack()
    text_sing_in.place(x=500, y=50)
    text_sing_in_style = ('Arial', 35, 'bold')
    text_sing_in.configure(font=text_sing_in_style)
    # -------------------------------------------------------------------
    Entry_sing_in = Label(windows, text='username', font=('calibre', 15, 'bold'), bg='white', fg='black')
    Entry_sing_in.pack()
    Entry_sing_in.place(x=450, y=170)
    Entry_sing_in = Entry(windows, width=25, font=('calibre', 15, 'bold'), fg='black', bg='LightBlue')
    Entry_sing_in.pack()
    Entry_sing_in.place(x=450, y=200)
    # -------------------------------------------------------------------------------------------------
    passEntry_sing_in = Label(windows, text='password', font=('calibre', 15, 'bold'), bg='white', fg='black')
    passEntry_sing_in.pack()
    passEntry_sing_in.place(x=450, y=250)
    passEntry_sing_in = Entry(windows, width=25, font=('calibre', 15, 'bold'), fg='black', bg='LightBlue', show="*")
    passEntry_sing_in.pack()
    passEntry_sing_in.place(x=450, y=280)
    # -------------------------------------------------------------------------------------------------
    emailEntry_sing_in = Label(windows, text='email', font=('calibre', 15, 'bold'), bg='white', fg='black')
    emailEntry_sing_in.pack()
    emailEntry_sing_in.place(x=450, y=330)
    emailEntry_sing_in = Entry(windows, width=25, font=('calibre', 15, 'bold'), fg='black', bg='LightBlue')
    emailEntry_sing_in.pack()
    emailEntry_sing_in.place(x=450, y=360)

    # --------------------------------------------------------------------------------------------------
    def singin():
        username = Entry_sing_in.get()
        password = passEntry_sing_in.get()
        if username=='' or password=='':
            messagebox.showerror('خطا','لطفا تمامی مقادیر را پر کنید')
        else:
            if not is_username_unique(username):
                messagebox.showerror('خطا',"این نام کاربری قبلاً ثبت شده است")
                return
            else:
                with open('all_user.txt', "a") as file:
                    file.write(f"{username}:{password}\n")
                    messagebox.showinfo('موفقیت'," کاربر با موفقیت ذخیره شد")

    botton_singin = Button(windows, text='sing in', font=('calibre', 15, 'bold'), bg='#3726d2', fg='black', width=20,
                           command=singin)
    botton_singin.pack()
    botton_singin.place(x=462, y=460)
    # -------------------------------------------------------------------------------------------------
    text_login_in = Label(windows, text='Log in', bg='#3726d2', fg='black')
    text_login_in.pack()
    text_login_in.place(x=120, y=50)
    text_login_in_style = ('Arial', 35, 'bold')
    text_login_in.configure(font=text_login_in_style)
    # -------------------------------------------------------------------
    Entry_login_in = Label(windows, text='username', font=('calibre', 15, 'bold'), bg='#3726d2', fg='black')
    Entry_login_in.pack()
    Entry_login_in.place(x=60, y=200)
    Entry_login_in = Entry(windows, width=25, font=('calibre', 15, 'bold'), fg='black', bg='LightBlue')
    Entry_login_in.pack()
    Entry_login_in.place(x=60, y=230)
    # -------------------------------------------------------------------------------------------------
    passEntry_login_in = Label(windows, text='password', font=('calibre', 15, 'bold'), bg='#3726d2', fg='black')
    passEntry_login_in.pack()
    passEntry_login_in.place(x=60, y=280)
    passEntry_login_in = Entry(windows, width=25, font=('calibre', 15, 'bold'), fg='black', bg='LightBlue', show="*")
    passEntry_login_in.pack()
    passEntry_login_in.place(x=60, y=310)

    # --------------------------------------------------------------------------------------------------
    def Login():
        username = Entry_login_in.get()
        password= passEntry_login_in.get()
        if username=='' or password=='':
            messagebox.showerror('خطا','لطفا تمامی مقادیر را پر کنید')
        else:
            try:
                with open('all_user.txt', 'r') as file:
                    for line in file:
                        stored_username, stored_password = line.strip().split(':')
                        if stored_username == username:
                            if stored_password == password:
                                messagebox.showinfo('ورود', "با موفقیت وارد شدید")
                                return
                            else:
                                messagebox.showerror('خطا', "رمز عبور نادرست است")
                                return
                    messagebox.showerror('خطا', "نام کاربری یافت نشد")
            except FileNotFoundError:
                messagebox.showerror('خطا', "هیچ کاربری ثبت نشده است")

    button_login = Button(windows, text='Log in', font=('calibre', 15, 'bold'), bg='white', fg='black', width=20,
                          command=Login)
    button_login.pack()
    button_login.place(x=60, y=460)
    windows.mainloop()


Singin()
# -----------------------------------------enddesing------------------------------------------------

