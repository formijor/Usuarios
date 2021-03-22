'''
Created on 22 mar. 2021

@author: Jorge
'''
import Usuarios
import DBusuarios

class Mediador():
    def __init__(self):
        self.name = 'Mediador Usuario'
        self.usuarios = {}
        self.db_usuarios = DBusuarios.ControlDB(self)
        
    def loguear_usuario(self, email): #modificar para que use un solo campo unico (DNI o usuario)
        datos = self.db_usuarios.get_datos_usuario(email)[0]
        usuario = Usuarios.Usuario(self, datos)
        self.usuarios[str(usuario.get_id())]= usuario
    
    def get_nombres_usuarios_logueados(self):
        lista_nombres = []
        for usuario in self.usuarios.values():
            lista_nombres.append(usuario.get_nombre())
        return lista_nombres
    
    def get_lista_usuarios_logueados(self):
        lista_usuarios = []
        for usuario in self.usuarios.values():
            datos_usuario = (usuario.get_id(), usuario.get_nombre(), usuario.get_email())
            lista_usuarios.append(datos_usuario)
        return lista_usuarios
    
    def get_usuario_nombre(self, id_usuario):
        nombre = self.usuarios[id_usuario].get_nombre()
        return nombre
    
    def get_lista_usuarios_registrados(self):
        return self.db_usuarios.get_lista_usuarios_registrados()
    
    def registrar_usuario(self, datos):
        self.db_usuarios.registrar_usuario(datos)
        
    def crear_db(self):
        self.db_usuarios.crear_db()
        
    def truncar_tabla_usuarios(self):
        self.db_usuarios.truncar_tabla_usuarios()
        
    def cerrar_conexion(self):
        self.db_usuarios.cerrar_conexion()
    
    
    
if __name__ == "__main__":
    mediador = Mediador()
    #mediador.crear_db()
    #datos = {'nombre': 'Jorge', 'email': 'formijor@gmail.com', 'id': 1}
    #mediador.loguear_usuario(datos)
    #datos = {'nombre': 'Carolina', 'email': 'scmontoya1@gmail.com', 'id': 2}
    #mediador.loguear_usuario(datos)
    #mediador.truncar_tabla_usuarios()
    '''datos1 = ['"Jorge"','"lalala1"','"formijor@gmail.com"']
    mediador.registrar_usuario(datos1)
    datos2 = ['"Carolina"','"lalala2"','"scmontoya1@gmail.com"']
    mediador.registrar_usuario(datos2)'''
    
    #print (mediador.get_lista_usuarios_registrados())
    
    print ('-----> Logueando Usuarios \n')
    mediador.loguear_usuario("'formijor@gmail.com'")
    mediador.loguear_usuario("'scmontoya1@gmail.com'")
    
    print ('===== Usuarios Logueados =====')
    print ('Usuarios Logueados: ', mediador.get_lista_usuarios_logueados())
    print ('Nombres de usuarios Logueados: ', mediador.get_nombres_usuarios_logueados())
    print ('==============================\n')
    
    mediador.cerrar_conexion()
    #print (mediador.get_nombres_usuarios_logueados())
    #print (mediador.get_lista_usuarios_logueados())
        