class TipoCuenta: # ahorro, corriente
    def __init__(self,id,descripcion):
        self.id=id
        self.descripcion = descripcion

class Cuenta:
    def __init__(self, id,valor):
        self.id = id
        self.descripcion = valor # codigo y descripcion de la cuenta
     
class Cliente:
    def __init__(self,cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre

class RetiroDeposito:
    def __init__(self,id, cliente,tipo_transaccion,tipo_cuenta,cuenta):
        self.id = id
        self.cliente = cliente
        self.tipo_transaccion = tipo_transaccion # retiro, deposito
        self.tipo_cuenta = tipo_cuenta # ahorro o corriente
        self.cuenta = cuenta # numero de cuenta
        self.DetalleRetiroDeposito = []
        
    def addDetalleRetiroDeposito(self):
      pass
        
class DetalleRetiroDeposito:
    def __init__(self, id,fecha_transaccion,valor_transaccion):
        self.id = id
        self.fecha_transaccion = fecha_transaccion
        self.valor_transaccion = valor_transaccion

    