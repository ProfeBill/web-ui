# Para las aplicaciones web creadas con Flask, debemos importar siempre el modulo flask
# la clase request permite acceso a la información de la petición HTTP
from flask import Flask, request, jsonify    

# Para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template
from flask import render_template

from Usuario import Usuario
import ControladorUsuarios

# Flask constructor: crea una variable que nos servirá para comunicarle a Flask
# la configuración que queremos para nuestra aplicación
app = Flask(__name__)     

@app.route("/view/new-user")
def VistaCrearUsuario():
   return render_template("new-user.html")
   
@app.route("/view/save-user")  
def VistaGuardarUsuario():
   cedula="321654987"
   nombre = request.args["nombre"]
   apellido = request.args["apellido"]
   correo="no@tiene.com"
   direccion="no tiene"
   telefono="paila"
   codigo_departamento = request.args["codigo_departamento"]
   codigo_municipio=codigo_departamento + "001"

   nuevo_usuario = Usuario(cedula,nombre,apellido,correo,direccion,telefono,codigo_departamento,codigo_municipio)
   ControladorUsuarios.Insertar(nuevo_usuario)
   return "usuario guardado"
    
# Esta linea permite que nuestra aplicación se ejecute individualmente
if __name__=='__main__':
   app.run( debug=True )