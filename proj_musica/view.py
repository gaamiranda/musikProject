import tkinter as tk
from tkinter import FLAT, Button, Canvas, Entry, Frame, Image, Label, messagebox
from model.musica import *
from PIL import Image, ImageTk
from model.users import *


class View:
    def __init__(self, master):
        self.master = master
        self.users = LinkedListUsers()
        self.master.geometry('800x800')
        self.master.resizable(False, False)
        self.master.title('Login')

        #Frame
        self.frame = tk.Frame(self.master, width=800, height=800, bg='white')
        self.frame.pack()

        #Janela Login
        self.login_janela = tk.Frame(self.master, bg='black', width='800', height='800')
        self.login_janela.place(x=0, y=0)

        self.linhacima = Image.open("linhacima.png")
        self.linhacima = self.linhacima.resize((800, 100)) #LANCZOS
        self.linhacima = ImageTk.PhotoImage(self.linhacima)
        self.linhacima_label = tk.Label(self.login_janela, image=self.linhacima, bg='#040405')
        self.linhacima_label.place(x=0, y=0)

        self.linhabaixo = Image.open("linhabaixo.png")
        self.linhabaixo = self.linhabaixo.resize((800, 100)) #LANCZOS
        self.linhabaixo = ImageTk.PhotoImage(self.linhabaixo)
        self.linhabaixo_label = tk.Label(self.login_janela, image=self.linhabaixo, bg='#040405')
        self.linhabaixo_label.place(x=0, y=700)



        self.logo_bv = Image.open("bemvindo.png")
        self.logo_bv = self.logo_bv.resize((300, 100)) #LANCZOS
        self.logo_bv = ImageTk.PhotoImage(self.logo_bv)
        self.logo_bv_label = tk.Label(self.login_janela, image=self.logo_bv, bg='#040405')
        self.logo_bv_label.place(x=80, y=150)

        #Login
        self.sign_label = tk.Label (self.login_janela, text="Sign In", bg='#040405', fg='white', font=('Arial', 13, 'bold'))
        self.sign_label.place(x=640, y=370)

        self.logo = Image.open("SpotUal.png")
        self.logo = self.logo.resize((300, 300)) #LANCZOS
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = tk.Label(self.login_janela, image=self.logo, bg='#040405')
        self.logo_label.place(x=70, y=330)

        self.logo_user = Image.open("iconuser.png")
        self.logo_user = self.logo_user.resize((80, 80)) #LANCZOS
        self.logo_user = ImageTk.PhotoImage(self.logo_user)
        self.logo_user_label = tk.Label(self.login_janela, image=self.logo_user, bg='#040405')
        self.logo_user_label.place(x=630, y=270)


        #Username
        self.username_label = tk.Label(self.login_janela, text='Username', relief= 'flat', bg='#040405', fg="#6b6a69", font=('Arial', 13, 'bold'))
        self.username_label.place(x=550, y=420)
        self.username_nome = tk.Entry(self.login_janela, highlightthickness=0, relief='flat', bg='#040405', fg='#6b6a69', font=('Arial', 12, 'bold'))
        self.username_nome.place(x=580, y=456)
        self.linha = tk.Canvas(self.login_janela, width=230, height=2.0, bg='white', highlightthickness=0)
        self.linha.place(x=550, y=480)

        #Passsword
        self.password_label = tk.Label(self.login_janela, text='Password', relief= 'flat', bg='#040405', fg="#6b6a69", font=('Arial', 13, 'bold'))
        self.password_label.place(x=550, y=500)
        self.password_pw = tk.Entry(self.login_janela, highlightthickness=0, relief='flat', bg='#040405', fg='#6b6a69', font=('Arial', 12, 'bold'), )
        self.password_pw.place(x=580, y=536, width=190)
        self.linha_pw = tk.Canvas(self.login_janela, width=230, height=2.0, bg='white', highlightthickness=0)
        self.linha_pw.place(x=550, y=560)

        #Botao Login
        self.login_button = tk.Button(self.login_janela, text="LOGIN", font=('Arial', 12, 'bold'), width=23, bd=0, bg="#0F5B37", cursor="hand2", activebackground="#0F5B37", fg="white", command= lambda: self.login(self.username_nome.get(), self.password_pw.get()))
        self.login_button.place(x=550, y=600)

        #registar password
        self.sign_button = tk.Button(self.login_janela, text="REGISTAR", font=('Arial', 12, 'bold'), width=23, bd=0, bg="#0F5B37", cursor="hand2", 
                                    activebackground="#0F5B37", fg="white", command=self.registar)
        self.sign_button.place(x=550, y=640)

    def registar(self):
            self.frame.destroy()
            tela = tk.Toplevel(self.master)
            tela.title("Registo")
            tela.configure(background="#ffe76c")
            frame = tk.Frame(tela, bg = "#ffe76c")
            frame.pack()

            self.lc = Image.open("linhacima.png")
            self.lc = self.lc.resize((800, 100)) #LANCZOS
            self.linhacima = ImageTk.PhotoImage(self.linhacima)
            self.linhacima_label = tk.Label(self.login_janela, image=self.linhacima, bg='#040405')
            self.linhacima_label.place(x=0, y=0)

            nome_label = tk.Label(frame, text="Username:", font=('Arial', 14), bg='#ffe76c')
            nome_label.pack(pady=100)
            nome_entry = tk.Entry(frame, font=('Arial', 14))
            nome_entry.pack(pady=15)
            
            password_label = tk.Label(frame, text="Password:", font=('Arial', 14), bg='#ffe76c')
            password_label.pack()
            password_entry = tk.Entry(frame, show="*", font=('Arial', 14))
            password_entry.pack(pady=5)

            password_confirmar_label = tk.Label(frame, text="Confirmar Password:", font=('Arial', 14), bg='#ffe76c')
            password_confirmar_label.pack()
            password_confirmar_entry = tk.Entry(frame, show="*", font=('Arial', 14))
            password_confirmar_entry.pack(pady=5)

            registar_button = tk.Button(frame, text="Registar", font=('Arial', 14),fg='white', bg='#6d7575', command= lambda: self.users.add_user(nome_entry.get(), password_entry.get(), password_confirmar_entry.get()))
            registar_button.pack(pady=10, ipadx=20, ipady=5)
            

    def login(self, nome, password):
        temp = self.users.head
        while temp:
            if temp.nome == nome and temp.password == password:
                messagebox.showinfo("Login", "Login efetuado com sucesso!")
                break
            else:
                temp = temp.next
        if temp == None:
            messagebox.showerror("Erro", "Utilizador ou password erradas!")
            return
        self.master.destroy()
        #pagina principal