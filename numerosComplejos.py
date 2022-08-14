import math


def main():
    sumarComplejos([12, 2], [13, 1])
    restarComplejos([13, 4], [9, 8])
    multiplicarComplejos([8, 9], [2, 1])
    divisionComplejos([8, 9], [2, 1])
    moduloComplejos([8, -3])
    cartesianoAPolar([-2, 2])
    cartesianoAPolar([2, 2])
    faseComplejos([1,2])
    
def sumarComplejos(c1, c2):
    suma = [c1[0]+c2[0], c1[1]+c2[1]]
    printBonito(suma)


def restarComplejos(c1, c2):
    resta = [c1[0]-c2[0], c1[1]-c2[1]]
    printBonito(resta)


def multiplicarComplejos(c1, c2):
    multiplicacion = [c1[0]*c2[0]-c1[1]*c2[1], c1[1]*c2[0]+c1[0]*c2[1]]
    printBonito(multiplicacion)


def divisionComplejos(c1, c2):
    dividiendo = c2[0]**2 + c2[1]**2
    division = [(c1[0]*c2[0]+c1[1]*c2[1]) / dividiendo,
                (c2[0]*c1[1]-c1[0]*c2[1]) / dividiendo]
    printBonito(division)


def conjugadoComplejos(c1):
    conjugado = [c1[0], -c1[1]]
    printBonito(conjugado)


def moduloComplejos(c1):
    modulo = math.sqrt((c1[0])**2 + (c1[1]) ** 2)
    return modulo


def faseComplejos(c1):
    x = c1[0]
    y = c1[1]
    ## Encontrando el cuadrante segun los puntos
    if (x < 0 and y < 0) or (x < 0 and y >= 0):
        return math.pi + (math.atan(c1[1] / c1[0]))

    elif x >= 0 and y < 0:
        return 2 * math.pi +  (math.atan(c1[1 ] / c1[0 ] ) )

    else:
        return  (math.atan(c1[1 ] / c1[0 ] ) )


def cartesianoAPolar(c1):
    angulo = faseComplejos(c1)
    cartesianoAPolar = [moduloComplejos(c1), angulo]
    print(cartesianoAPolar)


def printBonito(respuesta):
    if (respuesta[1] > 0):
        print(str(respuesta[0]) + " + " + str(respuesta[1]) + "i")
    else:
        print(str(respuesta[0]) + " " + str(respuesta[1]) + "i")


main()
