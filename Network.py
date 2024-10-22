from Nodo import Nodo
import numpy as np


class Network:
    def __init__(self):
        sNodo1 = Nodo(np.array([[1,1],[1,1]]))
        sNodo2 = Nodo(np.array([[1,1],[1,1]]))
        self.startLayer = [sNodo1,sNodo2]
        self.w1 = np.array([[1,1,1],[1,1,1]])
        self.middleLayer = []
        for i in range(len(self.w1[0])):
            self.middleLayer.append(Nodo(np.array([[sNodo1.getOutput(),sNodo2.getOutput()],[self.w1[0][i],self.w1[1][i]]])))
        self.z1 = []
        self.a1 = []
        for i in range(len(self.middleLayer)):
            self.z1.append(self.middleLayer[i].getZ())
            self.a1.append((self.middleLayer[i].getOutput()))
        self.w2 = np.array([[1, 1], [1, 1],[1,1]])
        self.finalLayer = []
        for i in range(len(self.w2[0])):
            self.finalLayer.append(Nodo(np.array([[self.middleLayer[0].getOutput(),self.middleLayer[1].getOutput(),self.middleLayer[2].getOutput()],[self.w2[0][i],self.w2[1][i],self.w2[2][i]]])))
        self.z2 = []
        self.a2 = []
        for i in range(len(self.finalLayer)):
            self.z2.append(self.finalLayer[i].getZ())
            self.a2.append(self.finalLayer[i].getOutput())



    def getFinalOutput(self):
        return [self.finalLayer[0].getOutput(),self.finalLayer[1].getOutput()]



