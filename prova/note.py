from computador import Computador
class Note(Computador):
	def __init__(self, modelo, cor, preco, tempoBateria):
		self._modelo = modelo
		self._cor = cor
		self._preco = preco
		self.__tempoBateria = tempoBateria

		
	@property
	def modelo(self):
		return self._modelo

	@modelo.setter
	def modelo(self, modelo):
		self._modelo = modelo

	@property
	def cor(self):
		return self._cor				

	@cor.setter
	def cor(self, cor):
		self._cor = cor

	@property
	def preco(self):
		return self._preco				

	@preco.setter
	def preco(self, preco):
		self._preco = preco

	@property
	def getInformacoes(self):
		return self.getInformacoes
	

	def getInformacoes(self):
		print ('notebook de modelo: ', self._modelo, ' cor: ', self._cor, ' preco: ',
		self._preco, ' e duração de bateria de: ', self.__tempoBateria, 'horas')

	@property
	def cadastrar(self):
		return self.cadastrar

	def cadastrar(self):
		print ('notebook cadastrado com sucesso')			
