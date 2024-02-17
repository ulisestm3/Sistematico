def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
#Ejemplo de uso
#numero_terminos = 10
numero_terminos = int(input("Ingrese numero de terminos: "))
print("Serie de Fibonacci:")
for i in range(numero_terminos):
    print(fibonacci(i))