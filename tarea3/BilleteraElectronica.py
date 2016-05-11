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
        self.creditos = Historial()
        self.debitos = Historial()
        
    def saldo(self):
        return self.creditos.total - self.debitos.total
    
    def recargar(self, monto, fecha, id_rest):
        pass
        
        