from Nodo import Nodo
import numpy as np
from os import system
import random as r

class Network:
    def __init__(self, ):
        self.input = [1, 1]
        self.w1 = np.random.uniform(0,1,(3,2))
        self.w2 = np.random.uniform(0, 1, (2, 3))
        self.b1 = np.random.uniform(0, 1, (1, 3))
        self.b2 = np.random.uniform(0, 1, (1, 2))
        self.middleLayer = []
        for i in range(len(self.w1)):
            self.middleLayer.append(Nodo(np.array([[self.input[0], self.input[1]], [self.w1[i][0], self.w1[i][1]]]), self.b1[0][i]))
        self.z1 = []
        self.a1 = []
        for i in range(len(self.middleLayer)):
            self.z1.append(self.middleLayer[i].getZ())
            self.a1.append(self.middleLayer[i].getOutput())
        self.z1 = np.array(self.z1)
        self.a1 = np.array(self.a1)
        self.finalLayer = []
        for i in range(len(self.w2)):
            self.finalLayer.append(Nodo(np.array([[self.middleLayer[0].getOutput(),self.middleLayer[1].getOutput(),self.middleLayer[2].getOutput()],[self.w2[i][0],self.w2[i][1],self.w2[i][2]]]),self.b2[0][i]))
        self.z2 = []
        self.a2 = []
        for i in range(len(self.finalLayer)):
            self.z2.append(self.finalLayer[i].getZ())
            self.a2.append(self.finalLayer[i].getOutput())
        self.z2 = np.array(self.z2)
        self.a2 = np.array(self.a2)
        self.train()

    def backWardPropCalc(self, expected):
        dz2 = [[self.a2[0] - expected[0]], [self.a2[1] - expected[1]]]
        dw2 = np.multiply(dz2,np.transpose(self.a1))
        db2 = np.array([dz2[0][0],dz2[1][0]])
        self.w2 = self.w2 - (0.25 * dw2)
        self.b2 = self.b2 - (0.25 * db2)
        dz1 = np.dot(np.transpose(self.w2) @ dz2, self.a1 @ np.transpose(1-self.a1))
        dw1 = dz1 @ np.array([[self.input[0] , self.input[1]]])
        self.w1 = self.w1 - (0.25*dw1)
        self.b1 = self.b1 - (0.25*np.transpose(dz1))



    def train(self):
        inputs = [[0,0],[0,1],[1,0],[1,1]]
        expected = [[0,0],[0,1],[0,1],[0,1]]
        for i in range(1000):
            system('clear')
            print("Progress: " + str(i) + "/" + str(10000))
            for j in range(len(inputs)):
                self.input = inputs[j]
                self.do(self.input)
                self.backWardPropCalc(expected[j])
        #print("W1")
        #print(self.w1)
        #print("W2")
        #print(self.w2)



    # Cuando ya se ha realizado el entrenamiento le pasamos un input y nos devuelve el resultado
    def do(self, input):
        for i in range(len(self.w1)):
            self.middleLayer[i].reSet(np.array([[input[0],input[1]],[self.w1[i][0],self.w1[i][1]]]),self.b1[0][i])
        for i in range(len(self.middleLayer)):
            self.z1[i] = self.middleLayer[i].getZ()
            self.a1[i] = self.middleLayer[i].getOutput()
        for i in range(len(self.w2)):
            self.finalLayer[i].reSet(np.array([[self.middleLayer[0].getOutput(),self.middleLayer[1].getOutput(),self.middleLayer[2].getOutput()],[self.w2[i][0],self.w2[i][1],self.w2[i][2]]]),self.b2[0][i])
        for i in range(len(self.finalLayer)):
            self.z2[i] = self.finalLayer[i].getZ()
            self.a2[i] = self.finalLayer[i].getOutput()
        return self.a2

    def do2(self, input):
        self.input = input
        self.reCalc()
        return self.a2

    def reCalc(self):
        for i in range(len(self.middleLayer)):
            self.middleLayer[i].reSet(np.array([[self.input[0],self.input[1]], [self.w1[i][0], self.w1[i][1]]]),self.b1[0][i])

        for i in range(len(self.finalLayer)):
            self.finalLayer[i].reSet(np.array([[self.middleLayer[0].getOutput(),self.middleLayer[1].getOutput(),self.middleLayer[2].getOutput()],[self.w2[i][0],self.w2[i][1],self.w2[i][2]]]),self.b2[0][i])


    def getFinalOutput(self):
        return [self.finalLayer[0].getOutput(),self.finalLayer[1].getOutput()]



