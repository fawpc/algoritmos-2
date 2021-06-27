from no_estacionamento import No
class Fila:
	def __init__(self):
		self.inicio = None
		self.fim = None
		self.tamanho = 0

	def adicionar(self, valor):
		no = No(valor)
		if self.tamanho ==0:
			self.inicio = no
			self.fim = no
		elif self.tamanho >=7:
			no = No("esperando vaga")
			print("no aguardo de vaga")
			self.fim.proximo = no
			self.fim = no			
			self.remover()	
		elif self.tamanho >=5:
			no = No("esperando vaga")
			print("no aguardo de vagas")
			self.fim.proximo = no
			self.fim = no				
		else:
			self.fim.proximo = no
			self.fim = no
		self.tamanho +=1
		
	def imprimir(self):
		texto = "";
		if self.tamanho == 0:
			texto = "Fila vazia"
		else:
			aux = self.inicio
			while(aux):
				texto = texto + str(aux.dado) + " - "
				aux = aux.proximo
		print("vagas ocupadas: ", texto)
		
	def remover(self):
		if self.tamanho == 0:
			print("Fila vazia")	
		elif self.tamanho == 1:
			self.inicio = None
			self.fim = None
			self.tamanho -=1
		elif self.tamanho >=5:
			aux = self.inicio
			while(aux):
				if aux.dado == 1 and aux.proximo.dado == "esperando vaga":
					aux.proximo.dado = 2
					break
				elif aux.dado == 2 and aux.proximo.dado == "esperando vaga":
					aux.proximo.dado = 3
					break
				elif aux.dado == 3 and aux.proximo.dado == "esperando vaga":
					aux.proximo.dado = 4
					break
				elif aux.dado == 4 and aux.proximo.dado == "esperando vaga":
					aux.proximo.dado = 5
					break
				elif aux.dado == 5 and aux.proximo.dado == "esperando vaga":
					aux.proximo.dado = 1
					break
				else:
					aux = aux.proximo
			self.inicio = self.inicio.proximo
			self.tamanho -=1					
		else:
			self.inicio = self.inicio.proximo
			self.tamanho -=1