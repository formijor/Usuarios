'''
Created on 22 mar. 2021

@author: Jorge
'''
import Usuarios
import Mediador
import ManejoDatos

if __name__ == "__main__":
    mediador = Mediador.Mediador()
    usuario = Usuarios.Usuario(mediador)
    datos = ManejoDatos.DatosSQL(mediador)
    
    mediador.add_instancia(usuario, '1')
    mediador.add_instancia(datos, '2')
    
    usuario.enviar_mensaje()
    datos.enviar_mensaje()
