class Pessoa():	
	def __init__(self, cod, nome, endereco, telefone):
		self.__cod = cod
		self.nome = nome
		self._endereco = endereco
		self.__telefone = telefone

	def imprimir(self):
		print("cidadão de nome: ", self.nome, " e numero: ", self.__telefone)

		