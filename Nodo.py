import math
import numpy as np

class Nodo:
    def __init__(self,entradas, b):
        self.entradas = None
        self.b = b
        self.z = None
        self.out = None
        if len(entradas[0]) == len(entradas[1]):
            self.entradas = np.array([entradas[0],entradas[1]])
            self.genZ()
            self.genOutput()
        else:
            print("No es una matriz cuadrada, no se guardaran los valores")


    def reSet(self, entradas, b):
        self.entradas = entradas
        self.b = b
        self.genZ()
        self.genOutput()

    def genZ(self):
        z = 0
        s = self.entradas.shape
        self.z = np.dot(self.entradas[0],self.entradas[1]).item() + self.b

    def getZ(self):
        return self.z

    def genOutput(self):
        print("Z: "+str(self.z))
        print("Out : " + str(self.out))
        if self.z < -709:
            self.z = -709
        self.out = 1 / (1 + math.exp(-self.z))

    def getOutput(self):
        return self.out


