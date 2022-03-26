import matplotlib.pyplot as plt 
import numpy as np

x=[0,85.5,304,470,622,750,800]
h=[464.95,461.5,448.9,447.5,462,465.78,470]
gson=[6.69,7.46,10.29,10.61,7.34,6.49,5.55]
g=[[] for x in range(6)]

hf=[]

fark=445
temp =1.7
for i in h:
    hfark = i - fark
    hf.append(hfark)

for i in range(6):
    for j in hf:
        g[i].append((0.3086-0.04185*temp)*j)
    temp+=0.1
for i in range(len(g)):
    for j in range(len(g[i])):
        g[i][j] += gson[j]
    plt.plot(x,g[i])
plt.show()