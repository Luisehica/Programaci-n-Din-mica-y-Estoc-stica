# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:04:54 2020

@author: luise
"""
import time
import sys 

def fibonacci_recursivo(n, count):
    count += 1
    if n == 0 or n == 1:
        return 1, count
    return fibonacci_recursivo(n-1, count) + fibonacci_recursivo(n-2, count), count

def fibonacci_dinamico(n, count, memo = {}):
    count += 1
    if n == 0 or n == 1:
        return 1, count
    
    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, count, memo) + fibonacci_dinamico(n - 2, count, memo)
        memo[n] = resultado
        
        return resultado , count
        

if __name__ == '__main__':
    sys.setrecursionlimit(10002)
    n = 6
    comienzo = time.time()
    count = 0
    count1 = 0
    fibo, count = fibonacci_recursivo(n,count)
    fibo1, count1 = fibonacci_dinamico(n, count1)
    print(f' recursivo {count}, dinamico {count1}')
    final = time.time()
    print(f'El numero de fibonacci de {n} es {fibo}\nEl algoritmo tomo {final-comienzo} segundos')