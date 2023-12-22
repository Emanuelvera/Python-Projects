def f(x):
    respuesta = 0

    for i in range (1000):    # Esto va a corre 1000 veces sin importar el tamaño de x
        respuesta += 1 

    for i in range (x):       # Esto va a corre x veces puede ser 1 o 1millon
        respuesta += x

    for i in range (x):       # 2x**2
        for j in range(x):
            respuesta += 1
            respuesta += 1 

    return respuesta

# El alcance de la funcion seria: 1002 + x + 2x**2

