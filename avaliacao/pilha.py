from no import No
class Pilha:
	def __init__(self):
		self.topo = None
		self.base =None
		self.tamanho = 0

	def adicionar(self, autor, titulo):
		no = No(autor, titulo)
		if self.tamanho == 0:
			self.topo = no
			self.base = no	
		else:
			aux = self.topo
			self.topo	= no
			self.topo.proximo = aux
		self.tamanho +=1	

	def imprimir(self):
		texto = "";
		if self.tamanho == 0:
			texto = "pliha de livros vazia"
		else:
			aux = self.topo
			while(aux):
				texto = texto +" autor: "+ str(aux.autor.nome) + " - " + " titulo: "+ str(aux.titulo)+"|"
				aux = aux.proximo
		print(texto)
		
	def remover(self):
		if self.tamanho == 0:
			print("pilha de livros vazia")	
		elif self.tamanho == 1:
			self.topo = None
			self.base = None
			self.tamanho -=1
		else:
			self.topo = self.topo.proximo
			self.tamanho -=1