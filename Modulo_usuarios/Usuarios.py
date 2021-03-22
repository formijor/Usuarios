'''
Created on 22 mar. 2021

@author: Jorge
'''

class Usuario():
    def __init__(self, mediador, datos):
        self.set_datos(datos)
        self.mediador = mediador
    
    #-------------------------------------------------Setters
    
    def set_datos(self, datos):
        self.set_id_usuario(datos[0])
        self.set_nombre(datos[1])
        self.set_email(datos[3])
               
    def set_id_usuario(self, id_usuario):
        self.id_usuario = id_usuario
    
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
        
    def set_email_institucion(self, email):  
        self.email_institucion = email  
        
    def set_pais_institucion(self, pais_institucion):
        self.pais_institucion = pais_institucion
        
    def set_ciudad_institucion(self, ciudad_institucion):
        self.ciudad_institucion = ciudad_institucion
        
    #--------------------------------------------------------GETTERS
    def get_nombre(self):
        return self.nombre
        
    def get_clave(self):
        return self.clave
    
    def get_email(self):
        return self.email
    
    def get_id(self):
        return self.id_usuario
    
    def enviar_mensaje(self):
        self.mediador.enviar_mensaje('2', 'Chau')
    
    def imprimir_mensaje(self, mensaje):
        print ('soy usuario y me mandaron a decir: '+ mensaje)
    