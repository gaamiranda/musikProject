import tkinter as tk
from tkinter import FLAT, Button, Canvas, Entry, Frame, Image, Label, messagebox
from model.musica import *
from model.users import *


class View:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1166x718')
        self.master.resizable(False, False)
        self.master.title('Login')

        #Frame
        self.frame = tk.Frame(self.master, width=1166, height=718, bg='white')
        self.frame.pack()

        #Janela Login
        self.login_janela = tk.Frame(self.master, bg='#040405', width='800', height='600')
        self.login_janela.place(x=200, y=70)

        self.txt = "Bem-Vindo"
        self.head = tk.Label(self.login_janela, text=self.txt, fg="white", bg="#040405", font=('Arial', 13, 'bold'))
        self.head.place(x=80, y=30, width=300, height=30)

        #Login
        self.sign_label = tk.Label (self.login_janela, text="Sign In", bg='#040405', fg='white', font=('Arial', 13, 'bold'))
        self.sign_label.place(x=650, y=240)

        #Username
        self.username_label = tk.Label(self.login_janela, text='Username', relief= 'flat', bg='#040405', fg="#6b6a69", font=('Arial', 13, 'bold'))
        self.username_label.place(x=550, y=300)
        self.username_nome = tk.Entry(self.login_janela, highlightthickness=0, relief='flat', bg='#040405', fg='#6b6a69', font=('Arial', 12, 'bold'))
        self.username_nome.place(x=580, y=335)
        self.linha = tk.Canvas(self.login_janela, width=230, height=2.0, bg='white', highlightthickness=0)
        self.linha.place(x=550, y=359)

        #Passsword
        self.password_label = tk.Label(self.login_janela, text='Password', relief= 'flat', bg='#040405', fg="#6b6a69", font=('Arial', 13, 'bold'))
        self.password_label.place(x=550, y=380)
        self.password_pw = tk.Entry(self.login_janela, highlightthickness=0, relief='flat', bg='#040405', fg='#6b6a69', font=('Arial', 12, 'bold'), )
        self.password_pw.place(x=580, y=416, width=190)
        self.linha_pw = tk.Canvas(self.login_janela, width=230, height=2.0, bg='white', highlightthickness=0)
        self.linha_pw.place(x=550, y=440)

        #Botao Login
        self.login_button = tk.Button(self.login_janela, text="LOGIN", font=('Arial', 12, 'bold'), width=23, bd=0, bg="green", cursor="hand2", activebackground="green", fg="white")
        self.login_button.place(x=550, y=470)

        #registar password
        self.sign_button = tk.Button(self.login_janela, text="REGISTAR", font=('Arial', 12, 'bold'), width=23, bd=0, bg="green", cursor="hand2", 
                                     activebackground="green", fg="white", command=self.registar)
        self.sign_button.place(x=550, y=510)

    def registar(self):
            self.frame.destroy()
            tela = tk.Toplevel(self.master)
            tela.title("Registo")
            tela.configure(background="#ffe76c")
            frame = tk.Frame(tela, bg = "#ffe76c")
            frame.pack()

            nome = tk.Label(frame, text="Username:", font=('Arial', 14), bg='#ffe76c')
            nome.pack()
            nome = tk.Entry(frame, font=('Arial', 14))
            nome.pack(pady=5)
                
            password = tk.Label(frame, text="Password:", font=('Arial', 14), bg='#ffe76c')
            password.pack()
            password = tk.Entry(frame, show="*", font=('Arial', 14))
            password.pack(pady=5)

            password_confirmar = tk.Label(frame, text="Confirmar Password:", font=('Arial', 14), bg='#ffe76c')
            password_confirmar .pack()
            password_confirmar  = tk.Entry(frame, show="*", font=('Arial', 14))
            password_confirmar .pack(pady=5)

            registar_button = tk.Button(frame, text="Registar", font=('Arial', 14),fg='white', bg='#6d7575',)
            registar_button.pack(pady=10, ipadx=20, ipady=5)


