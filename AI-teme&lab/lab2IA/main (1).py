import numpy as np

x=[2,1,2]
y=[1,-1,4]
lung_x=np.linalg.norm(x)
print("Lungimea vect. x=", lung_x)
lung_y=np.linalg.norm(y)
print("Lungimea vect. y=", lung_y)
produs_scalar=np.dot(x,y)
print("Produsul scalar al vectorilor x si y este egal cu:", produs_scalar)
cos=produs_scalar/(lung_y*lung_x)
print("Cosinusul unghiului: ", cos)


def clasi(c):
    if(np.sign(np.sum(c))==1):print("Clasa 1")
    else: print("Clasa 2")

p0=[-1,-1,-1]
p1=[-1,-1, 1]
p2=[-1, 1,-1]
p3=[ 1,-1,-1]
p4=[-1, 1, 1]
p5=[ 1,-1, 1]
p6=[ 1, 1,-1]
p7=[ 1, 1, 1]
print("Punctul p0",p0,end=" ")
clasi(p0)
print("Punctul p1",p1,end=" ")
clasi(p1)
print("Punctul p2",p2,end=" ")
clasi(p1)
print("Punctul p3",p3,end=" ")
clasi(p3)
print("Punctul p4",p4,end=" ")
clasi(p4)
print("Punctul p5",p5,end=" ")
clasi(p5)
print("Punctul p6",p6,end=" ")
clasi(p6)
print("Punctul p7",p7,end=" ")
clasi(p7)

o1_prec=1
o2_prec=1
o3_prec=1
while(1):
    o1=np.sign(o2_prec-o3_prec)
    o2=np.sign(o1_prec-o3_prec)
    o3=np.sign(-o1_prec-o2_prec)
    if(o1==o1_prec and o2==o2_prec and o3==o3_prec): break
    o1_prec=o1
    o2_prec=o2
    o3_prec=o3
print(o1," ",o2," ",o3)