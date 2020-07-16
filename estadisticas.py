import random
import math

def media(x):
    return sum(x) / len(x)

def varianza(x):
    mu = media(x)

    acumulador = 0
    for i in x:
        acumulador += (i - mu)**2

    return acumulador / len(x)

def desviacion_estandar(x):
    return math.sqrt(varianza(x))

def distribucion_normal(media, sigma, limites=[-inf, inf]):
    pass

if __name__ == '__main__':
    X = [random.randint(1,21) for i in range(20)]
    mu = media(X)
    sigma_cuadrado = varianza(X)
    sigma = desviacion_estandar(X)
    print(X)
    print(f' media = {mu}')
    print(f' varianza = {sigma_cuadrado}')
    print(f' desviación estándar = {sigma}')