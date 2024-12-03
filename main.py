from Nodo import Nodo
import numpy as np
from Network import Network

#n = Nodo(np.array([[0,1],[1,1]]),1)
#print(n.getOutput())
net = Network()
net.do2([0,0])
print(net.getFinalOutput())
net.do2([0,1])
print(net.getFinalOutput())
net.do2([1,0])
print(net.getFinalOutput())
net.do2([1,1])
print(net.getFinalOutput())