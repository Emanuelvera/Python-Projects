import random

def busqueda_linea(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break

    return match


if __name__ == "__main__":
    tamaño_de_la_lista = int(input("De que tamaño sera la lista?"))
    objetivo = int(input("Que numero quieres encontrar?"))

    lista = [random.randint(0,100) for i in range(tamaño_de_la_lista)]

    encontrado = busqueda_linea(lista, objetivo)
    print(lista)
    print(f"El elemento {objetivo} {'esta' if encontrado else 'no esta'} en la lista ")


''' Aca podemos ver que mientras mas grande sea n mas va a 
demorar en buscar el numero, esto es una O(n) es una funcion lineal'''
                            
