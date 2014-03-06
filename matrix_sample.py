import sympy
import matrices

theta = sympy.Symbol("theta")
rx  = matrices.TRotX(theta).m
r_x = matrices.TRotX(-theta).m

print(rx*r_x)
print(sympy.trigsimp(rx*r_x) == sympy.Matrix.eye(4))