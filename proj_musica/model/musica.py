class NodeMusica:
	def __init__(self, musica):
		self.musica = musica
		self.next = None

class NodeFila:
	def __init__(self, musica):
		self.musica = musica
		self.next = None
		self.prev = None


class LinkedListFila:
	def __init__(self):
		self.head = None
	
	def add_song(self, musica):
		node = NodeFila(musica)
		if self.head == None:
			self.head = node
		else:
			temp = self.head
			while temp.next:
				temp = temp.next
			temp.next = node
			node.prev = temp

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
		if self.check_song(musica):
			#raise Exception("Song already in playlist")
			return
			#aqui tem de se meter uma messagebox a dizer que a musica ja foi adicionada
		node = NodeMusica(musica)
		if self.head == None:
			self.head = node
		else:
			last = self.get_last()
			last.next = node
		self.size += 1

	def check_song(self, musica):
		temp = self.head
		while temp:
			if temp.musica == musica:
				return True
			temp = temp.next
		return False

	def remove_song(self, musica):
		if self.size == 0:
			return
			#messagebox a dizer que nao ha nada na playlist
		if self.check_song(musica) == False:
			return
			#messagebox a dizer que nao existe essa musica
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
	
	def __str__(self):
		temp = self.head
		while temp.next:
			print(f"{temp.musica}", end="->")
			temp = temp.next
		print(f"{temp.musica}")
		return f"size: {self.size}"
		