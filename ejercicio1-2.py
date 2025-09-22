import matplotlib.pyplot as plt
import numpy as np
import math

def Rx(deg):
    r = math.radians(deg)
    return np.array([
        [1,0,0],
        [0, math.cos(r), -math.sin(r)],
        [0, math.sin(r),  math.cos(r)]
    ])

def Ry(deg):
    r = math.radians(deg)
    return np.array([
        [math.cos(r), 0, math.sin(r)],
        [0, 1, 0],
        [-math.sin(r), 0, math.cos(r)]
    ])

def Rz(deg):
    r = math.radians(deg)
    return np.array([
        [math.cos(r), -math.sin(r), 0],
        [math.sin(r),  math.cos(r), 0],
        [0, 0, 1]
    ])

psi = Rx(720/7) @ Ry(90) @ Rz(-60)
#print("Ry(90): ",np.round(Ry(90), 6)) 
#print("Rx(-90)*Ry(90): ",np.round(Rx(-90) @ Ry(90), 6)) 
print("psi: ",np.round(psi, 6))   
