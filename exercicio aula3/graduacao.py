from exercicio import Aluno

class AluGraduacao(Aluno):
	def __init__(self, codigo, nome, matricula, semestre):
		Aluno.__init__(self, codigo, nome, matricula)
		self.semestre = semestre
		print("semestre: ", semestre)