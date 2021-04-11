from automovel import Automovel
from veiculo import Veiculo

class Carro(Automovel):
	def __init__(self, marca, qtdRodas, modelo, velocidade, potencia, portas):
		Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potencia)
		self.portas = portas

	def imprint(self):
		print("carro com:", self.portas, " portas")


carro1 = Carro("fiat", 4, "punto", 80, 88, 3)
carro1.acelerar(25)
carro1.frear(0)
carro1.imprimi()
carro1.imprimir()
carro1.imprint()