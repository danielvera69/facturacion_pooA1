class TipoPrestamo: # hipotecario, comercial, emprendimiento
    def __init__(self,id,descripcion):
        self.id=id
        self.descripcion = descripcion

class TasaInteres:
    def __init__(self, id,valor):
        self.id = id
        self.valor = valor # porcentaje de tasa de interes
     
class Cliente:
    def __init__(self,id, nombre):
        self.id = id
        self.nombre = nombre

class Prestamo:
    def __init__(self,id, cliente,tipo_prestamo,fecha_prestamo,valor_prestamo,interes,valor_total,num_pagos):
        self.id = id
        self.cliente = cliente
        self.tipo_prestamo = tipo_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.valor_prestamo = valor_prestamo
        self.interes = interes
        self.valor_total = valor_total # valor_prestamo*interes
        self.num_pagos = num_pagos
        self.detalleCuotasPrestamos = []
        
    def addDetalleCoutasPrestamo(self):
      pass
        
class DetalleCoutasPrestamo:
    def __init__(self, id,fecha_pago,  valor_cuota):
        self.id = id
        self.fecha_pago = fecha_pago
        self.valor_cuota = valor_cuota

    