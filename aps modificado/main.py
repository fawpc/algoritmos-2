from apartamento import Apartamento
from torre import Torre
from estacionamento import Fila
t1 = Torre(1, "são pedro", "piratini")
fila = Fila()
ap2 = Apartamento(2, "102", fila.adicionar("102") , None, t1)
ap1 = Apartamento(1, "101", fila.adicionar("101") , ap2.numero, t1)
ap1.imprimir()
ap2.imprimir()
fila.imprimir()
