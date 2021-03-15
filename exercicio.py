#exercicios
#fiz o basico, sei que poderia colocar um while para enquanto
#não fosse inserido dados validos continuar perguntando,
#talvez eu implemente durante a semana, se esse comentário ainda estiver
#aqui infelizmente não tive tempo
nome = ["batata", "pera", "abacaxi"]

precos = [1.00, 2.50, 5.00]

quantidade = [52, 35, 80]


selec= int(input('selecione uma função, 1 igual a consultar, 2 excluir item: '))
if selec<1 or selec>2 :
	print('digite um valor valido')
elif selec == 1:
	nomeprod= input('digite o nome do produto: ' )
	if nomeprod=='batata':
		print('produto: ', nome[0],' preço: ', precos[0], ' quantidade: ', quantidade[0])
	elif nomeprod=='pera':
		print('produto: ', nome[1], ' preço: ', precos[1], ' quantidade: ', quantidade[1])
	elif nomeprod=='pera':
		print('produto: ', nome[2], ' preço: ', precos[2], ' quantidade: ', quantidade[2])	

elif selec==2:
	nomedel= input('digite o produto a ser excluido: ')
	if nomedel=='batata':
		nome = ["pera", "abacaxi"]

		precos = [2.50, 5.00]

		quantidade = [35, 80]
		print('produtos: ', nome, ' preços: ', precos, ' quantidade: ', quantidade)

	elif nomedel=='pera':
		nome = ["batata", "abacaxi"]

		precos = [1.00, 5.00]

		quantidade = [52, 80]
		print('produtos: ', nome, ' preços: ', precos, ' quantidade: ', quantidade)

	elif nomedel=='abacaxi':
		nome = ["batata", "pera"]

		precos = [1.00, 2.50]

		quantidade = [52, 35]
		print('produtos: ', nome, ' preços: ', precos, ' quantidade: ', quantidade)

	else: 
		print('insira um valor valido')					