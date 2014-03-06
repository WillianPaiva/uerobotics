# uerobotics

Materials for the course "Introduction to Robotics" at the University of Bordeaux, France

## Course on Forward and Inverse Models

We will give you code to create symbolic transformation matrices. You will need sympy that you can install using:

    pip install sympy --user

The code can be used by creating scripts such as:

    import sympy
    import matrices

    theta = sympy.Symbol("theta")
    rx  = matrices.TRotX(theta).m
    r_x = matrices.TRotX(-theta).m

    print(rx*r_x)
    print(sympy.trigsimp(rx*r_x) == sympy.Matrix.eye(4))

For the forward model, you should produce a function:

    def f_kin(theta_0, theta_1, theta_2):
        ...
        return (x_tip, y_tip, z_tip)
