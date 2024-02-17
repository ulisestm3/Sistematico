#Listas
lista = [1, 2, 3, "Manzana", 15.6, True]
print(lista)

#Imprimir el primer elemento de la lista
print(lista[0])

#Tamaño de la lista
tam = len(lista)
print(f"El tamaño es {tam}")

#imprimir el ultimo valor
print(lista[tam-1])

#Imprimir los primeros 3 elementos
print(lista[0:3])

#Imprimir los elementos 4 hasta 6
print(lista[3:7])

#agregar un elemento a la lista
lista.append("Zuniga")
print(lista)

#imprimir los ultimos 3 elementos de la lista
final = len(lista)
inicio = final - 3
print(lista[inicio: final + 1])

#eliminar manzana
lista.remove("Manzana")
lista.remove("Zuniga")

#ordenar la lista
lista.sort()
print(lista)