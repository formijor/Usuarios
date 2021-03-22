'''
Created on 22 mar. 2021

@author: Jorge
'''



class Mediador():
    def __init__(self):
        self.lista_instancias = {}
            
    def add_instancia(self, instancia, id_instancia):
        self.lista_instancias[id_instancia] = instancia
    
    def enviar_mensaje(self, instancia, mensaje):
        self.lista_instancias[instancia].imprimir_mensaje(mensaje)
    