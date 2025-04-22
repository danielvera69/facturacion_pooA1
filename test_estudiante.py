from datetime import date

class Periodo:
    def __init__(self,id,periodo,active):
        self.id=id
        self.periodo = periodo
        self.fecha_creacion=date.today()
        self.active = active

class Nivel:
    def __init__(self,id,nivel):
        self.id=id
        self.nivel = nivel
        self.fecha_creacion=date.today()
        self.active = True

class Asignatura:
    def __init__(self, id,descripcion,nivel,active):
        self.id = id
        self.descripcion = descripcion
        self.nivel= nivel
        self.fecha_creacion=date.today()
        self.active = active
        
class Profesor:
    def __init__(self,id, nombre,active):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion=date.today()
        self.active = active
        
class Estudiante:
    def __init__(self, id, nombre,active):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion=date.today()
        self.active = active

class Nota:
    def __init__(self,id, periodo,profesor,asignatura,active):
        self.id = id
        self.periodo = periodo
        self.profesor = profesor
        self.asignatura = asignatura
        self.detalleNota = []
        self.fecha_creacion=date.today()
        self.active = active
        
    def addNota(self):
      pass
        
class DetalleNota:
    def __init__(self, id,estudiante,  nota1, nota2, recuperacion=None, observacion=None):
        self.id = id
        self.estudiante = estudiante
        self.nota1 = nota1
        self.nota2 = nota2
        self.recuperacion = recuperacion
        self.observacion = observacion

    