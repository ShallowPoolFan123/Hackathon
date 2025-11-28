from ursina import *

app = Ursina()

background = Entity(
    parent = camera.ui,
    model = 'quad',
    color = color.red,
    scale = (window.aspect_ratio, 1),
    position = (0, 0)
)

app.run()