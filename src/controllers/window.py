import glfw
from OpenGL.GL import *
from .polygon import Polygon
import numpy as np

class Window:
    def __init__(self, width: int, height: int, title: str,camera_rotation =False,  transparent_reverse=False):
        self._list_of_polygons = []
        self.transparent_reverse = transparent_reverse
        self.camera_rotation = camera_rotation
        # Initializing glfw library
        if not glfw.init():
            raise Exception('Glfw can not be initialized!')
        # Creating the window
        self._win = glfw.create_window(width, height, title, None, None)
        # Check if window was created
        if not self._win:
            glfw.terminate()
            raise Exception('Glfw window could not be created!')
        # Set window position
        glfw.set_window_pos(self._win, 400, 200)
        # Make the context current
        glfw.make_context_current(self._win)
        glClearColor(34/255, 34/255, 34/255, 1)

    # Main application loop
    def main_loop(self):

        #rotacion inical de camara para cambiar perspectiva
        glRotate(45, 1,0,0)
        glRotate(-30, 0,1,0)

        if  self.transparent_reverse:
            glEnable(GL_CULL_FACE);  
            glCullFace(GL_FRONT);  
        
        while not glfw.window_should_close(self._win):
            glfw.poll_events()
            glClear(GL_COLOR_BUFFER_BIT)
            self.draw_axis()
            for polygon in self._list_of_polygons:
                self._draw_polygon(polygon)
            
            if self.camera_rotation:
                glRotate(1, 0,1,0)
            
            glfw.swap_buffers(self._win)
            
        # Terminate glfw, free up allocated resources
        glfw.terminate()

    def add_polygon(self, polygon: Polygon):
        self._list_of_polygons.append(polygon)

    def draw_axis(self):
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, np.array([1, 0, 0, 0, 0, 0,
                                                  0, 1, 0, 0, 0, 0,
                                                  0, 0, 1, 0, 0, 0,
                                                  ]))
        glEnableClientState(GL_COLOR_ARRAY)

        glColorPointer(3, GL_FLOAT, 0,  np.array([1, 0, 0, 1, 1, 1,
                                                  0, 1, 0, 1, 1, 1,
                                                  0, 0, 1, 1, 1, 1,
                                                  ]))
        glDrawArrays(GL_LINES, 0, 6 )

    def _draw_polygon(self, polygon: Polygon):
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, polygon.get_vertices().flatten())
        glEnableClientState(GL_COLOR_ARRAY)
        glColorPointer(3, GL_FLOAT, 0, polygon.get_colors())
        glDrawArrays(GL_TRIANGLE_FAN, 0, polygon.get_sides())

