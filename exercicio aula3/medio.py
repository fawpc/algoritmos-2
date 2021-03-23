from exercicio import Aluno

class AluMedio(Aluno):
	def __init__(self, codigo, nome, matricula, ano):
		Aluno.__init__(self, codigo, nome, matricula)
		self.ano = ano
		print("ano: ", ano)