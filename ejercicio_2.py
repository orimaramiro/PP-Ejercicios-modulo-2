# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con lambda



    # Lambda expression
    # 1)
    # Realizar una funcion lambda que retorne el tamaño
    # (len) de un string pasado como parámetro
def len_str():
    len_string = lambda x : len(x)
    cadena = len_string ("cada vez más difícil")
    print (cadena)
    # 2)
    # Lista de string
    

    # Utilice la función map para mapear una lambda expression
    # que retorne el tamaño (len) de cada texto em cata iteración
    # de la lista de textos
    # El resultado (el len de cada palabra) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line"
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "len_string" dentro del map, debe colocar
    # directamente la lambda.
def len_str_palabras():
    palabras = ['Inove', 'casa', 'programacion']
    palabras_lambda = list(map(lambda x: len(x), palabras))
    print(palabras_lambda)
    # palabras_len = list(map....)
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    len_str ()
    len_str_palabras()
    print("terminamos")