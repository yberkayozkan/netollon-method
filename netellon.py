import matplotlib.pyplot as plt 
import numpy as np
x=[0,85.5,304,470,622,750,800]
h=[464.95,461.5,448.9,447.5,462,465.78,470]
gson=np.array([6.69,7.46,10.29,10.61,7.34,6.49,5.55])

hf=np.array([])

g1=[]
g2=[]
g3=[]
g4=[]
g5=[]
g6=[]

hf=[]

fark=445

for i in h:
    hfark = i - fark
    hf.append(hfark)


for i in hf:
    g=(0.3086-0.04185*1.7)*i
    g1.append(g)
    
for i in hf:
    g=(0.3086-0.04185*1.8)*i
    g2.append(g)

for i in hf:
    g=(0.3086-0.04185*1.9)*i
    g3.append(g)

for i in hf:
    g=(0.3086-0.04185*2)*i
    g4.append(g)

for i in hf:
    g=(0.3086-0.04185*2.1)*i
    g5.append(g)

for i in hf:
    g=(0.3086-0.04185*2.2)*i
    g6.append(g)


a1=np.array(g1)
a2=np.array(g2)
a3=np.array(g3)
a4=np.array(g4)
a5=np.array(g5)
a6=np.array(g6)

s1=g1+gson
s2=g2+gson
s3=g3+gson
s4=g4+gson
s5=g5+gson
s6=g6+gson

plt.plot(x,s1)
plt.plot(x,s2)
plt.plot(x,s3)
plt.plot(x,s4)
plt.plot(x,s5)
plt.plot(x,s6)

plt.show()