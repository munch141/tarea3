'''
Created on May 11, 2016

@author: ricardo
'''
import unittest
from datetime import *
from BilleteraElectronica import *


class Test(unittest.TestCase):

    def testAgregarTransaccion(self):
        t = Transaccion(1000, datetime(2016, 5, 11, 12, 0), 1)
        h = Historial()
        h.agregarTransaccion(t)
        
        self.assertEquals(len(h.trans), 1)
        self.assertEquals(h.trans[len(h.trans)-1].monto, 1000)
        self.assertEquals(h.trans[len(h.trans)-1].fecha,
                          datetime(2016, 5, 11, 12, 0))
        self.assertEquals(h.trans[len(h.trans)-1].id_rest, 1)
        self.assertEquals(h.total, 1000)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()