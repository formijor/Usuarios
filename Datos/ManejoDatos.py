'''
Created on 21 mar. 2021

@author: Jorge
'''

import sqlite3


class DatosSQL():
    def __init__(self, mediador):
        self.connection_string = ''
        self.mediador = mediador
        
    def get_datasource(self):
        datasource = ''
        return datasource
    
    def connectar(self, datasource):
        self.conn = sqlite3.connect(datasource)
        return self.conn
    
    def cerrar_conexion(self):
        self.conn.close()
        
    def ejecutar_query(self, query):
        cursor = self.conn.execute(query)
        self.conn.commit()
        return cursor.fetchall()
    
    def enviar_mensaje(self):
        self.mediador.enviar_mensaje('1', 'Hola')
    
    def imprimir_mensaje(self, mensaje):
        print ('Soy Datos y me mandaron a decir: ' + mensaje)
    
class Datasource():
    def __init__(self):
        self.datasource = ''
        
    def get_datasource(self):
        return 'connexion="Usuarios"'

class Query():
    def __init__(self):
        pass
    
    def insertar_usuario(self, datos, tabla):
        query = 'INSERT INTO ' + tabla + ' VALUES ('
        for dato in datos:
            query = query + dato + ','
        query = query[:-1] + ')'
        return query
        
    def buscar_usuario_por_nombre(self, nombre):
        query = 'SELECT * FROM Usuario WHERE nombre = ' + nombre
        return query
    
    def buscar_usuario_por_email(self, nombre):
        query = 'SELECT * FROM Usuario WHERE email = ' + nombre
        return query
    
    def lista_usuarios(self):
        query = 'SELECT * FROM Usuario'
        return query
    
    def lista_ciudad(self):
        query = 'SELECT * FROM Ciudad'
        return query
        
class UsuariosDatabase():
    def __init__(self):
        pass
    
    def crear_tabla_usuario(self):
        query = '''CREATE TABLE Usuario (
    id_usuario integer PRIMARY KEY,
       nombre text NOT NULL,
       clave text NOT NULL,
    email text NOT NULL UNIQUE)'''
        return query
    
    def crear_tabla_ciudad(self):
        query = '''CREATE TABLE Ciudad (
        id_ciudad integer PRIMARY KEY,
        id_pais integer NOT NULL,
        nombre text NOT NULL
        )'''
        return query
        
    
source = Datasource()
datos = DatosSQL()
query = Query()
usuarios = UsuariosDatabase()
if __name__ == "__main__":
    datasource = 'Usuarios'#source.get_datasource()
    datos.connectar(datasource)
    #datos.ejecutar_query('DROP TABLE Usuario')
    datos.ejecutar_query(usuarios.crear_tabla_usuario())
    #datos.ejecutar_query('DROP TABLE Usuario')
    '''
    datos.ejecutar_query(usuarios.crear_tabla_ciudad())
    try:
        datos.ejecutar_query(query.insertar_usuario(('Null', '"Carolina Montoya"','"lalala"','"scmontoya1@gmail.com"'), '"Usuario"'))
        datos.ejecutar_query(query.insertar_usuario(('Null', '"Jorge Formigo"','"lalala"','"Formijor@gmail.com"'), '"Usuario"'))
    except:
        print ('error')
    resultado = datos.ejecutar_query(query.buscar_usuario_por_nombre('"Jorge Formigo"'))
    print(resultado)
    resultado = datos.ejecutar_query(query.lista_usuarios())
    print(resultado)'''
    datos.cerrar_conexion()
    
    
    
    