from automovel import Automovel
from veiculo import Veiculo

class Moto(Automovel):
	def __init__(self, marca, qtdRodas, modelo, velocidade, potencia, partida):
		Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potencia)
		self.partida = partida

	def imprint(self):
		print("moto com partida:", self.partida)

moto1 = Moto("kawasaki", 2, "ninja", 80, 500, "eletronica")
moto1.acelerar(15)
moto1.frear(0)
moto1.imprimi()
moto1.imprimir()
moto1.imprint()		

