from datetime import date
from dataclasses import dataclass


@dataclass
class Familiar:
    parentezco: str
    nombre: str
    apellido: str
    fecha_nacimiento: date
    def __init__( self, parentezco : str, nombre: str, apellido: str, fecha_nacimiento: date ):
        self.parentezco = parentezco
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        
@dataclass
class Usuario:
    """
    Pertenece la Capa de Reglas de Negocio (Model)

    Representa a un usuario de la EPS en la aplicación
    """
    cedula: str
    nombre : str
    apellido : str
    correo : str
    direccion : str
    telefono : str
    codigo_departamento : str
    codigo_municipio : str
    familiares : list[Familiar]
    
    def __init__( self, cedula, nombre, apellido, correo, direccion, telefono, codigo_departamento, codigo_municipio )  :
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
        self.codigo_departamento = codigo_departamento
        self.codigo_municipio = codigo_municipio
        self.familiares = []

    def agregarFamiliar(self, parentezco : str, nombre: str, apellido: str, fecha_nacimiento: date ):
        """
        Registra una persona en el grupo familiar de un usuario

        Parametros: Parentezco, nombre, apellido, fecha nacimiento 
        """ 
        persona = Familiar( parentezco, nombre, apellido, ( fecha_nacimiento)  ) 
        self.familiares.append( persona )   

    def esIgual( self, comparar_con ) :
        """
        Compara el objeto actual, con otra instancia de la clase Usuario
        """
        assert( self.cedula == comparar_con.cedula )
        assert( self.nombre == comparar_con.nombre )
        assert( self.apellido== comparar_con.apellido )
        assert( self.direccion== comparar_con.direccion )
        assert( self.correo== comparar_con.correo )
        assert( self.telefono== comparar_con.telefono )
        assert( self.codigo_departamento== comparar_con.codigo_departamento )
        assert( self.codigo_municipio== comparar_con.codigo_municipio )

        posicion = 0
        # Cuando comparemos objetos que contienen listas, el primer paso 
        # es verificar que tengan el mismo numero de elementos
        assert( len(self.familiares) == len(comparar_con.familiares) )
        
        # Estrategia: recorrer mi lista d efmailiares y comprarla con la de la otra instancia
        # Usando la posicion
        for f in self.familiares:
            familiar_comparacion = comparar_con.familiares[ posicion ]

            assert( f.parentezco == familiar_comparacion.parentezco )
            assert( f.nombre == familiar_comparacion.nombre )
            assert( f.apellido == familiar_comparacion.apellido )
            assert( f.fecha_nacimiento == familiar_comparacion.fecha_nacimiento )

            posicion = posicion + 1

