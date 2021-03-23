class Aluno():
	def __init__(self, codigo, nome, matricula):
		self.codigo = codigo
		self.nome = nome
		self.matricula = matricula
		
	def imprimir(self):
			print("codigo: ", self.codigo)
			print("nome: ", self.nome)
			print("matricula: ", self.matricula)