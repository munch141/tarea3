'''
Created on May 11, 2016

@author: ricardo
'''
import unittest
from datetime import *
from BilleteraElectronica import *


class Test(unittest.TestCase):

    def testAgregarTransaccion(self):
        h = Historial()
        h.agregarTransaccion(Transaccion(1000, datetime(2016, 5, 11, 12, 0), 1))
        
        self.assertEquals(len(h.trans), 1)
        self.assertEquals(h.trans[len(h.trans)-1].monto, 1000)
        self.assertEquals(h.trans[len(h.trans)-1].fecha,
                          datetime(2016, 5, 11, 12, 0))
        self.assertEquals(h.trans[len(h.trans)-1].id_rest, 1)
        self.assertEquals(h.total, 1000)
        
    def testCalcularSaldo(self):
        b = BilleteraElectronica(1, "Ricardo", "Münch", 23073743, [1,2,3,4])
        b.credito.agregarTransaccion(Transaccion(
                                        1000,datetime(2016, 5, 11, 12, 0), 1))
        b.debito.agregarTransaccion(Transaccion(
                                        500, datetime(2016, 5, 11, 12, 30), 1))
        self.assertEqual(b.saldo(), 500)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()