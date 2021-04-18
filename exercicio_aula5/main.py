from pessoa import Pessoa
from fisica import Fisica
from juridica import Juridica
p1 = Fisica("2","pedro", "rua loureiro", 5553750, 775442, 15, 80, 1.85)
p1.calculoIMC()
p1.imprimir()
p1.imprime()

p2 = Juridica("1", "joão", "rua pinhais", 5553750, 40028922, "RS 036", 83)
p2.imprimi()
p2.notaFiscal(0)

p3 = Juridica("3", "joão", "rua pinhais", 5553750, 400222, "RS 076", 23)
p3.imprimi()
p3.notaFiscal(1)