from __future__ import print_function, division

import unittest
import sympy

import matrices

class TestMatrices(unittest.TestCase):

    def test_hm_inverse_x_sorting(self):

        theta = sympy.Symbol('theta')
        alpha = sympy.Symbol('alpha')
        r = sympy.Symbol('r')
        d = sympy.Symbol('d')

        hm = matrices.HomMatrix(alpha, r, d, theta)

        self.assertEqual(sympy.trigsimp(hm.m*hm.m_1), sympy.Matrix.eye(4))

    def test_transformation(self):

        theta = sympy.Symbol('theta')
        trans   = matrices.TTransX( theta)
        trans_1 = matrices.TTransX(-theta)
        self.assertEqual(sympy.trigsimp(trans.m*trans_1.m), sympy.Matrix.eye(4))

        rot   = matrices.TRotX( theta)
        rot_1 = matrices.TRotX(-theta)
        self.assertEqual(sympy.trigsimp(rot.m*rot_1.m), sympy.Matrix.eye(4))
