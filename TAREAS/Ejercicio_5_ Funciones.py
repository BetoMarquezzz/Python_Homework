

#   REALIZAR EJEMPLOS DE FUNCIONES 


def multiplicar(a, b):
    resultado = a * b
    return resultado


def saludar():
    print("¡Hola, mundo!")


def encontrar_maximo(lista):
    maximo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo


def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32