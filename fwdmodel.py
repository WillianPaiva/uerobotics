from numpy import *



def denavit_start_matrix(alpha , theta, d, r):
    a = matrix([[cos(theta), -sin(theta)*cos(alpha), sin(theta)*sin(alpha), r*cos(theta)],
                [sin(theta), cos(theta)*cos(alpha), -cos(theta)*sin(alpha), r*sin(theta)],
                [0,          sin(alpha),             cos(alpha),               d        ],
                [0,                   0,                   0,                   1       ]])
    
    return a

def f_kin(theta1, theta2, theta3):
    
    th1 = theta1 * pi/180
    th2 = theta2 * pi/180
    th3 = theta3 * pi/180

    
    r0 = denavit_start_matrix(0,0,0,41)
    
    
    r_r1 = sqrt((49**2) +(14.5**2))
    r1 = denavit_start_matrix((pi/2),(th1),-14.5,49)
    
    
    
    r_r2 = sqrt((60.5**2) +(23.5**2))
    ang_r2 = arcsin(23.5/r_r2)
    r2 = denavit_start_matrix(0,(th2 -ang_r2 ) ,0,r_r2)
    
    
    
   
    r3 = denavit_start_matrix(0,(th3 +ang_r2-(pi/2)),0,52)
    r_r4 = sqrt((41**2) +(14.5**2))
    ang_r4 = arcsin(14.5/r_r4)
    
    r4 = denavit_start_matrix(0,ang_r4,0,41)
    
    
    b = matrix([[0],[0],[0],[1]])
    
    
    
    final = r0*r1*r2*r3*r4*b
    
           
    
    x_tip = final.item(0)
    y_tip = final.item(1)
    z_tip = final.item(2)
    
    return x_tip, y_tip, z_tip
