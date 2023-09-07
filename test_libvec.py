import libvec as lc
import unittest
import numpy as np

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

    def test_adjunmat(self):
        mat1 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        sum_ver = [[(1 - 4j), (-4 - 2j), (2 - 14j)], [(-1 + 12j), (45 + 1j), (2 - 9j)], [(4 - 7j), (13 - 7j), (1 - 3j)]]
        sum_doc = lc.adjuntamat(mat1)
        self.assertEqual(sum_doc, sum_ver)

    def test_productmat(self):
        mat1 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        mat2 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        sum_ver = [[(-77 + 124j), (-65 - 505j), (30 - 121j)], [(-262 + 276j), (2015 + 87j), (554 + 328j)],
                   [(-120 + 10j), (240 + 380j), (-135 + 207j)]]
        sum_doc = lc.productmat(mat1, mat2)
        self.assertEqual(sum_doc, sum_ver)

    def test_accionmat(self):
        mat = [[2 + 4j, 3 - 2j], [4 - 8j, 5 + 1j]]
        vec = [1 + 6j, 2 - 9j]
        sum_ver = "[-34.-15.j  71.-27.j]"
        sum_doc = lc.accionmat(mat,vec)
        self.assertEqual(sum_doc, sum_ver)

    def test_productint(self):
        c1 = [1 + 5j, -4 - 9j]
        c2 = [1 + 5j, 5 + 17j]
        resp_verd = (109 - 103j)
        resp_doct = lc.produinterno(c1, c2)
        self.assertEqual(resp_doct, resp_verd)

    def test_normvec(self):
        c1 = [1 + 5j, -4 - 9j]
        resp_verd = 11.09
        resp_doct = lc.normvect(c1)
        self.assertEqual(resp_doct, resp_verd)

    def test_distvect(self):
        vec_1 = [7 + 3j]
        vec_2 = [1 - 5j]
        resp_verd = 10.0
        resp_doct = lc.distvect(vec_1, vec_2)
        self.assertEqual(resp_doct, resp_verd)

    def test_valprop(self):
        mat = [[1, 2, -1], [1, 0, 1],[4, -4, 5]]
        resp_verd = """los valores propios para esta matriz o vector son [3. 2. 1.] y los vectores son [[-0.23570226  0.43643578  0.40824829]
        [ 0.23570226 -0.21821789 -0.40824829]
        [ 0.94280904 -0.87287156 -0.81649658]]"""
        resp_doct = lc.valprop(mat)
        self.assertEqual(resp_doct,resp_verd)

    def test_matunita(self):
        mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        resp_verd = "Si es unitaria"
        resp_doct = lc.matunita(mat)
        self.assertEqual(resp_doct, resp_verd)

    def test_mat_hermitiana(self):
        mat = [[1, -1 - 12j, 4 + 7j], [-1 + 12j, 45, 13 + 7j], [4 - 7j, 13 - 7j, 1]]
        resp_verd = "Es hermimtiana"
        resp_doct = lc.mathermitiana(mat)
        self.assertEqual(resp_doct, resp_verd)

    def test_prodtensemat(self):
        mat1 = [[2, 3], [1, 4]]
        mat2 = [[5, 3, 2], [1, 0, 2], [-2, 5, 6]]
        resp_verd = [[10, 6, 4, 15, 9, 6], [2, 0, 4, 3, 0, 6], [-4, 10, 12, -6, 15, 18], [5, 3, 2, 20, 12, 8],[1, 0, 2, 4, 0, 8], [-2, 5, 6, -8, 20, 24]]
        resp_doct = lc.prodtensemat(mat1, mat2)
        self.assertEqual(resp_doct, resp_verd)



if __name__ == '__main__':
    unittest.main()