#                                                                     Tarea 3
#                                                                     LISTAS



mi_lista = [] # nada

lista = [2, ['a', 'b', 'e', 'f', 'h', 'r'], 10.9, 'que onda'] 

print (lista)                                                # [2, ['a', 'b', 'e', 'f', 'h', 'r], 10.9, 'que onda'] 

lista.reverse()
print(lista)                                                 # ['que onda', 10.9, ['a', 'b', 'e', 'f', 'h', 'r], 1]

lista=[30, 15, 50, 72, 58, 789]
print(len(lista))                                            # imprime un 6


lista.append(100)
print(len(lista))                                            # imprime un 7
print(lista[5])                                              # imprime un 789
print(lista[1])                                              # imprime un 15