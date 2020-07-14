# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:53:42 2020

@author: luise
"""

from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)
    
    for _ in range(pasos):
        campo.mover_borracho(borracho)
        
    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0,0)
    distancias = []
    
    for _ in range (numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata , 1))
        
    return distancias

def graficar_distancia_media(x, y):
    grafica = figure(title='Camino aleaotrio', x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x, y, legend = 'distancia media')
    
    show(grafica)

def graficar_posicion_recorrida(x, y):
    pass


def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []
    n = 0
    distancia = []
    
    for pasos in distancias_de_caminata:
        distancia.append([simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)])
        distancia_media = round(sum(distancia[n][0])/len(distancia[n][0]), 4)
        distancia_maxima = max(distancia[n][0])
        distancia_minima = min(distancia[n][0])
        distancias_media_por_caminata.append(distancia_media)
        n += 1
        print(f' {tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')
        
    graficar_distancia_media(distancias_de_caminata, distancias_media_por_caminata)
    return distancia
if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100
    
    distancia = main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)