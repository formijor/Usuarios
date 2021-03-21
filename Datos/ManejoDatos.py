'''
Created on 21 mar. 2021

@author: Jorge
'''

import sqlite3


class DatosSQL():
    def __init__(self):
        self.connection_string = ''
        
    def get_datasource(self):
        datasource = ''
        return datasource
    
    def connectar(self, datasource):
        print (datasource)
        self.conn = sqlite3.connect(datasource)
        return self.conn
    
    def cerrar_conexion(self):
        self.conn.close()
        
    def ejecutar_query(self, query):
        cursor = self.conn.execute(query)
        return cursor
    
class Datasource():
    def __init__(self):
        self.datasource = ''
        
    def get_datasource(self):
        return 'connexion="Usuarios"'

source = Datasource()
datos = DatosSQL()
if __name__ == "__main__":
    datasource = 'Usuarios'#source.get_datasource()
    datos.connectar(datasource)
    datos.cerrar_conexion()