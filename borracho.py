# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:31:46 2020

@author: luise
"""
import random

class Borracho:
    
    def __init__(self, name):
        self.name = name
    
class BorrachoTradicional(Borracho):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def camina(self):
        return random.choice([(0,1), (0, -1), (1,0), (-1,0)])
