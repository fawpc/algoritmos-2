from abc import ABCMeta, abstractmethod
class Computador(metaclass=ABCMeta):
	@property
	def modelo(self):
		pass
	
	@property
	def cor(self):
		pass

	@property
	def preco(self):
		pass				
		
	@property
	def getInformacoes(self):
		pass

	@property
	def cadastrar(self):
		pass
		
			
	@modelo.setter
	@abstractmethod
	def modelo(self, modelo):
		pass

	@cor.setter
	@abstractmethod
	def cor(self, cor):
		pass
	
	@preco.setter
	@abstractmethod
	def preco(self, preco):
		pass

	@getInformacoes.setter
	@abstractmethod
	def getInformacoes(self):
		pass

	@cadastrar.setter
	@abstractmethod
	def cadastrar(self):
		pass	