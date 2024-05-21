import tkinter as tk
from tkinter import messagebox
from model.database import *


class NodeUser:
	def __init__(self, nome, password):
		self.nome = nome
		self.password = password
		self.next = None
	

class LinkedListUsers:
	def __init__(self):
		self.head = None
	
	def add_user(self, nome, password, passwordConfirmada, databasee, help):
		if len(nome) == 0:
			messagebox.showerror("Erro", "O nome não pode ser nulo!")
			return
		if len(password) == 0:
			messagebox.showerror("Erro", "A password não pode ser nula!")
			return
		if password != passwordConfirmada:
			messagebox.showerror("Erro", "As passwords não são iguais!")
			return
		if help == 0:
			if databasee.insert_cliente(nome, password):
				messagebox.showinfo("Registado", "Cliente registado com sucesso")
			else:
				messagebox.showerror("Erro", "Este nome de utilizador já está em uso")
		node = NodeUser(nome, password)
		temp = self.head
		if temp == None:
			self.head = node
		else:
			while temp.next:
				temp = temp.next
			temp.next = node
		#messagebox.showinfo("Registado", "Registado com sucesso!")
		#temp = self.head
	def check_user(self, nome):
		temp = self.head
		while temp:
			if temp.nome == nome:
				return True
			temp = temp.next
		return False