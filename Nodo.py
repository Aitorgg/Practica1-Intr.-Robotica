import math
import numpy as np

class Nodo:
    def __init__(self,entradas):
        self.entradas = None
        if len(entradas[0]) == len(entradas[1]):
            self.entradas = np.array([entradas[0],entradas[1]])
            self.genZ()
            self.genOutput()
        else:
            print("No es una matriz cuadrada, no se guardaran los valores")


    def genZ(self):
        z = 0
        s = self.entradas.shape
        self.z = None
        self.z = np.dot(self.entradas[0],self.entradas[1]).item() + 1

    def getZ(self):
        return self.z

    def genOutput(self):
        self.out = 1 / (1 + math.exp(-self.z))

    def getOutput(self):
        return self.out