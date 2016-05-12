# -*- coding: utf-8 -*-
'''
Created on May 11, 2016

Hecho por:
    Ricardo Münch. Carnet: 11-10684.
    Raquel Prado. Carnet: 11-10801.
'''
import unittest
import sys
from BilleteraElectronica import (BilleteraElectronica, Historial, Transaccion)

class Test(unittest.TestCase):

    def testAgregarTransaccion(self):
        '''
        Caso interior
        '''
        h = Historial()
        h.agregarTransaccion(Transaccion(1000, 1))
        
        self.assertEquals(len(h.trans), 1)
        self.assertEquals(h.trans[len(h.trans)-1].monto, 1000)
        self.assertEquals(h.trans[len(h.trans)-1].id_rest, 1)
        self.assertEquals(h.total, 1000)
        
    def testCalcularSaldo(self):
        '''
        Caso interior
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.creditos.agregarTransaccion(Transaccion(1000,1))
        b.debitos.agregarTransaccion(Transaccion(500, 1))
        self.assertEqual(b.saldo(), 500)
        
    def testRecargar(self):
        '''
        Caso interior
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.recargar(1000, 1)
        
        self.assertEquals(len(b.creditos.trans), 1)
        self.assertEquals(b.creditos.trans[len(b.creditos.trans)-1].monto, 1000)
        self.assertEquals(b.creditos.trans[len(b.creditos.trans)-1].id_rest, 1)
        self.assertEquals(b.creditos.total, 1000)

    def testConsumir(self):
        '''
        Caso interior
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.recargar(1000, 1)
        b.consumir(500, 1, 1234)
        
        self.assertEquals(len(b.debitos.trans), 1)
        self.assertEquals(b.debitos.trans[len(b.debitos.trans)-1].monto, 500)
        self.assertEquals(b.debitos.trans[len(b.debitos.trans)-1].id_rest, 1)
        self.assertEquals(b.debitos.total, 500)

    def testConsumirVerificarPIN(self):
        '''
        Caso interior
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.recargar(1000, 1)
        b.consumir(500, 1, 1234)
        b.consumir(500, 1, 0000)
        
        self.assertEquals(len(b.debitos.trans), 1)
        self.assertEquals(b.debitos.trans[len(b.debitos.trans)-1].monto, 500)
        self.assertEquals(b.debitos.trans[len(b.debitos.trans)-1].id_rest, 1)
        self.assertEquals(b.debitos.total, 500)
        
    def testConsumirVerificarCreditoSuficiente(self):
        '''
        Caso interior
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.recargar(1000, 1)
        b.consumir(500, 1, 1234)
        b.consumir(2000, 1, 1234)
        
        self.assertEquals(len(b.debitos.trans), 1)
        self.assertEquals(b.debitos.trans[len(b.debitos.trans)-1].monto, 500)
        self.assertEquals(b.debitos.trans[len(b.debitos.trans)-1].id_rest, 1)
        self.assertEquals(b.debitos.total, 500)
    
    def testAgregarTransaccionMonto0Total0(self):
        '''
        Caso esquina
        '''
        h = Historial()
        h.agregarTransaccion(Transaccion(0, 1))
        self.assertEquals(h.total, 0)
    
    def testAgregarTransaccionMontoInfTotal0(self):
        '''
        Caso esquina
        '''
        h = Historial()
        h.agregarTransaccion(Transaccion(sys.float_info.max, 1))
        self.assertEquals(h.total, sys.float_info.max)
    
    def testAgregarTransaccionMonto0TotalInf(self):
        '''
        Caso esquina
        '''
        h = Historial()
        h.total = sys.float_info.max
        h.agregarTransaccion(Transaccion(0, 1))
        self.assertEquals(h.total, sys.float_info.max)
        
    def testAgregarTransaccionMontoInfTotalInf(self):
        '''
        Caso esquina
        '''
        h = Historial()
        h.total = sys.float_info.max
        h.agregarTransaccion(Transaccion(sys.float_info.max, 1))
        self.assertEquals(h.total, sys.float_info.max)
    
    def testCalcularSaldoCredito0Debito0(self):
        '''
        Caso esquina
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        self.assertEqual(b.saldo(), 0)
    
    def testCalcularSaldoCreditoInfDebito0(self):
        '''
        Caso esquina
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.recargar(sys.float_info.max, 1) 
        self.assertEqual(b.saldo(), sys.float_info.max)
    
    def testCalcularSaldoCredito0DebitoInf(self):
        '''
        Caso esquina
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.consumir(sys.float_info.max, 1, 1234) 
        self.assertEqual(b.saldo(), 0)
    
    def testCalcularSaldoCreditoInfDebitoInf(self):
        '''
        Caso esquina
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.recargar(sys.float_info.max, 1)
        b.consumir(sys.float_info.max, 1, 1234) 
        self.assertEqual(b.saldo(), 0)
        
    def testRecargarMonto0Total0(self):    
        '''
        Caso esquina
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.recargar(0, 1)
        self.assertEqual(b.creditos.total, 0)
    
    def testRecargarMontoInfTotal0(self):
        '''
        Caso esquina
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.recargar(sys.float_info.max, 1)
        self.assertEqual(b.creditos.total, sys.float_info.max)
    
    def testRecargarMonto0TotalInf(self):
        '''
        Caso esquina
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.creditos.total = sys.float_info.max
        b.recargar(0, 1)
        self.assertEqual(b.creditos.total, sys.float_info.max)   
    
    def testRecargarMontoInfTotalInf(self):
        '''
        Caso esquina
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.creditos.total = sys.float_info.max
        b.recargar(sys.float_info.max, 1)
        self.assertEqual(b.creditos.total, sys.float_info.max)   
   
    def testConsumirMonto0Total0(self):
        '''
        Caso esquina
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.consumir(0, 1, 1234)
        self.assertEqual(b.debitos.total, 0)  
    
    def testConsumirMontoInfTotal0(self):
        '''
        Caso esquina
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.consumir(sys.float_info.max, 1, 1234)
        self.assertEqual(b.debitos.total, 0)
        
    def testConsumirMonto0TotalInf(self):
        '''
        Caso esquina
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.debitos.total = sys.float_info.max
        b.consumir(0, 1, 1234)
        self.assertEqual(b.debitos.total, sys.float_info.max)
        
    def testConsumirMontoInfTotalInf(self):
        '''
        Caso esquina
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.debitos.total = sys.float_info.max
        b.consumir(sys.float_info.max, 1, 1234)
        self.assertEqual(b.debitos.total, sys.float_info.max)
        
    def testAgregarTransaccionSumaMax1(self):
        '''
        Caso frontera
        '''
        h = Historial()
        h.agregarTransaccion(Transaccion(sys.float_info.max, 1))
        self.assertEqual(h.total, sys.float_info.max)
        
    def testAgregarTransaccionSumaMax2(self):
        '''
        Caso frontera
        '''
        h = Historial()
        h.total = sys.float_info.max
        h.agregarTransaccion(Transaccion(0, 1))
        self.assertEqual(h.total, sys.float_info.max)
        
    def testAgregarTransaccionSumaMayorQueMax1(self):
        '''
        Caso frontera
        '''
        h = Historial()
        h.total = sys.float_info.min
        h.agregarTransaccion(Transaccion(sys.float_info.max, 1))
        self.assertEqual(h.total, sys.float_info.min)

    def testAgregarTransaccionSumaMayorQueMax2(self):
        '''
        Caso frontera
        '''
        h = Historial()
        h.total = sys.float_info.max
        h.agregarTransaccion(Transaccion(sys.float_info.min, 1))
        self.assertEqual(h.total, sys.float_info.max)
        
    def testAgregarTransaccionSuma0(self):
        '''
        Caso frontera
        '''
        h = Historial()
        h.agregarTransaccion(Transaccion(0, 1))
        self.assertEqual(h.total, 0)
        
    def testAgregarTransaccionSumaMenorQue0A(self):
        '''
        Caso frontera
        '''
        h = Historial()
        h.agregarTransaccion(Transaccion(-sys.float_info.min, 1))
        self.assertEqual(h.total, 0)
        
    def testAgregarTransaccionSumaMenorQue0B(self):
        '''
        Caso malicioso
        '''
        h = Historial()
        h.total = -sys.float_info.min
        h.agregarTransaccion(Transaccion(100, 1))
        self.assertEqual(h.total, 100)
        
    def testSaldo0(self):
        '''
        Caso frontera
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.recargar(100, 1)
        b.consumir(100, 1, 1234)
        self.assertEqual(b.saldo(), 0)
        
    def testSaldoMenorQue0(self):
        '''
        Caso frontera
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.debitos.total = sys.float_info.min
        self.assertEqual(b.saldo(), 0)
    
    def testRecarga0(self):
        '''
        Caso frontera
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.recargar(0, 1)
        self.assertEqual(b.creditos.total, 0)
    
    def testRecargaMenorque0(self):
        '''
        Caso frontera
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.recargar(-sys.float_info.min, 1)
        self.assertEqual(b.creditos.total, 0)
        
    def testConsumirSaldoIgualMontoYPINCorrecto(self):
        '''
        Caso frontera
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.consumir(0, 1, 1234)
        self.assertEqual(b.debitos.total, 0)    
    
    def testConsumirPINInorrecto(self):
        '''
        Caso frontera
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.consumir(100, 1, 1284)
        self.assertEqual(b.debitos.total, 0) 
            
    def testConsumirSaldoMenorqueMontoPINCorrecto(self):
        '''
        Caso frontera
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.consumir(-sys.float_info.min, 1, 1234)
        self.assertEqual(b.debitos.total, 0)  
    
    def testRecargaTipoIncorrecto(self):
        '''
        Caso Malicioso
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.recargar("sdsd", 1)
        self.assertEqual(b.creditos.total, 0) 
    
    def testConsumirMontoIncorrectoPINCorrecta(self):
        '''
        Caso Malicioso
        '''
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, 1234)
        b.consumir("sdsd", 1,1234)
        self.assertEqual(b.creditos.total, 0) 
    
              
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()