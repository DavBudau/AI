import random
import decimal

prag=decimal.Decimal(0.0001)
c=decimal.Decimal(0.01) #constanta

def f(x):
    return 6*x**2-12*x+1

#trebuie facuta o functie ce calculeaza derivata folosind ecuatia definitiei derivatei f(x)=(f(x+h)-f(x))/h

def deriv_f(x):#trebuie facut o functie ce
    h=decimal.Decimal(0.0000000000000000000001) #infinitesimal
    return (f(x+h)-f(x))/h

xn=decimal.Decimal(random.randrange(1000))
while True:
    xn_n=xn-c*deriv_f(xn) #xn_n=urmatoarea valoare
    if abs(xn_n-xn)<prag:
        break
    xn=xn_n
    print(f(xn))

print("min f(x)=", f(xn))

def g(x,y):
    return x**2+2*y**2

#derivatele partiale
def deriv_g_x(x,y):
    h = decimal.Decimal(0.0000000000000000000001)
    return (g(x+h,y)-g(x,y))/h
def deriv_g_y(x,y):
    h = decimal.Decimal(0.0000000000000000000001)
    return (g(x,y+h)-g(x,y))/h

xn_x=decimal.Decimal(random.randrange(1000))
xn_y=decimal.Decimal(random.randrange(1000))
while True:
    xn_x_n= xn_x-c*deriv_g_x(xn_x, xn_y) #scuzati nu prea sunt inspirat cu numirea variabilelor: xn_x_n= urmatoarea valoare
    xn_y_n= xn_y-c*deriv_g_y(xn_x, xn_y)
    if abs(xn_x_n-xn_x)<prag and abs(xn_y_n-xn_y):
        break
    xn_x=xn_x_n
    xn_y=xn_y_n
    print(g(xn_x,xn_y))

print("min g(x,y)=", g(xn_x,xn_y))


#acelasi lucru ca inainte
def h(x,y):
    return (1-x)**2+100*(x-y**2)**2

#derivatele partiale
def deriv_h_x(x,y):
    h = decimal.Decimal(0.0000000000000000000001)
    return (g(x+h,y)-g(x,y))/h
def deriv_h_y(x,y):
    h = decimal.Decimal(0.0000000000000000000001)
    return (g(x,y+h)-g(x,y))/h

xn_x=decimal.Decimal(random.randrange(1000))
xn_y=decimal.Decimal(random.randrange(1000))
while True:
    xn_x_n= xn_x-c*deriv_h_x(xn_x, xn_y)
    xn_y_n= xn_y-c*deriv_h_y(xn_x, xn_y)
    if abs(xn_x_n-xn_x)<prag and abs(xn_y_n-xn_y):
        break
    xn_x=xn_x_n
    xn_y=xn_y_n
    print(h(xn_x,xn_y))

print("min h(x,y)=", h(xn_x,xn_y))

