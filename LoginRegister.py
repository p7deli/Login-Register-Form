import tkinter as tk
from PIL import Image, ImageTk
from customtkinter import CTkLabel, CTkEntry, CTkButton, CTkCheckBox
from database_creat import Database
from tkinter import messagebox


class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry("800x500+300+80")
        self.resizable(False, False)
        self.config(bg="white")
        self.iconbitmap("icons/login .ico")

        # -------------------------------------------------------------------------
        self.dt = Database("database_fl.db")
        # -------------------------------------------------------------------------

        self.image_background = Image.open("pictures/background.jpg")
        self.image_background = self.image_background.resize((400, 400))
        self.photo_background = ImageTk.PhotoImage(self.image_background)
        tk.Label(self, image=self.photo_background, bg="white").place(x=10, y=20)
        # ----------------------------------------------------------------

        # ---------------------------------------------------------- Label Title
        self.lbl_title = tk.Label(self, text="Login Form", font=("Arial", 25, "bold"),
                                  fg="#2c77c7", bg="white")
        self.lbl_title.place(x=120, y=10)

        # ----------------------------------------------------------- Login
        self.frame_login = tk.Frame(self, width=380, height=470, bg="white")
        self.frame_login.place(x=410, y=10)

        self.img = Image.open("icons/user.png")
        self.img = self.img.resize((100, 100))
        self.ph = ImageTk.PhotoImage(self.img)
        tk.Label(self.frame_login, image=self.ph, bg="white").place(x=160, y=5)

        self.img_user = Image.open("icons/username.png")
        self.img_user = self.img_user.resize((20, 20))
        self.ph_user = ImageTk.PhotoImage(self.img_user)
        tk.Label(self.frame_login, image=self.ph_user, bg="white").place(x=80, y=150)
        CTkLabel(self.frame_login, text="________ UserName ________", font=("Arial", 15, "bold"), bg_color="white",
                 text_color="#2c77c7").place(x=110, y=150)
        self.txt_username = CTkEntry(self.frame_login, width=240, height=35, border_width=2, border_color="#2c77c7",
                                     font=("Arial", 20))
        self.txt_username.place(x=85, y=180)

        self.img_pass = Image.open("icons/password.png")
        self.img_pass = self.img_pass.resize((30, 30))
        self.ph_pass = ImageTk.PhotoImage(self.img_pass)
        tk.Label(self.frame_login, image=self.ph_pass, bg="white").place(x=75, y=220)
        CTkLabel(self.frame_login, text="________ PassWord ________", font=("Arial", 15, "bold"), bg_color="white",
                 text_color="#2c77c7").place(x=110, y=220)
        self.txt_password = CTkEntry(self.frame_login, width=240, height=35, border_width=2, border_color="#2c77c7",
                                     font=("Arial", 20), show="*")
        self.txt_password.place(x=85, y=255)

        self.show_hide_pass = CTkCheckBox(self.frame_login, text="SHOW", font=("Arial", 20, "bold"),
                                          text_color="#00558f", fg_color="#00558f",
                                          border_color="#00558f", command=self.show_hide)
        self.show_hide_pass.place(x=85, y=305)

        self.btn_login2 = CTkButton(self.frame_login, text="LOGIN", font=("Arial", 20, "bold"),
                                    fg_color="#2c77c7", border_width=3, border_color="#00558f",
                                    width=240, height=50, hover_color="#00558f",
                                    text_color="white", command=self.login_2)
        self.btn_login2.place(x=85, y=345)
        self.btn_register2 = CTkButton(self.frame_login, text="REGISTER", font=("Arial", 20, "bold"),
                                       fg_color="#28333b", border_width=3, border_color="black",
                                       width=240, height=50, hover_color="black",
                                       text_color="white", command=self.go_to_register)
        self.btn_register2.place(x=85, y=400)

        # ----------------------------------------------------------- Register
        self.frame_register = tk.Frame(self, width=380, height=470, bg="white")
        self.frame_register.place_forget()

        self.img1 = Image.open("icons/user.png")
        self.img1 = self.img.resize((100, 100))
        self.ph1 = ImageTk.PhotoImage(self.img1)
        tk.Label(self.frame_register, image=self.ph1, bg="white").place(x=135, y=5)

        tk.Label(self.frame_register, text="FirstName ...", font=("Arial", 15, "bold"), fg="#2c77c7",
                 bg="white").place(x=35, y=120)
        self.txt_firstname = CTkEntry(self.frame_register, width=180, height=35, font=("Arial", 20),
                                      border_color="#2c77c7")
        self.txt_firstname.place(x=5, y=150)

        tk.Label(self.frame_register, text="LastName ...", font=("Arial", 15, "bold"), fg="#2c77c7"
                 , bg="white").place(x=220, y=120)
        self.txt_lastname = CTkEntry(self.frame_register, width=180, height=35, font=("Arial", 20),
                                     border_color="#2c77c7")
        self.txt_lastname.place(x=190, y=150)

        self.img_user1 = Image.open("icons/username.png")
        self.img_user1 = self.img_user1.resize((20, 20))
        self.ph_user1 = ImageTk.PhotoImage(self.img_user1)
        tk.Label(self.frame_register, image=self.ph_user1, bg="white").place(x=5, y=185)
        CTkLabel(self.frame_register, text="_______________ UserName ________________", font=("Arial", 15, "bold"),
                 bg_color="white", text_color="#2c77c7").place(x=35, y=185)
        self.txt_username1 = CTkEntry(self.frame_register, width=365, height=35, border_width=2, border_color="#2c77c7",
                                      font=("Arial", 20))
        self.txt_username1.place(x=5, y=215)

        self.img_pass1 = Image.open("icons/password.png")
        self.img_pass1 = self.img_pass1.resize((30, 30))
        self.ph_pass1 = ImageTk.PhotoImage(self.img_pass1)
        tk.Label(self.frame_register, image=self.ph_pass1, bg="white").place(x=2, y=255)
        CTkLabel(self.frame_register, text="_______________ PassWord ________________", font=("Arial", 15, "bold"),
                 bg_color="white", text_color="#2c77c7").place(x=35, y=255)
        self.txt_password1 = CTkEntry(self.frame_register, width=365, height=35, border_width=2, border_color="#2c77c7",
                                      font=("Arial", 20), show="*")
        self.txt_password1.place(x=5, y=285)

        self.show_hide_pass1 = CTkCheckBox(self.frame_register, text="SHOW", font=("Arial", 20, "bold"),
                                           text_color="#00558f", fg_color="#00558f",
                                           border_color="#00558f", command=self.show_hide1)
        self.show_hide_pass1.place(x=5, y=325)

        self.btn_register1 = CTkButton(self.frame_register, text="REGISTER", font=("Arial", 20, "bold"),
                                       fg_color="#2c77c7", border_width=3, border_color="#00558f",
                                       width=365, height=50, hover_color="#00558f",
                                       text_color="white", command=self.register_)
        self.btn_register1.place(x=5, y=360)

        self.btn_login1 = CTkButton(self.frame_register, text="LOGIN", font=("Arial", 20, "bold"),
                                    fg_color="#28333b", border_width=3, border_color="black",
                                    width=365, height=50, hover_color="black",
                                    text_color="white", command=self.go_to_login)
        self.btn_login1.place(x=5, y=415)

    def go_to_register(self):
        self.frame_login.place_forget()
        self.frame_register.place(x=410, y=10)
        self.lbl_title.config(text="Register Form")
        self.lbl_title.place(x=100, y=10)
        self.title("Register")

    def go_to_login(self):
        self.frame_login.place(x=410, y=10)
        self.frame_register.place_forget()
        self.lbl_title.config(text="Login Form")
        self.lbl_title.place(x=120, y=10)
        self.title("Login")

    def show_hide(self):
        state = self.show_hide_pass.get()
        if state:
            self.show_hide_pass.configure(text="HIDE")
            self.txt_password.configure(show="")
        else:
            self.show_hide_pass.configure(text="SHOW")
            self.txt_password.configure(show="*")

    def show_hide1(self):
        state = self.show_hide_pass1.get()
        if state:
            self.show_hide_pass1.configure(text="HIDE")
            self.txt_password1.configure(show="")
        else:
            self.show_hide_pass1.configure(text="SHOW")
            self.txt_password1.configure(show="*")

    def login_2(self):
        username = self.txt_username.get()
        password = self.txt_password.get()
        self.dt.connect_db()
        self.dt.create_table()
        if username != "" and password != "":
            if not self.dt.check_user(username, password):
                messagebox.showinfo("Login", "Hello Welcome")
                self.dt.close_db()
                self.destroy()
            else:
                messagebox.showerror("Error", "Username and Password are not correct")
                self.dt.close_db()
                ques = messagebox.askyesno("Ques", "You don't have an account, if you want to create one?")
                if ques:
                    self.go_to_register()
                else:
                    self.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all the boxes")

    def register_(self):
        firstname = self.txt_firstname.get()
        lastname = self.txt_lastname.get()
        username = self.txt_username1.get()
        password = self.txt_password1.get()

        self.dt.connect_db()
        self.dt.create_table()
        if firstname != "" and lastname != "" and username != "" and password != "":
            if self.dt.create_user(firstname, lastname, username, password):
                self.dt.close_db()
                messagebox.showinfo("Register", f"Welcome to {username},"
                                                f" go to the login section to enter the program")
                self.go_to_login()
            else:
                messagebox.showerror("Error", "This username is already in use")
        else:
            messagebox.showerror("Error", "Please fill in all the boxes")


if __name__ == '__main__':
    app = LoginPage()
    app.mainloop()
