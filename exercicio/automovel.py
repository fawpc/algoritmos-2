from veiculo import Veiculo

class Automovel(Veiculo):
	def __init__(self, marca, qtdRodas, modelo, velocidade, potencia):
		Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade )
		self.potencia = potencia
		
	def imprimir(self):
		print("automovel com: ", self.potencia, "cv de potência")