import tkinter as tk
import tkinter
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

    
        self.logo = Image.open("SpotUal.png")
        self.logo = self.logo.resize((300, 300)) #LANCZOS
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = tk.Label(self.login_janela, image=self.logo, bg='#040405')
        self.logo_label.place(x=70, y=330)

        #Login
        self.sign_label = tk.Label (self.login_janela, text="Sign In", bg='#040405', fg='white', font=('Arial', 13, 'bold'))
        self.sign_label.place(x=610, y=260)
        self.logo_user = Image.open("iconuser.png")
        self.logo_user = self.logo_user.resize((80, 80)) #LANCZOS
        self.logo_user = ImageTk.PhotoImage(self.logo_user)
        self.logo_user_label = tk.Label(self.login_janela, image=self.logo_user, bg='#040405')
        self.logo_user_label.place(x=600, y=160)


        #Username
        self.username_label = tk.Label(self.login_janela, text='Username', relief= 'flat', bg='#040405', fg="#6b6a69", font=('Arial', 13, 'bold'))
        self.username_label.place(x=530, y=320)
        self.username_nome = tk.Entry(self.login_janela, highlightthickness=0, relief='flat', bg='#040405', fg='#6b6a69', font=('Arial', 12, 'bold'))
        self.username_nome.place(x=560, y=356)
        self.linha = tk.Canvas(self.login_janela, width=230, height=2.0, bg='white', highlightthickness=0)
        self.linha.place(x=530, y=380)

        #Passsword
        self.password_label = tk.Label(self.login_janela, text='Password', relief= 'flat', bg='#040405', fg="#6b6a69", font=('Arial', 13, 'bold'))
        self.password_label.place(x=530, y=400)
        self.password_pw = tk.Entry(self.login_janela, highlightthickness=0, relief='flat', bg='#040405', fg='#6b6a69', font=('Arial', 12, 'bold'), show="*" )
        self.password_pw.place(x=560, y=436, width=190)
        self.linha_pw = tk.Canvas(self.login_janela, width=230, height=2.0, bg='white', highlightthickness=0)
        self.linha_pw.place(x=530, y=460)
        self.show_password_var = tk.BooleanVar()
        self.show_password_var.set(False)
        self.check_button = tk.Checkbutton(self.login_janela, text="Mostrar Password", relief= 'flat', bg='#040405', fg="#6b6a69", activeforeground="#6b6a69", activebackground="black", background="black",font=('Arial', 13, 'bold'), variable=self.show_password_var, command=self.show_password)
        self.check_button.place(x=530, y=480)


        #Botao Login
        self.login_button = tk.Button(self.login_janela, text="LOGIN", font=('Arial', 12, 'bold'), width=23, bd=0, bg="#0F5B37", cursor="hand2", activebackground="#0F5B37", fg="white", command= lambda: self.login(self.username_nome.get(), self.password_pw.get()))
        self.login_button.place(x=530, y=530)

        #registar password
        self.sign_button = tk.Button(self.login_janela, text="REGISTAR", font=('Arial', 12, 'bold'), width=23, bd=0, bg="#0F5B37", cursor="hand2", 
                                    activebackground="#0F5B37", fg="white", command=self.registar)
        self.sign_button.place(x=530, y=570)

    def show_password(self):
        if self.show_password_var.get():
            self.password_pw.config(show="")
        else:
            self.password_pw.config(show="*")

    def registar(self):
            self.frame.destroy()
            tela = tk.Toplevel(self.master)
            tela.title("Registo")
            tela.resizable(False, False)
            tela.geometry("500x500")
            tela.configure(background="#2B2B2B")
            frame = tk.Frame(tela, width=500, height=500)
            frame.pack()

            imagem_pil = Image.open("egistar.png")  # Substitua pelo caminho da sua imagem
            imagem = ImageTk.PhotoImage(imagem_pil)
            imagem_label = tk.Label(frame, image=imagem)
            imagem_label.image = imagem  # Manter uma referência para a imagem
            imagem_label.pack(pady=0)

            frame2 = ctk.CTkFrame(imagem_label, width=320, height=360, corner_radius= 15, bg_color="#2B2B2B")
            frame2.place(relx= 0.5, rely=0.5, anchor=tkinter.CENTER)

            registar = ctk.CTkLabel(frame2, width= 220, text= "Criar Conta", font=('Century Gothic', 20))
            registar.place(x=50, y=45)

            nome_entry = ctk.CTkEntry(frame2, width=220, placeholder_text="Username")
            nome_entry.place(x=50, y=110)

            password_entry = ctk.CTkEntry(frame2, width=220, placeholder_text="Password", show="*")
            password_entry.place(x=50, y=165)

            password_confirmar_entry = ctk.CTkEntry(frame2, width=220, placeholder_text="Confirmar Password", show="*")
            password_confirmar_entry.place(x=50, y=220)

            show_password_var = tk.BooleanVar()
            show_password_var.set(False)
            check_button = ctk.CTkCheckBox(frame2, width= 80, text="Mostrar Password", font=('Arial', 13, 'bold'))
            check_button.place(x=50, y=260)

            registar_button = ctk.CTkButton(frame2, width= 220, text="Registar", font=('Arial', 14), fg_color="#0F5B37", hover_color="#0F5B37", corner_radius=15,
                                            command= lambda: self.users.add_user(nome_entry.get(), password_entry.get(), 
                                            password_confirmar_entry.get(), self.database, 0))
            registar_button.place(x=50, y=300)
            
        

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