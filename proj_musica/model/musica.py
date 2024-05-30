from tkinter import messagebox
from model.spotify import *

musicas = {"Cantona": "spotify:track:6mobne6wnkwLGDxF9T7D55", "Cinha": "spotify:track:2rUTqrOSkNZlBG7RnjaQSy", "Qualquer-Feira": "spotify:track:29QDgz4rRKiT2oB0hMgq8E", "Pé no Mar": "spotify:track:4hL6Jr0nOm5erNhCv7FpCT", "Alô": "spotify:track:6vBuEFImAx36hDYiYqBtkZ", "No Fumo No Trabajo (Skit)": "spotify:track:4o2HbQ4QQJqVvvtYfMP6JX", "Habibi": "spotify:track:31w82iq7jsYmPAsM8YChIy", "Hello": "spotify:track:1lkkQTw3ynEq47l42eVn9h", "Hennessy": "spotify:track:6f5Rg365HweagAIch5Tco6", "Direção Paris": "spotify:track:47vme38PigHgHq5YVEzUt8"}

class NodeMusica:
	def __init__(self, musica):
		self.musica = musica
		self.next = None

class NodeFila:
	def __init__(self, musica, musica_uri):
		self.musica = musica
		self.musica_uri = musica_uri
		self.next = None
		self.prev = None


class LinkedListFila:
	def __init__(self):
		self.head = None
		self.current = None
		self.stop = 0
	
	def add_song(self, musica):
		if musica in musicas:
			node = NodeFila(musica, musicas[musica])
		else:
			messagebox.showerror("Erro", "Música não existe!")
			return
		if self.head == None:
			self.head = node
		else:
			temp = self.head
			while temp.next:
				temp = temp.next
			temp.next = node
			node.prev = temp
	
	def init_songs(self):
		for musica in musicas:
			node = NodeFila(musica, musicas[musica])
			if self.head == None:
				self.head = node
				self.current = node
			else:
				temp = self.head
				while temp.next:
					temp = temp.next
				temp.next = node
				node.prev = temp
	
	def find_node(self, uri):
		temp = self.head
		while temp:
			if temp.musica_uri == uri:
				return temp
			temp = temp.next
	
	def get_current_song(self, musica):
		temp = self.head
		while temp:
			if temp.musica == musica:
				return temp
			temp = temp.next
	
	def play_song(self, selected, list_box):
		if self.stop == 1:
			self.resume_song()
			return
		if selected:
			uri = musicas[list_box.get(selected[0])]
			spoti_play(uri)
			self.current = self.find_node(uri)

	def next_song(self):
		if self.current and self.current.next:
			spoti_play(self.current.next.musica_uri)
		self.current = self.current.next

	def prev_song(self):
		if self.current and self.current.prev:
			spoti_play(self.current.prev.musica_uri)
		self.current = self.current.prev

	def pause_song(self):
		spoti_pause()
		self.stop = 1
	
	def resume_song(self):
		spoti_resume()
		self.stop = 0



	def __str__(self):
		temp = self.head
		while temp.next:
			print(f"{temp.musica}", end="->")
			temp = temp.next
		print(f"{temp.musica}")
		while temp:
			print(f"{temp.musica}", end="<-")
			temp = temp.prev
		return ""

class LinkedListMusica:
	def __init__(self):
		self.head = None
		self.size = 0
	
	def is_empty(self):
		return self.size == 0
	
	def size(self):
		return self.size
	
	def add_song(self, musica):
		if musica not in musicas:
			messagebox.showerror("Erro", "Música não existe!")
			return
		if self.check_song(musica):
			messagebox.showerror("Erro", "Música já está na playlist")
			return
		node = NodeMusica(musica)
		if self.head == None:
			self.head = node
		else:
			last = self.get_last()
			last.next = node
		self.size += 1
		messagebox.showinfo("Sucesso", "Música adicionada com sucesso")

	def check_song(self, musica):
		temp = self.head
		while temp:
			if temp.musica == musica:
				return True
			temp = temp.next
		return False

	def remove_song(self, musica):
		if self.size == 0:
			messagebox.showerror("Erro", "Playlist está vazia")
			return
		temp = self.head
		temp1 = self.head
		if temp.musica == musica:
			self.head = temp.next
			self.size -= 1
			return
		while temp.next:
			temp1 = temp
			temp = temp.next
			if temp.musica == musica:
				temp1.next = temp.next
				temp.next = None
				self.size -= 1
				return

	def get_last(self):
		temp = self.head
		while temp.next:
			temp = temp.next
		return temp

	def get_songs(self):
		temp = self.head
		music = []
		while temp:
			music.append(temp.musica)
			temp = temp.next
		return music

	def __str__(self):
		temp = self.head
		while temp.next:
			print(f"{temp.musica}", end="->")
			temp = temp.next
		print(f"{temp.musica}")
		return f"size: {self.size}"
		