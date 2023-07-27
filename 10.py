import numpy as np
import math as m
finaloutput=-10
for x1 in np.arange(0.00,2.0,0.01):
   for x2 in np.arange(0.00,2.0,0.01):
       for x3 in np.arange(0.00,2.0,0.01):
            if(0<x1 <2 and 0<x2 <2 and 0<x3 <2 and (x1+x2+x3)<4 and x2+x3<2 ):
                output = m.log(3*x1+x2+x3)+m.log(x1+5*x2+3*x3)+m.log(x1+3*x2+5*x3)- float(2)/(2-x1)**2 - float(2)/(2-x2)**2 - float(2)/(2-x3)**2 - float(2)/(2-x2-x3)**2 - float(1)/(4-x1-x2-x3)**2 
                #print output
                if (output>finaloutput):
                   finalx1=x1
                   finalx2=x2
                   finalx3=x3
                   finaloutput=output

print "x1 = ", finalx1, "x2 = ", finalx2 , "x3 = ", finalx3 , "Final Output = " , finaloutput

