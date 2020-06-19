from controllers.window import Window
from controllers.polygon import Polygon
import numpy as np
import math
import time

if __name__ == '__main__':

    win = Window(450, 450, 'Visor 3D CUBO', 
    camera_rotation=True,
    transparent_reverse=True
    )

   #Creamos nuestro cubo
    p = [
        [0, 0, 0], 
        [1, 0, 0], 
        [0, 1, 0], 
        [0, 0, 1], 
        [1, 1, 0], 
        [1, 0, 1], 
        [0, 1, 1], 
        [1, 1, 1],]
    cube = [
        Polygon([p[0], p[1], p[4], p[2], ]),
        Polygon([p[0], p[3], p[5], p[1], ]),
        Polygon([p[0], p[2], p[6], p[3], ]),
        Polygon([p[7], p[4], p[1], p[5], ]),
        Polygon([p[7], p[6], p[2], p[4], ]),
        Polygon([p[7], p[5], p[3], p[6], ]),
    ]

    #y añadimos cada una de las caras 
    for face in cube:
        win.add_polygon(face)
        
    win.main_loop()

    win2 = Window(450, 450, 'Visor 3D CUBOTRANSFORMADO', 
    camera_rotation=True,
    transparent_reverse=True
    )
    #creamos el cubo transformado
    p2 = [
        [0, 0, 0], 
        [(1+math.sqrt(3))/3, (1-math.sqrt(3))/3, 1/3], 
        [1/3, (1+math.sqrt(3))/3, (1-math.sqrt(3))/3], 
        [(1-math.sqrt(3))/3, 1/3, (1+math.sqrt(3))/3], 
        [(2+math.sqrt(3))/3, 2/3, (2-math.sqrt(3))/3], 
        [2/3, (2-math.sqrt(3))/3, (2+math.sqrt(3))/3], 
        [(2-math.sqrt(3))/3, (2+math.sqrt(3))/3, 2/3], 
        [1, 1, 1],]

    cubeTrans = [
        Polygon([p2[0], p2[1], p2[4], p2[2], ]),
        Polygon([p2[0], p2[3], p2[5], p2[1], ]),
        Polygon([p2[0], p2[2], p2[6], p2[3], ]),
        Polygon([p2[7], p2[4], p2[1], p2[5], ]),
        Polygon([p2[7], p2[6], p2[2], p2[4], ]),
        Polygon([p2[7], p2[5], p2[3], p2[6], ]),
    ]
    

    #y añadimos cada una de las caras 
    for face in cubeTrans:
        win2.add_polygon(face)

    win2.main_loop()