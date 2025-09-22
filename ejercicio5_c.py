import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from transforms3d.quaternions import quat2mat
import pandas as pd
import yaml

# leemos el dataset de la IMU
trayectoria_csv = pd.read_csv("ScriptsTP1_FINA_SANSONI/mav0/state_groundtruth_estimate0/data.csv")

# leemos matriz de transformación de la cam0 con repecto a la IMU
with open("ScriptsTP1_FINA_SANSONI/mav0/cam0/sensor.yaml", "r") as f:
    sensor_data = yaml.safe_load(f)

T_data = sensor_data["T_BS"]["data"]   

# pose de la cam0 con respecto a la IMU
T_BC = np.array(T_data).reshape((4,4))    

# abrimos el grafico
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# escala para los vectores
scale = 0.25

XS, YS, ZS = [], [], []
xs, ys, zs = [], [], []

for i in range(1500):   #len(trayectoria_csv["#timestamp"])

    t_ns = trayectoria_csv["#timestamp"].iloc[i]
    t_s = t_ns*1e-9
    x = trayectoria_csv[" p_RS_R_x [m]"].iloc[i]
    y = trayectoria_csv[" p_RS_R_y [m]"].iloc[i]
    z = trayectoria_csv[" p_RS_R_z [m]"].iloc[i]
    qw = trayectoria_csv[" q_RS_w []"].iloc[i]
    qx = trayectoria_csv[" q_RS_x []"].iloc[i]
    qy = trayectoria_csv[" q_RS_y []"].iloc[i]
    qz = trayectoria_csv[" q_RS_z []"].iloc[i]

    # Convertimos el cuaternión a matriz de rotación 3x3
    R = quat2mat([qw, qx, qy, qz])

    r = np.array([
        [x],
        [y],
        [z]
    ])

    # pose de la IMU con respecto al mundo
    T_WB = np.block([
        [R, r],
        [np.zeros((1,3)), np.ones((1,1))]
    ])

    # pose de la cam0 con respecto al mundo
    T_WC = T_WB @ T_BC

    X=T_WC[0,3]
    Y=T_WC[1,3]
    Z=T_WC[2,3]

    # acumulamos posiciones para la trayectoria
    XS.append(X)
    YS.append(Y)
    ZS.append(Z)

    xs.append(x)
    ys.append(y)
    zs.append(z)

    # limpiamos vectores de frames anteriores
    ax.cla()

    # trayectorias acumuladas
    ax.plot(XS, YS, ZS, color='gray', linewidth=1, label='cam0')

    ax.plot(xs, ys, zs, color='orange', linewidth=1, label='IMU')


    # dibujamos las flechas
    ax.quiver(X, Y, Z, T_WC[0,0], T_WC[1,0], T_WC[2,0], color='r', length=scale, label='x')
    ax.quiver(X, Y, Z, T_WC[0,1], T_WC[1,1], T_WC[2,1], color='g', length=scale, label='y')
    ax.quiver(X, Y, Z, T_WC[0,2], T_WC[1,2], T_WC[2,2], color='b', length=scale, label='z')

    ax.quiver(x, y, z, R[0,0], R[1,0], R[2,0], color='r', length=scale)
    ax.quiver(x, y, z, R[0,1], R[1,1], R[2,1], color='g', length=scale)
    ax.quiver(x, y, z, R[0,2], R[1,2], R[2,2], color='b', length=scale)

    # Etiquetas y título
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Frame numero: {i} Timestamp: {t_s:.9f}s')
    ax.legend(loc="upper left")
    ax.set_xlim(4.4, 5.1)
    ax.set_ylim(-2.1, -1.5)
    ax.set_zlim(0.5, 1.2)
    ax.set_box_aspect([1,1,1])

    # actualizamos frame
    plt.draw()
    plt.pause(0.00000000001)  # Pausa breve para ver la animación

plt.ioff()
plt.show()









