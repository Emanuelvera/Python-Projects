import random

def tirar_dado(numeros_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numeros_de_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6]) # ambien podria ser random.randint(1,7)
        secuencia_de_tiros.append(tiro)
    
    return secuencia_de_tiros



def main (numeros_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range (numero_de_intentos):
        secuencia_de_tiros = tirar_dado (numeros_de_tiros)
        tiros.append(secuencia_de_tiros)


    tiros_con_1 = 0

    for tiro in tiros:
        if 1 in tiro:
            tiros_con_1 += 1
    
    probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos
    print (f"Probabilidad de obtene por lo menos un 1 en {numeros_de_tiros} tiros = {probabilidad_tiros_con_1}")



if __name__ == '__main__':
    numeros_de_tiros = int(input("cantidad de veces a tirar el dado: "))
    numero_de_intentos = int(input("cuantas veces correra la simulacion: "))

    main (numeros_de_tiros, numero_de_intentos )
