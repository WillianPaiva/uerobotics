#######################################################################################
#  Copyright (C) Tue 18 Mar 2014 07:30:13 PM CET Author Willian Paiva                 #
#                                                                                     #
#  This program is free software: you can redistribute it and/or modify               #
#  it under the terms of the GNU General Public License as published by               #
#  the Free Software Foundation, either version 3 of the License, or                  #
#  (at your option) any later version.                                                #
#                                                                                     #
#  This program is distributed in the hope that it will be useful,                    #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of                     #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                      #
#  GNU General Public License for more details.                                       #
#                                                                                     #
#  You should have received a copy of the GNU General Public License                  #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.              #
#######################################################################################


from numpy import *


#create a basic DH matrix 
def denavit_start_matrix(alpha , theta, d, r):
    a = matrix([[cos(theta), -sin(theta)*cos(alpha), sin(theta)*sin(alpha), r*cos(theta)],
                [sin(theta), cos(theta)*cos(alpha), -cos(theta)*sin(alpha), r*sin(theta)],
                [0,          sin(alpha),             cos(alpha),               d        ],
                [0,                   0,                   0,                   1       ]])
    
    return a


#calculate the x - y - z based on given angles 
def f_kin(theta1, theta2, theta3):
    

    #transform degrees on radian 
    th1 = theta1 * pi/180
    th2 = theta2 * pi/180
    th3 = theta3 * pi/180

    # DH from base to axe R1
    r0 = denavit_start_matrix(0,0,0,41)
    
    # DH from axe R1 to the axe R2
    r1 = denavit_start_matrix((pi/2),(th1),-14.5,49)
    
    
    #calculates the distance between axes R2 and R3
    r_r2 = sqrt((60.5**2) +(23.5**2))

    #angle correction for theta2
    ang_r2 = arcsin(23.5/r_r2)

    # matrix from axe R2 to the axe R3
    r2 = denavit_start_matrix(0,(th2 -ang_r2 ) ,0,r_r2)
     
    
    #matrix from axe R3 to the center of the piece
    r3 = denavit_start_matrix(0,(th3 +ang_r2-(pi/2)),0,52)

    
    #matrix and angle correction for the last piece of the arm     
    r_r4 = sqrt((41**2) +(14.5**2))
    ang_r4 = arcsin(14.5/r_r4)
    r4 = denavit_start_matrix(0,ang_r4,0,41)
    
    

    b = matrix([[0],[0],[0],[1]])
    
    
    #convertion 
    final = r0*r1*r2*r3*r4*b
    
           
    
    x_tip = final.item(0)
    y_tip = final.item(1)
    z_tip = final.item(2)
    
    return x_tip, y_tip, z_tip
