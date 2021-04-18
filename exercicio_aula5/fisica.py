from pessoa import Pessoa

class Fisica(Pessoa):
	def __init__(self, cod, nome, endereco, telefone, cpf, idade, peso, altura):
		Pessoa.__init__(self, cod, nome, endereco, telefone)
		self.__cpf = cpf
		self.idade = idade
		self.peso = peso
		self.altura = altura

	def calculoIMC(self, imc=0):
		self.imc = imc
		self.imc = self.peso / (self.altura*self.altura)

	def imprime(self):
		print("pessoa de cpf: ", self.__cpf, " e imc:", self.imc)