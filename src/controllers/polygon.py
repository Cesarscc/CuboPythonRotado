import numpy as np


class Polygon:
    def __init__(self,
                 polygon_vertices: list,
                 ):

        color = np.random.rand(3)#Genera un vector de 3 argumentos con numeros aleatorios entre 0 y 1
        polygon_colors = np.array(
            [[0.5, 0.5, 1.5], color, color, [0, 0, 0]]).flatten()

        self._vertices = np.array(polygon_vertices, dtype=np.float32)/2
        self._colors = np.array(polygon_colors, dtype=np.float32)
        self._sides = len(polygon_vertices)

    def get_vertices(self):
        return self._vertices

    def get_colors(self):
        return self._colors

    def get_sides(self):
        return self._sides

    def apply_transform(self, transform):
        self._vertices = np.array(map(transform, self._vertices))

    def translate_vertex(self, translation, vertex: np.array):
        return
