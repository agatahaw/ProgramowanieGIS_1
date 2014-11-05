# -*- coding: utf-8 -*-
import math 

def delta(a,b,c): 
    return b**2-4*a*c 

def miejsca_zerowe(a,b,c): 
    d = delta(a,b,c) 
    if d>0: 
        x1=(-float(b)-math.sqrt(d))/(2.0*float(a)) 
        x2=(-float(b)+math.sqrt(d))/(2.0*float(a)) 
        return (x1,x2) 
    elif d<0: 
        return None 
    else: 
        x=-b/(2*a) 
        return (x)

def kwadratowa(a,b,c,x): 
    return a*x**2+b*x+c


print "miejsca zerowe:" + str(miejsca_zerowe(1,-2,-8))
for x in xrange(-10,11):
    print "wartosc funkcji dla x= " +str(x) +"  wynosi  " + str(kwadratowa(1,-2,-8,x))