'''
Created on May 11, 2016

@author: ricardo
'''
class Transaccion:
    def __init__(self, monto, fecha, id_rest):
        self.monto = monto
        self.fecha = fecha
        self.id_rest = id_rest

class Historial:
    def __init__(self):
        self.trans = list()
        self.total = 0
        
    def agregarTransaccion(self, t):
        self.trans.append(t)
        self.total += t.monto

class BilleteraElectronica:
    '''
    classdocs
    '''

    def __init__(self, id, nombres, apellidos, ci, pin):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = ci
        self.pin = pin
        self.creditos = Historial()
        self.debitos = Historial()
        
    def saldo(self):
        return self.creditos.total - self.debitos.total
    
    def recargar(self, monto, fecha, id_rest):
        self.creditos.agregarTransaccion(Transaccion(monto, fecha, id_rest))
        
    def consumir(self, monto, fecha, id_rest, pin):
        if pin == self.pin and monto <= self.saldo():
            self.debitos.agregarTransaccion(Transaccion(monto, fecha, id_rest))
        elif pin != self.pin:
            print("No realizó la transacción, PIN incorrecto.")
        elif self.saldo() < monto:
            print("No realizó la transacción, saldo insuficiente.")
            
        
        