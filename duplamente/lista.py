from no import No
class Lista:
	def __init__(self):	
		self.inicio = None
		self.fim = None
		self.tamanho = 0

	def adicionar(self, valor):
		if self.inicio:
			aux = self.fim
			aux.proximo = No(valor)
			aux.proximo.anterior = aux
			self.fim = aux.proximo
			self.fim.proximo = None							
		else:
			self.inicio = No(valor)
			self.fim = self.inicio
		self.tamanho +=	1

	def adicionarNoinicio(self, valor):
		self.inicio.anterior = None
		if self.inicio:
			aux = self.inicio
			aux.anterior = No(valor)
			aux.anterior.proximo = aux
			self.inicio = aux.anterior
			self.inicio.anterior = None
		else:
			self.inicio = No(valor)
			self.fim = self.inicio				
		self.tamanho +=1	

	def imprimir(self):
		if (self.inicio == None):
			print("lista vazia")
		else:
			aux = self.inicio
			while (aux):
				print(str(aux.dado))
				aux = aux.proximo
			print('tamanho da lista: ', self.tamanho)

	def excluir(self, valor):
		if self.tamanho == 0:
			print("lista vazia!!")

		elif self.tamanho == 1:
			if self.inicio.dado == valor:
				self.inicio = None
				self.fim = None
				self.tamanho -= 1
			else:
				print("valor não encontrado")
		else:
			tamAnterior = self.tamanho
			if self.inicio.dado == valor:
				self.inicio = self.inicio.proximo
				self.inicio.anterior = None
				self.tamanho -= 1

			elif self.fim.dado == valor:
				self.fim = self.fim.anterior
				self.fim.proximo = None
				self.tamanho -= 1
			
			else:
				aju = self.inicio
				aux = self.inicio.proximo
				while(aux != None):
					if(aux.dado == valor):
						aux.proximo.anterior = aux
						aju.proximo = aux.proximo
						self.tamanho -= 1
					else:
						aju = aux
					aux = aux.proximo
			if tamAnterior == self.tamanho:
				print("valor", valor, "não encontrado")
		self.imprimir()

	def alterar(self, valor, novo):
		if self.tamanho == 0:
			print("lista vazia!!")

		elif self.tamanho == 1:
			if self.inicio.dado == valor:
				self.inicio = novo
			else:
				print("valor não encontrado")
		else:
			if self.inicio.dado ==valor:
				self.inicio.dado = novo
			else:
				anterior = self.inicio
				aux = self.inicio.proximo
				while(aux != None):
					if(aux.dado == valor):
						aux.dado = novo					
					else:	
						anterior = aux
					aux = aux.proximo
					if(aux == None):
						print("valor", valor, "valor não encontrado0")


		self.imprimir()

	def imprimirInverso(self):
		if(self.inicio == None):
			print("lista vazia")
		else:
			aux = self.fim
			while (aux):
				print(str(aux.dado))
				aux = aux.anterior
			print('tamanho da lista: ', self.tamanho)		