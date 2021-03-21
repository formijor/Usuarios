'''
Created on 20 mar. 2021

@author: Jorge
'''

class Usuario():
    def __init__(self):
        self.nombre = ''
        self.clave = ''
    
    #Setters
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def set_clave(self, clave):
        self.clave = clave    
    
    def set_email(self, email):
        self.email = email
        
    def set_dni(self, tipo, numero):
        self.dni = (tipo, numero)
        
    def set_genero(self, genero):
        self.genero = genero
    
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento
        
    def set_pais(self, pais):
        self.pais = pais
        
    def set_ciudad(self, ciudad):
        self.ciudad = ciudad
    
    def set_profesion(self, profesion):
        self.profesion = profesion
        
    def set_especialidad(self, especialidad):
        self.especialidad = especialidad
        
    def set_institucion(self, institucion):
        self.institucion = institucion
        
    def set_pais_institucion(self, pais_institucion):
        self.pais_institucion = pais_institucion
        
    def set_ciudad_institucion(self, ciudad_institucion):
        self.ciudad_institucion = ciudad_institucion
        
    #GETTERS
    def get_nombre(self):
        return self.nombre
        
    def get_clave(self):
        return self.clave
    
    #Validacion de usuario
    def validar_usuario(self, nombre, clave):
        validar = True #Operacion en la base de datos
        if validar:
            self.set_nombre(nombre)
            self.set_clave(clave)
            return True
        else:
            mensaje = self.get_mensaje(1000)
            return (False, mensaje) 
    
    def get_mensaje(self, numero):
        mensaje = 'Error de usuario' #Reemplazar por sistema de mensajes de error
        return mensaje
    
    #CREACION DE USUARIO
    def crear_usuario(self, nombre, clave, email):
        creado = True
        if creado:
            mensaje = 'Usuario creado'
            return (True, mensaje)
        else:
            mensaje = 'No se pudo crear el usuario'
            return (False, mensaje)
        
    
    
    
        
        