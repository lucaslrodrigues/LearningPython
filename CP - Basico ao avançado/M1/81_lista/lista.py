lista = [1,2,3,4]
lista[3] = 99

del lista[0]
print(lista)
lista[0] = "new value"
print(lista)

lista.append(5) # Add last value
print(lista)

lista.pop() # remove last value
print(lista)

lastValue = lista.pop() # retorna o último valor
print(lastValue)

lista.insert(2, "lucas")
print(lista)


listaA = [1,2,3]
listaB = [4,5,6]
listaC = listaA + listaB

print(listaC)
listaA.extend(listaB)
print(listaA)