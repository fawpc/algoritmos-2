from no import No
class Pilha:
	def __init__(self):
		self.inicio = None
		self.fim =None
		self.tamanho = 0

	def adicionar(self, valor):
		no = No(valor)
		if self.tamanho == 0:
			self.inicio = no
			self.fim = no	
		else:
			aux = self.inicio
			self.inicio	= no
			self.inicio.proximo = aux
		self.tamanho +=1	

	def imprimir(self):
		texto = "";
		if self.tamanho == 0:
			texto = "Fila vazia"
		else:
			aux = self.inicio
			while(aux):
				texto = texto + str(aux.dado) + " - "
				aux = aux.proximo
		print(texto)
		
	def remover(self):
		if self.tamanho == 0:
			print("Fila vazia")	
		elif self.tamanho == 1:
			self.inicio = None
			self.fim = None
			self.tamanho -=1
		else:
			self.inicio = self.inicio.proximo
			self.tamanho -=1		