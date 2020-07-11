# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:04:54 2020

@author: luise
"""
import time

def fibonacci_recursivo(n,):
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    
    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado
        
        return resultado
        

if __name__ == '__main__':
    n = 40
    comienzo = time.time()
    fibo = fibonacci_dinamico(n)
    final = time.time()
    print(f'El numero de fibonacci de {n} es {fibo}\nEl algoritmo tomo {final-comienzo} segundos')