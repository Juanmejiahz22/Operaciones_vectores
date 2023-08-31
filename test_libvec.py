import libvec as lc
import unittest

class TestCplxOperations(unittest.TestCase):

    def test_sumveccplx(self):
        suma = lc.sumaveccplx((5,3),(9,2))
        self.assertAlmostEqual(suma[0],14)
        self.assertAlmostEqual(suma[1],5)
    
    def test2_sumveccplx(self):
        suma = lc.sumaveccplx((-3,10),(7,3))
        self.assertAlmostEqual(suma[0],4)
        self.assertAlmostEqual(suma[1],13)
    
    def test_inverveccplx(self):
        inver = lc.inverveccplx((2,7))
        self.assertAlmostEqual(inver[0],-2)
        self.assertAlmostEqual(inver[1],-7)

    def test2_inverveccplx(self):
        inver = lc.inverveccplx((-5,-2))
        self.assertAlmostEqual(inver[0],5)
        self.assertAlmostEqual(inver[1],2)

    def test_multiescalcplx(self):
        multi = lc.multiescalcplx((2),(-3,4))
        self.assertAlmostEqual(multi[0],-6)
        self.assertAlmostEqual(multi[1],8)

    def test2_multiescalcplx(self):
        multi = lc.multiescalcplx((-5),(2,-6))
        self.assertAlmostEqual(multi[0],-10)
        self.assertAlmostEqual(multi[1],30)

    def test_sumamatcplx(self):
        suma = lc.sumamatcplx(([[1,2],[3,4]]),([[5,6],[7,8]]))
        self.assertAlmostEqual(suma[0],6)
        self.assertAlmostEqual(suma[1],8)
        self.assertAlmostEqual(suma[2],10)
        self.assertAlmostEqual(suma[3],12)
    
    def test2_sumamatcplx(self):
        suma = lc.sumamatcplx(([[5,-3],[-7,10]]),([[3,2],[-2,2]]))
        self.assertAlmostEqual(suma[0],8)
        self.assertAlmostEqual(suma[1],-1)
        self.assertAlmostEqual(suma[2],-9)
        self.assertAlmostEqual(suma[3],12)

    def test_invermatcplx(self):
        inver = lc.invermatcplx(([[1,2],[3,4]]))
        self.assertAlmostEqual(inver[0],-1)
        self.assertAlmostEqual(inver[1],-2)
        self.assertAlmostEqual(inver[2],-3)
        self.assertAlmostEqual(inver[3],-4)
    
    def test2_invermatcplx(self):
        inver = lc.invermatcplx(([[6,7],[4,6]]))
        self.assertAlmostEqual(inver[0],-6)
        self.assertAlmostEqual(inver[1],-7)
        self.assertAlmostEqual(inver[2],-4)
        self.assertAlmostEqual(inver[3],-6)
    
    def test_multimatcplx(self):
        mult = lc.multimatcplx((5),([[1,2],[3,4]]))
        self.assertAlmostEqual(mult[0],5)
        self.assertAlmostEqual(mult[1],10)
        self.assertAlmostEqual(mult[2],15)
        self.assertAlmostEqual(mult[3],20)
    
    def test2_multimatcplx(self):
        mult = lc.multimatcplx((2),([[5,2],[7,6]]))
        self.assertAlmostEqual(mult[0],10)
        self.assertAlmostEqual(mult[1],4)
        self.assertAlmostEqual(mult[2],14)
        self.assertAlmostEqual(mult[3],12)

    def test_transmatcplx(self):
        trans = lc.transmatcplx([[1,2],[3,4]])
        self.assertAlmostEqual(trans[0][0],1)
        self.assertAlmostEqual(trans[0][1],3)
        self.assertAlmostEqual(trans[1][0],2)
        self.assertAlmostEqual(trans[1][1],4)

    def test2_transmatcplx(self):
        trans = lc.transmatcplx([[3,6],[6,4]])
        self.assertAlmostEqual(trans[0][0],3)
        self.assertAlmostEqual(trans[0][1],6)
        self.assertAlmostEqual(trans[1][0],6)
        self.assertAlmostEqual(trans[1][1],4)
    
    def test_conjumat(self):
        conj = lc.conjumat(2 + 4j)
        self.assertAlmostEqual(conj,2 - 4j)

    def test2_conjumat(self):
        conj = lc.conjumat(2 - 4j)
        self.assertAlmostEqual(conj,2 + 4j)



if __name__ == '__main__':
    unittest.main()