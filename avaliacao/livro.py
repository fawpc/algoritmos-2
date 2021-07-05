from pilha import Pilha
class Livro():
	def  __init__(self, autor, titulo, pilha = Pilha()):
		self.autor = autor
		self.titulo = titulo
		self.pilha = pilha

	def ad(self):
		self.pilha.adicionar(self.autor, self.titulo)
		self.pilha.imprimir()

	def exc(self):	
		self.pilha.remover()

	def show(self):
		self.pilha.imprimir()		
