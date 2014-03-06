# uerobotics

Materials for the course "Introduction to Robotics" at the University of Bordeaux, France 

## Course on Forward and Inverse model

We will give you code to create symbolic transformation matrices. You will need sympy that you can install using:

    pip install sympy --user
  
The code can be used by creating scripts such as:

    import sympy
    import matrices
    
    theta = sympy.Symbol("theta")
    rx  = matrices.TRotX(theta)
    r_x = matrices.TRotY(-theta)
    
    print(rx*r_x == sympy.Matrix.eye(4))
