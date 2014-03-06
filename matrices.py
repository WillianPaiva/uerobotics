import sympy
from sympy import cos, sin

def deblock(m):
    m2 = sympy.Matrix(m.shape[0], m.shape[1], lambda i,j:0)
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            m2[i, j] = m[i, j]
    return m2


def print_matrix(m):
    m_print = [["" for _ in range(m.shape[1])] for _ in range(m.shape[0])]
    for j in range(m.shape[1]):
        col_width = max(len(m[i,j].__repr__()) for i in range(m.shape[0]))
        for i in range(m.shape[0]):
            m_print[i][j] = m[i,j].__repr__().rjust(col_width)

    for i in range(m.shape[0]):
        print('{}[{}]{}'.format('[' if i == 0 else ' ',
                                ',  '.join(e for e in m_print[i]),
                                ']' if i == m.shape[0] - 1 else ',',))


class RotX(object):
    """X rotation matrix"""

    def __init__(self, theta):
        #assert isinstance(theta, sympy.Symbol)
        self.theta  = theta
        self.m = sympy.Matrix([[1,          0,           0],
                               [0, cos(theta), -sin(theta)],
                               [0, sin(theta),  cos(theta)]])


class RotY(object):
    """Y rotation matrix"""

    def __init__(self, theta):
        #assert isinstance(theta, sympy.Symbol)
        self.theta  = theta
        self.m = sympy.Matrix([[ cos(theta), 0, sin(theta)],
                               [          0, 1,          0],
                               [-sin(theta), 0, cos(theta)]])


class RotZ(object):
    """Z rotation matrix"""

    def __init__(self, theta):
        #assert isinstance(theta, sympy.Symbol)
        self.theta  = theta
        self.m = sympy.Matrix([[cos(theta), -sin(theta), 0],
                               [sin(theta),  cos(theta), 0],
                               [         0,           0, 1]])

class TRotX(object):
    """Transformation matrice for a X rotation"""
    def __init__(self, theta):
        self.theta  = theta
        self.m = deblock(sympy.BlockMatrix([[RotX(theta).m, sympy.Matrix([[0, 0, 0]]).T],
                                            [sympy.Matrix([[0, 0, 0, 1]]), sympy.Matrix([[1]])]]))

class TRotY(object):
    """Transformation matrice for a Y rotation"""
    def __init__(self, theta):
        self.theta  = theta
        self.m = deblock(sympy.BlockMatrix([[RotY(theta).m, sympy.Matrix([[0, 0, 0]]).T],
                                            [sympy.Matrix([[0, 0, 0, 1]]), sympy.Matrix([[1]])]]))

class TRotZ(object):
    """Transformation matrice for a Z rotation"""
    def __init__(self, theta):
        self.theta  = theta
        self.m = deblock(sympy.BlockMatrix([[RotZ(theta).m, sympy.Matrix([[0, 0, 0]]).T],
                                            [sympy.Matrix([[0, 0, 0, 1]]), sympy.Matrix([[1]])]]))

class TTransX(object):
    """Transformation matrice for a X translation"""
    def __init__(self, a):
        self.a  = a
        self.m = deblock(sympy.BlockMatrix([[sympy.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), sympy.Matrix([[a, 0, 0]]).T],
                                            [sympy.Matrix([[0, 0, 0, 1]]), sympy.Matrix([[1]])]]))

class TTransY(object):
    """Transformation matrice for a Y translation"""
    def __init__(self, a):
        self.a  = a
        self.m = deblock(sympy.BlockMatrix([[sympy.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), sympy.Matrix([[0, a, 0]]).T],
                                            [sympy.Matrix([[0, 0, 0, 1]]), sympy.Matrix([[1]])]]))

class TTransZ(object):
    """Transformation matrice for a Y translation"""
    def __init__(self, a):
        self.a  = a
        self.m = deblock(sympy.BlockMatrix([[sympy.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), sympy.Matrix([[0, 0, a]]).T],
                                            [sympy.Matrix([[0, 0, 0, 1]]), sympy.Matrix([[1]])]]))

class HomMatrix(object):
    """Homogeneous transformation matrix, define the caracteristic of the robot joint."""

    def __init__(self, alpha, a, d, theta):
        """
            :param alpha: (always a constant)
            :param a:     (always a constant) - also called r.
            :param d:     (fixed for revolute joints)
            :param theta: (fixed for prismatic joints)
            For further details, consult :
            Section 1.5 "Workspace" of chapter 1 "Kinematics" in Springer Handbook of Robotics, or
            Virtual Robot Arm Control Model, by D.N.D. Kotteg, Proceedings of the Technical Sessions, 20 (2004) 7-14
            Video : http://www.youtube.com/watch?v=rA9tm0gTln8
        """
        self.t = sympy.Matrix([[a*cos(theta)], [a*sin(theta)], [d]])
        self.r = RotZ(theta).m*RotX(alpha).m
        self.m = deblock(sympy.BlockMatrix([[self.r, self.t],
                                            [sympy.Matrix([[0, 0, 0, 1]]), sympy.Matrix([[1]])]]))
        self.m_1 = deblock(sympy.BlockMatrix([[self.r.T, -self.r.T*self.t],
                                            [sympy.Matrix([[0, 0, 0, 1]]), sympy.Matrix([[1]])]]))

