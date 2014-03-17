from __future__ import print_function, division
import unittest
import math

from fwdmodel import f_kin

# acceptable error in mm
ERROR_MARGIN = 10

# all possible orientations for angles
# [1, 1, 1] is the same a the motors orientation
possible_orientations = (( 1,  1,  1),
                         ( 1,  1, -1),
                         ( 1, -1,  1),
                         ( 1, -1, -1),
                         (-1,  1,  1),
                         (-1,  1, -1),
                         (-1, -1,  1),
                         (-1, -1, -1))

def detect_orientation():
    """
    Detect the orientation of the angles on a few simple cases
    Note that if f_kin is wrong, this can cause the orientation
    to be improperly detected.
    """
    x0, y0, z0 = f_kin(0, 0, 0)
    x1, y1, z1 = f_kin(math.pi/2, 0, 0)
    x2, y2, z2 = f_kin(0, math.pi/2, 0)
    x3, y3, z3 = f_kin(0, 0, math.pi/2)
    ori0 = int(math.copysign(1, y1))
    ori1 = int(math.copysign(1, z0-z2))
    ori2 = int(math.copysign(1, z3-z0))

    orientation = (ori0, ori1, ori2)
    print("detected orientation: {}".format(orientation))
    return orientation

# replace function call by values if you know them/want to force them.
actual_orientation = detect_orientation()

def reorient(theta1, theta2, theta3):
    ori1, ori2, ori3 = actual_orientation
    return f_kin(ori1*theta1, ori2*theta2, ori3*theta3)

def close_enough(p, p2):
    return sum((p_i-p2_i)**2 for p_i, p2_i in zip(p, p2)) < ERROR_MARGIN

class TestForwardModel(unittest.TestCase):

    def test_zero(self):
        self.assertTrue(close_enough(f_kin(0, 0, 0), (164, 0, -130)))

    def test_simple(self):
        self.assertTrue(close_enough(reorient(90,  0,  0), ( 41.0, 122.5, -130.0)))
        self.assertTrue(close_enough(reorient( 0, 90,  0), (-25.0,   0.0,  -88.0)))
        self.assertTrue(close_enough(reorient( 0,  0, 90), (243.5,   0.0,  -23.5)))

if __name__ == '__main__':
    unittest.main()
