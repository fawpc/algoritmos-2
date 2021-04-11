from veiculo import Veiculo

class Bike(Veiculo):
	def __init__(self, marca, qtdRodas, modelo, velocidade, numMarchas, bagageiro):
		Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade )
		self.numMarchas = numMarchas
		self.bagageiro = bagageiro
		
	def imprimir(self):
		print("bike com:", self.numMarchas, " marchas", "e bagageiro:", self.bagageiro)

bike1 = Bike("caloi", 2, "de carbono", 25, 8, "de vime")
bike1.acelerar(0)
bike1.frear(14)
bike1.imprimi()
bike1.imprimir()		