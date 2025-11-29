from ursina import *
from ursina import Ursina, camera, Entity, EditorCamera

app = Ursina()

camera.orthographic = True

e = Entity()
e.model = 'quad'
e.color = color.random_color()
e.position = (-2, 0, 10)

e = Entity()
e.model = 'quad'
e.color = color.random_color()
e.position = (2, 0, 10)

e = Entity()
e.model = 'quad'
e.color = color.random_color()
e.position = (0, 0, 40)

EditorCamera()
from ursina.shaders import camera_grayscale_shader
camera.shader = camera_grayscale_shader

app.run()

