# Напишите программу cubic.py, которая принимает три параметра a,b,c и вычисляет корни уравнения x^3+a*x^2+b*x+c=0
# используя формулы Виета. Обратите внимание, что в некоторых случаях корни представляют собой комплексные числа,
# а в самих формулах активно используются (прямые и обратные) гиперболические функции, а также функция sgn(x).

import sys
from math import *
import cmath
import numpy as np
a, b, c = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])

q = (3*b-a**2)/9
r = (9*a*b-2*a**3-27*c)/54
s = q**3+r**2

if s > 0 :
	phi = (1/3)*cmath.acos(r/cmath.sqrt((-q)**3))
	x1 = 2*cmath.sqrt(-q)*cos(phi) - a/3
	x2 = 2*cmath.sqrt(-q)*cmath.cos(phi+(2/3)*pi) - a/3
	x3 = 2*cmath.sqrt(-q)*cmath.cos(phi-(2/3)*pi) - a/3
elif (s < 0):
	if q > 0:
		phi = (1/3)*acosh(abs(r)/(sqrt(q**3)))
		x1 = -2*np.sign(r)*sqrt(q)*cosh(phi) - a/3
		x2 = np.sign(r)*cmath.sqrt(q)*cosh(phi) - a/3 + complex(0,1)*sqrt(3)*cmath.sqrt(q)*sinh(phi)
		x3 = np.sign(r)*cmath.sqrt(q)*cosh(phi) - a/3 - complex(0,1)*sqrt(3)*cmath.sqrt(q)*sinh(phi)
	elif q < 0:
		phi = (1/3)*asinh(abs(r)/(sqrt(abs(q)**3)))	
		x1 = -2*np.sign(r)*sqrt(abs(q))*sinh(phi) - a/3
		x2 = np.sign(r)*cmath.sqrt(abs(q))*sinh(phi) - a/3 + complex(0,1)*sqrt(3)*cmath.sqrt(abs(q))*cosh(phi)
		x3 = np.sign(r)*cmath.sqrt(abs(q))*sinh(phi) - a/3 - complex(0,1)*sqrt(3)*cmath.sqrt(abs(q))*cosh(phi)
	else:
		x1 = -1*np.cbrt(c-(a**3)/27)-a/3
		x2 = -(a+x1)/2+(complex(0,1)/2)*cmath.sqrt(abs((a-3*x1)*(a+x1)-4*b))
		x3 = -(a+x1)/2-(complex(0,1)/2)*cmath.sqrt(abs((a-3*x1)*(a+x1)-4*b))
else:
	x1 = -2*np.sign(r)*sqrt(q) - a/3
	x2 = np.sign(r)*sqrt(q) - a/3
	x3 = x2
print(x1, " ", x2, " ", x3)
	
 



	
