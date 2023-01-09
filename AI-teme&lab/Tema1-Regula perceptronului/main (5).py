#sa folosit de la pagina 49 exercitiul 8
#sa folosit exemplu de la 46
#oleaca seamana cu hebb, parerea mea
import numpy as np

w=[0,1,0] #la pondair cum zice englezu

x1=[2,1,-1] #vectorii de intrare
x2=[0,-1,-1]

c=1
#supervizorii
d1=-1
d2=1

net= np.dot(w, x1) #se calculeaaza dot productu frumos acolo
print("net=", net)
semn=np.sign(net) #care-i semnu frate? aici e 1 cum ar veni
if semn!=d1: #verification fur le corection
    for i in range(0,3):
        r=d1-semn
        w[i]=w[i]+c*r*x1[i] #s-a dat formula alhamdulillah
    print("ponderile dupa corectie:", w)



net= np.dot(w, x2) #se calculeaaza dot productu frumos acolo
print("net=", net)
semn=np.sign(net) #care-i semnu frate?
if semn!=d2: #verification fur le corection
    for i in range(0,3):
        r=d2-semn
        w[i]=w[i]+c*r*x2[i] #s-a dat formula alhamdulillah
    print("ponderile dupa corectie:", w)

print("Gata si tema, alhamdulillah")
