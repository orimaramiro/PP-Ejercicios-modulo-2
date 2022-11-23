# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con lambda

import numpy as np

        # Lambda expression
    # 1)
    # Realizar una funcion lambda que eleve al cuadrado
    # el número pasado como parámetro
numeros = [1, -5, 4, 3]
def al_cuadrado ():
    potencia_2 = lambda x: x**2
    pot_3 = potencia_2(2)
    print(pot_3)
    # 2)
    # Utilice la función map para mapear una lambda expression
    # que retorne la potencia de 2 de cada numero en la lista numeros
    # El resultado (la potencia de cada numero) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line", es decir,
    # no declarar la lambda fuera del map sino diretamente dentro
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "potencia_2" dentro del map, debe colocar
    # directamente la lambda.
def al_cuadrado_lista():
    numeros_lambda = list(map(lambda x: x**2, numeros))
    print(numeros_lambda)
    # Lista de numeros


    # numeros_potencia = list(map....)
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    al_cuadrado()
    al_cuadrado_lista()
    print("terminamos")