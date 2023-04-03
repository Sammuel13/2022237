from FilaSequencialCircular import Fila,FilaException

fila = Fila()
fila.enfileira(10)
fila.enfileira(20)
fila.enfileira(30)
fila.enfileira(40)
# print('Elemento(): ', fila.elemento(3))
# print('busca(): ', fila.busca(20))

fila2 = Fila()
fila2.enfileira(11)
fila2.enfileira(22)
fila2.enfileira(33)

print(fila)
print(fila2)

fres = Fila.combina(fila,fila2)

print(fres)
# try:
#     for i in range(10):
#         print(fila.desenfileira())
# except FilaException as fe:
#     print(fe)