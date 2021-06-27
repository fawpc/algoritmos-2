from torre import Torre
from estacionamento import Fila
class Apartamento(Torre, Fila):
	def __init__(self, id_torre, nome, endereco, id_ap, numero, proximo):
		self.id_torre = id_torre
		self.nome = nome
		self.endereco = endereco
		self.id_ap = id_ap
		self.numero = numero
		self.proximo = proximo

	def vaga(self, valor, fila=Fila()):
		self.valor = valor
		fila.adicionar(valor)
		fila.imprimir()

	def cadastrar(self):
		print("Apartamento cadastrado com sucesso")

	def imprimir(self):
		if self.valor>5:
			print("o Apartamento do condominio alvorada da torre: ",self.nome, " |localização: ", self.endereco, " |e identificação da torre: ", self.id_torre,
				" |com identificação: ", self.id_ap, " |numero: ", self.numero, " |vaga de estacionamento: ", "aguardando vaga", " |e proximo ap: ", self.proximo)
		else:	
			print("o Apartamento do condominio alvorada da torre: ",self.nome, " |localização: ", self.endereco, " |e identificação da torre: ", self.id_torre,
				" |com identificação: ", self.id_ap, " |numero: ", self.numero, " |vaga de estacionamento: ", self.valor, " |e proximo ap: ", self.proximo)	
		print("---------------------------------------------------")			