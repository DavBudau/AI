import numpy as np

w=np.array([1,-1,0,0.5]) #ponderi initiale

x1=np.array([1,-2,1.5,0])
x2=np.array([1,-0.5,-2,-1.5])
x3=np.array([0,1,-1,1.5])

#Se aplica x1
net1=np.dot(w,x1)
print("valoare de activare este:", net1)
w1=w+np.sign(net1)*x1 #formula data in curs
print("w1=",w1)

#Se aplica x2
net2=np.dot(w1,x2)
print("valoare de activare este:", net2)
w2=w1+np.sign(net2)*x2 #formula data in curs
print("w2=",w2)

#Se aplica x3
net3=np.dot(w2,x3)
print("valoare de activare este:", net3)
w3=w2+np.sign(net3)*x3 #formula data in curs
print("w3=",w3)

print("\nA iesit ca in curs sunt smecher\n")

#Se aplica x^1
fun=2/(1+np.exp(-net1))-1
print("functia de activare:",fun)
w1=w+fun*x1
print("w1=", w1)

#Se aplica x^2
net2=np.dot(w1,x2)
fun=2/(1+np.exp(-net2))-1
print("functia de activare:",fun)
w2=w1+fun*x2
print("w2=", w2)

#Se aplica x^3
net3=np.dot(w2,x3)
fun=2/(1+np.exp(-net3))-1
print("functia de activare:",fun)
w3=w2+fun*x3
print("w3=", w3)

print("\nFoarte frumos, foarte frumos, primul exercitiu gata. Bravooo!\n")

print("\nAl doilea exercitiu, foarte frumos, foarte frumos.\n")

w=np.array([1,-1])
x1=np.array([1,-2])
x2=np.array([0,1])
x3=np.array([2,3])
x4=np.array([1,-1])

#Se aplica x1
net1=np.dot(w,x1)
print("valoare de activare este:", net1)
w1=w+np.sign(net1)*x1 #formula data in curs
print("w1=",w1)

#Se aplica x2
net2=np.dot(w1,x2)
print("valoare de activare este:", net2)
w2=w1+np.sign(net2)*x2 #formula data in curs
print("w2=",w2)

#Se aplica x3
net3=np.dot(w2,x3)
print("valoare de activare este:", net3)
w3=w2+np.sign(net3)*x3 #formula data in curs
print("w3=",w3)

#Se aplica x4
net4=np.dot(w3,x4)
print("valoare de activare este:", net4)
w4=w3+np.sign(net4)*x4 #formula data in curs
print("w4=",w4)

print("\nAm dat copy paste la codul anterior, foarte frumos, foarte frumos\n")

#Se aplica x^1
fun=2/(1+np.exp(-net1))-1
print("functia de activare:",fun)
w1=w+fun*x1
print("w1=", w1)

#Se aplica x^2
net2=np.dot(w1,x2)
fun=2/(1+np.exp(-net2))-1
print("functia de activare:",fun)
w2=w1+fun*x2
print("w2=", w2)

#Se aplica x^3
net3=np.dot(w2,x3)
fun=2/(1+np.exp(-net3))-1
print("functia de activare:",fun)
w3=w2+fun*x3
print("w3=", w3)

#Se aplica x^4
net4=np.dot(w3,x4)
fun=2/(1+np.exp(-net4))-1
print("functia de activare:",fun)
w4=w3+fun*x4
print("w4=", w4)

print("\nGata tema, foarte frumos, foarte frumos.\n")



