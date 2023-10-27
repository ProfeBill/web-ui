# Para las aplicaciones web creadas con Flask, debemos importar siempre el modulo flask
# la clase request permite acceso a la información de la petición HTTP
from flask import Flask, request, jsonify , url_for   

# Para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template
from flask import render_template

from Usuario import Usuario
import ControladorUsuarios

# Flask constructor: crea una variable que nos servirá para comunicarle a Flask
# la configuración que queremos para nuestra aplicación
app = Flask(__name__)     

@app.route("/")
def Home():
   return render_template("index.html")

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

@app.route("/view/user")
def vistaVerUsuario():
   cedula = request.args["cedula"]
   usuario = ControladorUsuarios.BuscarPorCedula(cedula)
   return render_template("usuario.html", user = usuario )


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

@app.route("/site-map")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    # links is now a list of url, endpoint tuples
    return links
    
# Esta linea permite que nuestra aplicación se ejecute individualmente
if __name__=='__main__':
   app.run( debug=True )