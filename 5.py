import numpy as np
import math as m
from scipy.optimize import fsolve
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D


L1=10
L2=2
L3=1
L4=0.50
L5=1.0
L1p=L2p=L3p=L4p=L5p=1.0
result=0

iteration_counter=0;
fig = pyplot.figure()
ax = Axes3D(fig)


# Lx meghdare feeli , Lxp meghdare ghabli m vaghti dige hichki taghir nakar vaysta  , L = Landa
while (L1 != L1p or L2 != L2p or L3 != L3p or L4 != L4p or L5 != L5p ) :

      print "t"
      L1p=L1
      L2p=L2
      L3p=L3
      L4p=L4
      L5p=L5
      print m.log(float(1)/float(L1+L5))+m.log(float(1)/float(L2+L4+L5))+m.log(float(1)/float(L3+L4+L5))+2*(L1+L2+L3+L4+2*L5)-8
      print "L1 = ", L1, "L2 = ", L2,"L3 = ", L3,"L4 = ", L4,"L5 = ", L5
      a= 2
      b= 2*L2+2*L3+4*L5-2
      c= 2*L2*L3+ 2*L2*L5+ 2*L5*L3+ 2*L5*L5- L3- L2- 2*L5
      L4temp = float(-b - m.sqrt((b*b)-(4*a*c)))/float(2*a)
      x=L4temp
      if(L4temp<0):
         L4temp=0
      if( m.log(float(1)/float(L1+L5))+m.log(float(1)/float(L2+L4temp+L5))+m.log(float(1)/float(L3+L4temp+L5))+2*(L1+L2+L3+L4temp+2*L5)-8) < result :
         L4=L4temp
      else :
         L4temp=2*L4-x
         if( m.log(float(1)/float(L1+L5))+m.log(float(1)/float(L2+L4temp+L5))+m.log(float(1)/float(L3+L4temp+L5))+2*(L1+L2+L3+L4temp+2*L5)-8) < result :
            L4=L4temp         
      
      result=m.log(float(1)/float(L1+L5))+m.log(float(1)/float(L2+L4+L5))+m.log(float(1)/float(L3+L4+L5))+2*(L1+L2+L3+L4+2*L5)-8
      print result
      print "L1 = ", L1, "L2 = ", L2,"L3 = ", L3,"L4 = ", L4,"L5 = ", L5

      R1 = float(1)/float(L1+L5)
      R2 = float(1)/float(L2+L4+L5)
      R3 = float(1)/float(L3+L4+L5)
      ax.bar3d(iteration_counter,1,0,0.5,0.5,L1,color='b', zsort='average')
      ax.bar3d(iteration_counter,2,0,0.5,0.5,L2,color='b', zsort='average')
      ax.bar3d(iteration_counter,3,0,0.5,0.5,L3,color='b', zsort='average')
      ax.bar3d(iteration_counter,4,0,0.5,0.5,L4,color='b', zsort='average')
      ax.bar3d(iteration_counter,5,0,0.5,0.5,L5,color='b', zsort='average')
      ax.bar3d(iteration_counter,6,0,0.5,0.5,R1,color='r', zsort='average')
      ax.bar3d(iteration_counter,7,0,0.5,0.5,R2,color='r', zsort='average')
      ax.bar3d(iteration_counter,8,0,0.5,0.5,R3,color='r', zsort='average')
      iteration_counter=iteration_counter+2
      
      
      L1temp = float(1-2*L5)/float(2)
      x=L1temp
      if(L1temp<0):
         L1temp=0
      if( m.log(float(1)/float(L1temp+L5))+m.log(float(1)/float(L2+L4+L5))+m.log(float(1)/float(L3+L4+L5))+2*(L1temp+L2+L3+L4+2*L5)-8) < result :
         L1=L1temp
      else :
         L1temp=2*L1-x
         if( m.log(float(1)/float(L1temp+L5))+m.log(float(1)/float(L2+L4+L5))+m.log(float(1)/float(L3+L4+L5))+2*(L1temp+L2+L3+L4+2*L5)-8) < result :
            L1=L1temp
            
      result=m.log(float(1)/float(L1+L5))+m.log(float(1)/float(L2+L4+L5))+m.log(float(1)/float(L3+L4+L5))+2*(L1+L2+L3+L4+2*L5)-8
      print result
      print "L1 = ", L1, "L2 = ", L2,"L3 = ", L3,"L4 = ", L4,"L5 = ", L5

      R1 = float(1)/float(L1+L5)
      R2 = float(1)/float(L2+L4+L5)
      R3 = float(1)/float(L3+L4+L5)
      ax.bar3d(iteration_counter,1,0,0.5,0.5,L1,color='b', zsort='average')
      ax.bar3d(iteration_counter,2,0,0.5,0.5,L2,color='b', zsort='average')
      ax.bar3d(iteration_counter,3,0,0.5,0.5,L3,color='b', zsort='average')
      ax.bar3d(iteration_counter,4,0,0.5,0.5,L4,color='b', zsort='average')
      ax.bar3d(iteration_counter,5,0,0.5,0.5,L5,color='b', zsort='average')
      ax.bar3d(iteration_counter,6,0,0.5,0.5,R1,color='r', zsort='average')
      ax.bar3d(iteration_counter,7,0,0.5,0.5,R2,color='r', zsort='average')
      ax.bar3d(iteration_counter,8,0,0.5,0.5,R3,color='r', zsort='average')
      iteration_counter=iteration_counter+2

      
      L2temp = float(1-2*L4-2*L5)/float(2)
      x=L2temp
      if(L2temp<0):
         L2temp=0
      if( m.log(float(1)/float(L1+L5))+m.log(float(1)/float(L2temp+L4+L5))+m.log(float(1)/float(L3+L4+L5))+2*(L1+L2temp+L3+L4+2*L5)-8) < result :
         L2=L2temp
      else :
         L2temp=2*L2-x
         if( m.log(float(1)/float(L1+L5))+m.log(float(1)/float(L2temp+L4+L5))+m.log(float(1)/float(L3+L4+L5))+2*(L1+L2temp+L3+L4+2*L5)-8) < result :
            L2=L2temp
         
      result=m.log(float(1)/float(L1+L5))+m.log(float(1)/float(L2+L4+L5))+m.log(float(1)/float(L3+L4+L5))+2*(L1+L2+L3+L4+2*L5)-8
      print result
      print "L1 = ", L1, "L2 = ", L2,"L3 = ", L3,"L4 = ", L4,"L5 = ", L5

      R1 = float(1)/float(L1+L5)
      R2 = float(1)/float(L2+L4+L5)
      R3 = float(1)/float(L3+L4+L5)
      ax.bar3d(iteration_counter,1,0,0.5,0.5,L1,color='b', zsort='average')
      ax.bar3d(iteration_counter,2,0,0.5,0.5,L2,color='b', zsort='average')
      ax.bar3d(iteration_counter,3,0,0.5,0.5,L3,color='b', zsort='average')
      ax.bar3d(iteration_counter,4,0,0.5,0.5,L4,color='b', zsort='average')
      ax.bar3d(iteration_counter,5,0,0.5,0.5,L5,color='b', zsort='average')
      ax.bar3d(iteration_counter,6,0,0.5,0.5,R1,color='r', zsort='average')
      ax.bar3d(iteration_counter,7,0,0.5,0.5,R2,color='r', zsort='average')
      ax.bar3d(iteration_counter,8,0,0.5,0.5,R3,color='r', zsort='average')
      iteration_counter=iteration_counter+2

      
      L3temp = float(1-2*L4-2*L5)/float(2)
      x=L3temp
      if(L3temp<0):
         L3temp=0
      if( m.log(float(1)/float(L1+L5))+m.log(float(1)/float(L2+L4+L5))+m.log(float(1)/float(L3temp+L4+L5))+2*(L1+L2+L3temp+L4+2*L5)-8) < result :
         L3=L3temp
      else :
         L3temp=2*L3-x
         if( m.log(float(1)/float(L1+L5))+m.log(float(1)/float(L2+L4+L5))+m.log(float(1)/float(L3temp+L4+L5))+2*(L1+L2+L3temp+L4+2*L5)-8) < result :
            L3=L3temp
         
      result=m.log(float(1)/float(L1+L5))+m.log(float(1)/float(L2+L4+L5))+m.log(float(1)/float(L3+L4+L5))+2*(L1+L2+L3+L4+2*L5)-8
      print result
      print "L1 = ", L1, "L2 = ", L2,"L3 = ", L3,"L4 = ", L4,"L5 = ", L5

      R1 = float(1)/float(L1+L5)
      R2 = float(1)/float(L2+L4+L5)
      R3 = float(1)/float(L3+L4+L5)
      ax.bar3d(iteration_counter,1,0,0.5,0.5,L1,color='b', zsort='average')
      ax.bar3d(iteration_counter,2,0,0.5,0.5,L2,color='b', zsort='average')
      ax.bar3d(iteration_counter,3,0,0.5,0.5,L3,color='b', zsort='average')
      ax.bar3d(iteration_counter,4,0,0.5,0.5,L4,color='b', zsort='average')
      ax.bar3d(iteration_counter,5,0,0.5,0.5,L5,color='b', zsort='average')
      ax.bar3d(iteration_counter,6,0,0.5,0.5,R1,color='r', zsort='average')
      ax.bar3d(iteration_counter,7,0,0.5,0.5,R2,color='r', zsort='average')
      ax.bar3d(iteration_counter,8,0,0.5,0.5,R3,color='r', zsort='average')
      iteration_counter=iteration_counter+2

      
      def func(L5):
          return (float(1)/float(L5+L1))+(float(1)/float(L5+L2+L4))+(float(1)/float(L5+L3+L4))-4
      L5temp = float(fsolve(func, 0.5))
      x=L5temp
      if(L5temp<0):
         L5temp=0
      if( m.log(float(1)/float(L1+L5temp))+m.log(float(1)/float(L2+L4+L5temp))+m.log(float(1)/float(L3+L4+L5temp))+2*(L1+L2+L3+L4+2*L5temp)-8) < result :
         L5=L5temp
      else :
         L5temp=2*L5-x
         if( m.log(float(1)/float(L1+L5temp))+m.log(float(1)/float(L2+L4+L5temp))+m.log(float(1)/float(L3+L4+L5temp))+2*(L1+L2+L3+L4+2*L5temp)-8) < result :
            L5=L5temp
        
      result=m.log(float(1)/float(L1+L5))+m.log(float(1)/float(L2+L4+L5))+m.log(float(1)/float(L3+L4+L5))+2*(L1+L2+L3+L4+2*L5)-8
      print result
      print "L1 = ", L1, "L2 = ", L2,"L3 = ", L3,"L4 = ", L4,"L5 = ", L5

      R1 = float(1)/float(L1+L5)
      R2 = float(1)/float(L2+L4+L5)
      R3 = float(1)/float(L3+L4+L5)
      ax.bar3d(iteration_counter,1,0,0.5,0.5,L1,color='b', zsort='average')
      ax.bar3d(iteration_counter,2,0,0.5,0.5,L2,color='b', zsort='average')
      ax.bar3d(iteration_counter,3,0,0.5,0.5,L3,color='b', zsort='average')
      ax.bar3d(iteration_counter,4,0,0.5,0.5,L4,color='b', zsort='average')
      ax.bar3d(iteration_counter,5,0,0.5,0.5,L5,color='b', zsort='average')
      ax.bar3d(iteration_counter,6,0,0.5,0.5,R1,color='r', zsort='average')
      ax.bar3d(iteration_counter,7,0,0.5,0.5,R2,color='r', zsort='average')
      ax.bar3d(iteration_counter,8,0,0.5,0.5,R3,color='r', zsort='average')
      iteration_counter=iteration_counter+2

      
#      print "L1 = ", L1, "L2 = ", L2,"L3 = ", L3,"L4 = ", L4,"L5 = ", L5
#      print "L1p = ", L1p, "L2p = ", L2p,"L3p = ", L3p,"L4p = ", L4p,"L5p = ", L5p
      print "R1 = ", float(1)/float(L1+L5), "R2 = ",float(1)/float(L2+L4+L5),"R3 = ",float(1)/float(L3+L4+L5)
      wait = raw_input("PRESS ENTER TO CONTINUE.")

      if(L1 != L1p or L2 != L2p or L3 != L3p or L4 != L4p or L5 != L5p):
            break
      
     

print "L1 = ", L1, "L2 = ", L2,"L3 = ", L3,"L4 = ", L4,"L5 = ", L5
print "L1p = ", L1p, "L2p = ", L2p,"L3p = ", L3p,"L4p = ", L4p,"L5p = ", L5p

ax.set_xlabel('Iteration Number axis')
ax.set_ylabel('Lagrange Multipliers & Flow Rates')
ax.set_zlabel('Variable Value')
pyplot.show()
