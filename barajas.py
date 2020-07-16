import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
#VALORES = ['as', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jota', 'reina', 'rey']
VALORES = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
    
    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    return mano

def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0
    corridas = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter = dict(collections.Counter(valores))
        cartas = sorted(list(counter.keys()))
        if cartas == list(range(cartas[0],cartas[0]+tamano_mano-1)):
            corridas +=1
            break

        for var in counter.values():
            if var == 2:
                pares += 1
                break
    probabilidad_par = pares / intentos
    probabilidad_corrida = corridas / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} cartas es {probabilidad_par}')
    print(f'La probailidad de obtener una carrera en una mano de {tamano_mano} cartas es {probabilidad_corrida}')

if __name__ == '__main__':
    
    barajas = crear_baraja()
    mano = obtener_mano(barajas, 5)
    print(mano)
    tamano_mano = 6
    intentos = 1000

    main(tamano_mano, intentos)