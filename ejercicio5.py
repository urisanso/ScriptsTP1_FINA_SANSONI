import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from transforms3d.quaternions import quat2mat
import pandas as pd

# Leer archivo CSV
trayectoria_csv = pd.read_csv("data.csv")

print(trayectoria_csv.iloc[1])

print(trayectoria_csv[" p_RS_R_x [m]"])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Escala para los vectores
scale = 0.5

for i in range(len(trayectoria_csv["#timestamp"])):
    #print(trayectoria_csv["#timestamp"].iloc[i])
    #print(i)
    t = trayectoria_csv["#timestamp"].iloc[i]
    x = trayectoria_csv[" p_RS_R_x [m]"].iloc[i]
    y = trayectoria_csv[" p_RS_R_y [m]"].iloc[i]
    z = trayectoria_csv[" p_RS_R_z [m]"].iloc[i]
    qw = trayectoria_csv[" q_RS_w []"].iloc[i]
    qx = trayectoria_csv[" q_RS_x []"].iloc[i]
    qy = trayectoria_csv[" q_RS_y []"].iloc[i]
    qz = trayectoria_csv[" q_RS_z []"].iloc[i]

    # Convertimos el cuaternión a matriz de rotación 3x3
    R = quat2mat([qw, qx, qy, qz])

    print("Matriz de rotación:")
    print(R)

    r = np.array([
        [x],
        [y],
        [z]
    ])

    ax.quiver(x, y, z, R[0,0], R[1,0], R[2,0], color='r', length=scale)
    ax.quiver(x, y, z, R[0,1], R[1,1], R[2,1], color='g', length=scale)
    ax.quiver(x, y, z, R[0,2], R[1,2], R[2,2], color='b', length=scale)

# Ajustes de la vista
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Sistemas de referencia 3D por punto')
ax.set_box_aspect([1,1,1])

plt.show()












