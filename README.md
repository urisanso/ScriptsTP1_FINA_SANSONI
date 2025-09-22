# ScriptsTP1_FINA_SANSONI - TRANSORMACIONES

Este repositorio contiene scripts en Python y datasets asociados para analizar y visualizar transformaciones, rotaciones y trayectorias de un robot a partir de datos de sensores.

## Estructura del repositorio

.
├── mav0/                               # Carpeta con los archivos CSV (datos de la IMU, groundtruth, etc.)
│   ├── state_groundtruth_estimate0/data.csv
│   ├── cam0/data/sensor.yaml
│   └── ...
├── ejercicio1-2.py                     # Transformaciones con matrices de rotación en 3D
├── ejercicio3.py                       # Transformaciones y traslaciones en 2D
├── ejercicio5_ab.py                    # Visualización 3D de trayectoria de la cámara a partir de la IMU
├── ejercicio5_c.py                     # Comparación trayectoria IMU vs cámara
├── TP1_RobóticaMóvil_FINA_SANSONI.pdf  # Informe del desarrollo del TP
└── README.md                           # Documentación y uso

## Requisitos

Antes de ejecutar los scripts, asegurarse de tener instalado Python 3 y las siguientes librerías:

pip install numpy matplotlib pandas pyyaml transforms3d

## Descripción de los scripts

- ejercicio1-2.py
Implementa matrices de rotación alrededor de los ejes X, Y y Z. Calcula una composición de rotaciones y muestra la matriz resultante.
Uso:
python ejercicio1-2.py

- ejercicio3.py
Implementa matrices de rotación y traslación en 2D. Convierte un punto de un sistema de coordenadas a otro (SC A ↔ SC W).
Uso:
python ejercicio3.py

- ejercicio5_ab.py
Lee datos de la IMU desde un .csv y la transformación de cámara desde sensor.yaml.
Muestra la trayectoria de la cámara en 3D, graficando los ejes locales en cada frame.
Uso:
python ejercicio5_ab.py

- ejercicio5_c.py
Similar a 5_ab, pero además grafica en 3D la trayectoria de la IMU y la compara con la trayectoria de la cámara.
Uso:
python ejercicio5_c.py

## Datos

Los datasets .csv se encuentran en la carpeta mav0/.

El archivo sensor.yaml contiene la transformación entre la IMU y la cámara.

## Autores

Trabajo realizado por FINA, Facundo y SANSONI, Uriel.