from ursina import *
from ursina import Ursina, camera, Entity, EditorCamera
import time

app = Ursina(size=(1280, 720))

music = Audio('assets/fightMusic.mp3', loop=True, autoplay=True)

background = Entity(
    parent = camera.ui,
    model = 'quad',
    color = color.violet,
    texture = 'assets/gameBackground.png', 
    scale = (window.aspect_ratio, 1),
    position = (0, 0)
)

player1 = Entity(
    model='assets/playerIdle',
    scale = 1,
    color = color.red,
    origin = (1, -0.5)
    )

speed = 5

def update():
    if held_keys['d']:
        player1.X += time.dt * speed
    if held_keys['a']:
        player1.X -= time.dt * speed 

app.run()