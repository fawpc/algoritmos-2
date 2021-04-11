class Veiculo():
	def __init__(self, marca, qtdRodas, modelo, velocidade):
		self.marca = marca
		self.qtdRodas = qtdRodas
		self.modelo = modelo
		self.velocidade = velocidade
	

	def acelerar(self, aumenta):
		self.aumenta = aumenta
		if (aumenta >0): 
			self.aumenta += self.velocidade 
		else:
			self.aumenta = 0

	def frear(self, diminui):
		self.diminui = diminui
		if (diminui > 0):
			self.diminui -= self.velocidade
		else:
			self.diminui = 0

		
	def imprimi(self):
		print("o veiculo de marca: ", self.marca,
		"com ", self.qtdRodas, " rodas, ", "de modelo: ",
		self.modelo, " velocidade: ", self.velocidade, " aceleração: ", self.aumenta, 
		" e freio: ", self.diminui)
