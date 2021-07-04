class Apartamento():
	def __init__(self, id_ap, numero, vaga, proximo, torre):
		self.id_ap = id_ap
		self.numero = numero
		self.vaga = vaga
		self.proximo = proximo
		self.torre = torre


	def cadastrar(self):
		print("Apartamento cadastrado")	

	def imprimir(self):
			print("o Apartamento do condominio alvorada da torre: ", self.torre.nome, " |endereço: ", 
				self.torre.endereco, "|com identificação: ", self.id_ap, " |numero: ", self.numero, " |vaga de estacionamento: ", self.vaga, " |e proximo no estacionamento: ", self.proximo)	
			print("---------------------------------------------------")
