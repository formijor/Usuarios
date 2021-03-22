'''
Created on 22 mar. 2021

@author: Jorge
'''

import sqlite3


class ControlDB():
    def __init__(self, mediador):
        self.connection_string = ''
        self.mediador = mediador
        self.query = Query()
        self.connectar('Usuarios')
        
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
    
    '''def get_usuario_id(self, email):
        query = self.query.buscar_usuario_por_email(email)
        return self.ejecutar_query(query)'''
    
    def get_datos_usuario(self, email):
        query = self.query.buscar_usuario_por_email(email)
        return self.ejecutar_query(query)
    
    def registrar_usuario(self, usuario_datos):
        query = self.query.insertar_usuario(usuario_datos, 'usuario')
        self.ejecutar_query(query)
        
    def get_lista_usuarios_registrados(self):
        query = self.query.lista_usuarios()
        return self.ejecutar_query(query)
        
    def truncar_tabla_usuarios(self):
        query = self.query.truncar_tabla('Usuario')
        self.ejecutar_query(query)
    
    def enviar_mensaje(self):
        self.mediador.enviar_mensaje('1', 'Hola')
    
    def imprimir_mensaje(self, mensaje):
        print ('Soy Datos y me mandaron a decir: ' + mensaje)
        
    def crear_db(self):
        query = self.query.crear_tabla_usuario()
        self.ejecutar_query(query)
        
        
class Query():
    def __init__(self):
        pass
    
    def insertar_usuario(self, datos, tabla):
        query = 'INSERT INTO ' + tabla + ' VALUES (Null,'
        for dato in datos:
            query = query + dato + ','
        query = query[:-1] + ')'
        return query
        
    def buscar_usuario_por_nombre(self, nombre):
        query = 'SELECT * FROM Usuario WHERE nombre = ' + nombre
        return query
    
    def buscar_usuario_por_email(self, email):
        query = 'SELECT * FROM Usuario WHERE email = ' + email
        return query
    
    def truncar_tabla(self, tabla):
        query = 'DELETE FROM ' + tabla
        return query
    
    def lista_usuarios(self):
        query = 'SELECT * FROM Usuario'
        return query
    
    def lista_ciudad(self):
        query = 'SELECT * FROM Ciudad'
        return query
    
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