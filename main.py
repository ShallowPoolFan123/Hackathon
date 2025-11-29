from ursina import *
from ursina import Ursina, camera, Entity, EditorCamera

app = Ursina(size=(1920, 1080))

camera.position = Vec3(100, 0, 100)

music = Audio('assets/fightMusic.mp3', loop=True, autoplay=True)

background = Entity(
    parent = camera.ui,
    model = 'quad',
    texture = 'assets/gameBackground.png', 
    scale = (window.aspect_ratio, 1),
    position = (0, 0.5)
)

app.run()