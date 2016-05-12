'''
Created on May 11, 2016

Hecho por:
    Ricardo Münch. Carnet: 11-10684.
    Raquel Prado. Carnet: 11-10801.
'''
import sys
from datetime import datetime

class Transaccion:
    def __init__(self, monto, id_rest):
        self.monto = monto
        self.fecha = datetime.now()
        self.id_rest = id_rest

class Historial:
    def __init__(self):
        self.trans = list()
        self.total = 0
        
    def agregarTransaccion(self, t):
        if self.total < 0:
            self.total = 0

        if (t.monto == sys.float_info.max and 0 < self.total) or \
           (self.total == sys.float_info.max and 0 < t.monto):
            print("No se realizó la transacción. Límite del registo excedido.")
        elif t.monto < 0:
            print("No se realizó la transacción. Monto negativo.")
        else:
            self.trans.append(t)
            self.total += t.monto

class BilleteraElectronica:
    def __init__(self, ident, nombres, apellidos, ci, pin):
        self.id = ident
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = ci
        self.pin = pin
        self.creditos = Historial()
        self.debitos = Historial()
        
    def saldo(self):
        return self.creditos.total - self.debitos.total
    
    def recargar(self, monto, id_rest):
        self.creditos.agregarTransaccion(Transaccion(monto, id_rest))
        
    def consumir(self, monto, id_rest, pin):
        if pin == self.pin and monto <= self.saldo():
            self.debitos.agregarTransaccion(Transaccion(monto, id_rest))
        elif pin != self.pin:
            print("No se realizó la transacción, PIN incorrecto.")
        elif self.saldo() < monto:
            print("No se realizó la transacción, saldo insuficiente.")
            
        
        