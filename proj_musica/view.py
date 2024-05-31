import tkinter as tk
import customtkinter as ctk 
from tkinter import *
from tkinter.ttk import Progressbar
from model.musica import *
from PIL import Image, ImageTk
from model.users import *
from model.database import *
from model.spotify import *




class View:
    def __init__(self, master):
        self.master = master
        self.database = DataBase()
        self.users = LinkedListUsers()
        img = PhotoImage(file= "SpotUal.png")
        self.master.iconphoto(False, img)
        self.master.geometry('800x800')
        self.master.resizable(False, False)
        self.master.title('Login')
        self.load_clients()
        self.playlist = LinkedListMusica()
        self.musicas_iniciais = LinkedListFila()
        self.init_music()

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



        self.logo_bv = Image.open("emvindo.png")
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
        self.password_pw = tk.Entry(self.login_janela, highlightthickness=0, relief='flat', bg='#040405', fg='#6b6a69', font=('Arial', 12, 'bold'), show="*" )
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

            nome_label = tk.Label(frame, text="Username:", font=('Arial', 14), bg='#ffe76c')
            nome_label.pack()
            nome_entry = tk.Entry(frame, font=('Arial', 14))
            nome_entry.pack(pady=5)
            
            password_label = tk.Label(frame, text="Password:", font=('Arial', 14), bg='#ffe76c')
            password_label.pack()
            password_entry = tk.Entry(frame, show="*", font=('Arial', 14))
            password_entry.pack(pady=5)

            password_confirmar_label = tk.Label(frame, text="Confirmar Password:", font=('Arial', 14), bg='#ffe76c')
            password_confirmar_label.pack()
            password_confirmar_entry = tk.Entry(frame, show="*", font=('Arial', 14))
            password_confirmar_entry.pack(pady=5)

            registar_button = tk.Button(frame, text="Registar", font=('Arial', 14),fg='white', bg='#6d7575', command= lambda: self.users.add_user(nome_entry.get(), password_entry.get(), password_confirmar_entry.get(), self.database, 0))
            registar_button.pack(pady=10, ipadx=20, ipady=5)
            

    def login(self, nome, password):
        if nome == "admin" and password == "admin":
            self.login_admin()
        else:
            temp = self.users.head
            while temp:
                if temp.nome == nome and temp.password == password:
                    messagebox.showinfo("Login", "Login efetuado com sucesso!")
                    self.master.withdraw()
                    break
                else:
                    temp = temp.next
            if temp == None:
                messagebox.showerror("Erro", "Utilizador ou password erradas!")
                return
            #pagina principal
            janela_princiapl = tk.Toplevel(self.master)
            janela_princiapl.title("SpotUal")
            janela_princiapl.geometry("600x500")
            img = PhotoImage(file= "icon.png")
            janela_princiapl.iconphoto(False, img)
            janela_princiapl.protocol("WM_DELETE_WINDOW", self.master.destroy)

            list_box = tk.Listbox(janela_princiapl, width= 50, font=("Arial", 16, "bold"))
            list_box.pack(pady=10)
            list_box.insert(tk.END, "Cantona", "Diamonds","We Found Love", "Gangstanismo","Alô", "Biggie Biggie Biggie","Habibi", "Como é que Tamos","Umbrella", "Erika")
            
            

            botao_frame = tk.Frame(janela_princiapl)
            botao_frame.pack(pady=20)
            botao_tras = ctk.CTkButton(botao_frame, text="<", width = 50, font= ("Arial", 18, "bold"), fg_color="#0F5B37", hover_color="#0F5B37", cursor="hand2", text_color="white", command=lambda: self.musicas_iniciais.prev_song(list_box))
            botao_tras.pack(side=tk.LEFT, padx= 5)
            botao_play = ctk.CTkButton(botao_frame, text="▶", width = 50, font=("Arial", 18, "bold"), fg_color="#0F5B37", hover_color="#0F5B37", cursor="hand2", text_color="white", command=lambda: self.musicas_iniciais.play_song(list_box.curselection(), list_box))
            botao_play.pack(side=tk.LEFT, padx= 5)
            botao_pausa = ctk.CTkButton(botao_frame, text="⏸️", width = 50, font=("Arial", 18, "bold"), fg_color="#0F5B37", hover_color="#0F5B37", cursor="hand2", text_color="white", command=lambda: self.musicas_iniciais.pause_song())
            botao_pausa.pack(side=tk.LEFT, padx= 5)
            botao_next = ctk.CTkButton(botao_frame, text=">", width= 50, font=("Arial", 18, "bold"), fg_color="#0F5B37", hover_color="#0F5B37", cursor="hand2", text_color="white", command=lambda: self.musicas_iniciais.next_song(list_box))
            botao_next.pack(side=tk.LEFT, padx=5)
            botao_adicionar = ctk.CTkButton(botao_frame, text="🎧", width=50, font=("Arial", 18, "bold"),fg_color="#0F5B37", hover_color="#0F5B37", cursor="hand2", text_color="white", command=lambda: self.add_to_playlist(list_box.curselection(), list_box))
            botao_adicionar.pack(side=tk.LEFT, padx=5)

            pesquisa_frame = tk.Frame(janela_princiapl)
            pesquisa_frame.pack(pady=5)
            barra_pesquisa = ctk.CTkEntry(pesquisa_frame, width=200, font= ("Arial", 18, "bold"))
            barra_pesquisa.pack(side=ctk.LEFT, padx=5)
            botao_lupa = ctk.CTkButton(pesquisa_frame, text="🔎", width= 40, font=("Arial", 18, "bold"), fg_color="#0F5B37", hover_color="#0F5B37", cursor="hand2", text_color="white", command=lambda: self.search_song(barra_pesquisa.get(), list_box))
            botao_lupa.pack(side=tk.LEFT, padx=5)
            nomes_frame = tk.Frame(janela_princiapl)
            nomes_frame.pack(pady=5)
            botao_dillaz = ctk.CTkButton(nomes_frame, text="Dillaz", width = 50, font= ("Arial", 18, "bold"), fg_color="#0F5B37", hover_color="#0F5B37", cursor="hand2", text_color="white", command=lambda: self.artist(list_box, "Dillaz"))
            botao_dillaz.pack(side=tk.LEFT, padx=5)
            botao_Rihanna = ctk.CTkButton(nomes_frame, text="Rihanna", width = 50, font= ("Arial", 18, "bold"), fg_color="#0F5B37", hover_color="#0F5B37", cursor="hand2", text_color="white", command=lambda: self.artist(list_box, "Rihanna"))
            botao_Rihanna.pack(side=tk.LEFT, padx=5)
            botao_kingbigs = ctk.CTkButton(nomes_frame, text="King Bigs", width = 50, font= ("Arial", 18, "bold"), fg_color="#0F5B37", hover_color="#0F5B37", cursor="hand2", text_color="white", command=lambda: self.artist(list_box, "King Bigs"))
            botao_kingbigs.pack(side=tk.LEFT, padx=5)
            botao_other = ctk.CTkButton(nomes_frame, text="Other", width = 50, font= ("Arial", 18, "bold"), fg_color="#0F5B37", hover_color="#0F5B37", cursor="hand2", text_color="white", command=lambda: self.artist(list_box, "Other"))
            botao_other.pack(side=tk.LEFT, padx=5)
            botao_reset = ctk.CTkButton(nomes_frame, text="Reset", width = 50, font= ("Arial", 18, "bold"), fg_color="#0F5B37", hover_color="#0F5B37", cursor="hand2", text_color="white", command=lambda: self.reset(list_box))
            botao_reset.pack(side=tk.LEFT, padx=5)

            botao_playlist = ctk.CTkButton(janela_princiapl, text="Playlist 1", width=50, font=("Arial", 18, "bold"),fg_color="#0F5B37", 
                                        hover_color="#0F5B37", cursor="hand2", text_color="white", command=self.janela_playlist)
            botao_playlist.pack(side=tk.LEFT, padx=5)
            
        
    
    def load_clients(self):
        for nome, password in self.database.fetch_clientes():
            self.users.add_user(nome, password, password, self.database, 1)
    
    def delete_database(self):
        for nome, passwd in self.database.fetch_clientes():
            if nome != "admin":
                self.database.delete_cliente(nome)
    
    def login_admin(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("Admin Panel")
        new_window.geometry('300x200')
        self.destryo = tk.Button(new_window, text="Destroy DATABASE", font=('Arial', 12, 'bold'), width=23, bd=0, bg="#0F5B37", cursor="hand2", 
                                    activebackground="#0F5B37", fg="white", command=self.delete_database)
        self.destryo.pack()
    
    def janela_playlist(self):
        jani = tk.Toplevel(self.master)
        jani.title("Playlist 1")
        jani.geometry('300x200')

        jani.grid_rowconfigure(0, weight=1)
        jani.grid_rowconfigure(1, weight=0)
        jani.grid_columnconfigure(0, weight=1)

        list_box = tk.Listbox(jani, width=50, font=("Arial", 16, "bold"))
        list_box.grid(row=0, column=0, pady=10, sticky='nsew')
        
        for song in self.playlist.get_songs():
            list_box.insert(tk.END, song)
        
        botao_playlist = ctk.CTkButton(jani, text="❌", width=50, font=("Arial", 18, "bold"),
                                    fg_color="#0F5B37", hover_color="#0F5B37", cursor="hand2", text_color="white", command=lambda: self.remove_from_playlist(list_box.curselection(), list_box))
        botao_playlist.grid(row=1, column=0, pady=10, padx=5, sticky='e')

    def init_music(self):
        self.musicas_iniciais.init_songs()
    
    def add_to_playlist(self, selected, list_box):
        if selected:
            self.playlist.add_song(list_box.get(selected[0]))
        
    def remove_from_playlist(self, selected, list_box):
        if selected:
            self.playlist.remove_song(list_box.get(selected[0]))
            list_box.delete(0, tk.END)
            for song in self.playlist.get_songs():
                list_box.insert(tk.END, song)
            messagebox.showinfo("Sucesso", "Música removida com sucesso")
    
    def search_song(self, song, list_box):
        if song not in musicas:
            messagebox.showerror("Erro", "Música não encontrada")
            return
        list_box.delete(0, tk.END)
        list_box.insert(tk.END, song)
        
    def reset(self, list_box):
        list_box.delete(0, tk.END)
        for musica in musicas:
            list_box.insert(tk.END, musica)

    def artist(self, list_box, artista):
        list_box.delete(0, tk.END)
        if artista == "Dillaz":
            list_box.insert(tk.END, "Cantona", "Alô", "Habibi")
        elif artista == "Rihanna":
            list_box.insert(tk.END, "Diamonds", "We Found Love", "Umbrella")
        elif artista == "King Bigs":
            list_box.insert(tk.END, "Gangstanismo", "Biggie Biggie Biggie", "Como é que Tamos")
        else:
            list_box.insert(tk.END, "Erika")