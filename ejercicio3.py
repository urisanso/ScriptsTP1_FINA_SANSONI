import numpy as np
import math

# Matriz de rotación
# W --> A 
# Para el passaje de puntos en SC A a SC W
def wRa(deg):
    r = math.radians(deg)
    return np.array([
        [math.cos(r), -math.sin(r)],
        [math.sin(r),  math.cos(r)]
    ])

# Para el passaje de puntos en SC W a SC A
def aRw(deg):
    r = math.radians(deg)
    return np.array([
        [ math.cos(r), math.sin(r)],
        [-math.sin(r), math.cos(r)]
    ])

# Matriz de traslación
# Para el passaje de puntos en SC A a SC W
def WtA(n1, n2):
    return np.array([
        [n1],
        [n2]
    ])

# Para el passaje de puntos en SC W a SC A
def AtW(n1, n2):
    return np.array([
        [-n1],
        [-n2]
    ])

p_w = np.array([[-1],[2]])

p_a = aRw(45) @ p_w #+ AtW(2,3)

print("aRw(45): \n",np.round(aRw(45), 3))
print("p_w: \n",np.round(p_w, 3))
print("AtW(2,3): \n",np.round(AtW(2,3), 3))
print("p_a: \n",np.round(p_a, 3))   
