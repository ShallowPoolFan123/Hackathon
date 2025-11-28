from ursina import *

app = Ursina()

background = Entity(
    parent = camera.ui,
    model = 'quad',
    texture = ('pride.png'),
    scale = (1, 1),
    position = (0, 0)
)

app.run