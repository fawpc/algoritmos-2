from pessoa import Pessoa

class Juridica(Pessoa):
	def __init__(self, cod, nome, endereco, telefone, cnpj, insEstadual, qtdFuncionarios):
		Pessoa.__init__(self, cod, nome, endereco, telefone)
		self.__cnpj = cnpj
		self.__insEstadual = insEstadual
		self.qtdFuncionarios = qtdFuncionarios

	def imprimi(self):
		print("pessoa de cnpj: ", self.__cnpj)

	def notaFiscal(self, count):
		self.count = count
		self.count += 1
		print("nota Fiscal emitida", " nº da nota Fiscal: ", self.count, "cnpj: ", self.__cnpj)