class NodeUser:
	def __init__(self, nome, password):
		self.nome = nome
		self.password = password
		self.next = None
	

class LinkedListUsers:
	def __init__(self):
		self.head = None
	
	def add_user(self, nome, password, passwordConfirmada):
		if self.check_user(nome):
			return
			#messagebox a dizer que ja existe o nome deste utilizador
		if password != passwordConfirmada:
			return
			#messagebox a dizer que as passwords nao coincidem
		node = NodeUser(nome, password)
		temp = self.head
		if temp == None:
			self.head = node
		else:
			while temp.next:
				temp = temp.next
			temp.next = node
		
	
	def check_user(self, nome):
		temp = self.head
		while temp:
			if temp.nome == nome:
				return True
			temp = temp.next
		return False