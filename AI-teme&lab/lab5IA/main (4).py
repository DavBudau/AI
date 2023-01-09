import numpy as np

x=np.array([[45,85],[50,43],[40,80],[55,42],[200,43],[48,40],[195,41],[43,87],[190,40]]) #pattern
w=np.array([[186,51],[84 ,40],[48,50]]) #prototipuri

c=0.8
epoci=5
prot=[]
for k in range(epoci):
    for i in range(np.size(x,0)):
        for j in range(np.size(w,0)):
            p=np.sqrt((x[i][0]-w[j][0])**2+(x[i][1]-w[j][1])**2) #norma folosind formula
            prot.append(p) #bagam frumusel in vector
        poz_min=np.argmin(prot) #cautam pozitia minimului
        w[poz_min]=w[poz_min]+c*(x[i]-w[poz_min]) #foarte frumos folosim formula
        prot.clear()
print("w nou=",w,"\n")

for i in range(np.size(x,0)):
    for j in range(np.size(w,0)):
        p=np.sqrt((x[i][0]-w[j][0])**2+(x[i][1]-w[j][1])**2)
        prot.append(p)
    poz_min=np.argmin(prot)
    prot.clear()
    print(x[i],"este asociat lui",w[poz_min],"\n")

