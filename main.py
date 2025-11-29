from ursina import *
from ursina import Ursina, camera, Entity, EditorCamera
import time

app = Ursina(size=(1280, 720))

music = Audio('assets/fightMusic.mp3', loop=True, autoplay=True)



background = Entity(
      model = 'quad',
      color = color.violet,
      texture = 'assets/gameBackground.png', 
      scale = (15.3, 8.2, -1),
)

player1 = Sprite(
    texture='assets/playerIdle.png',
    collider = 'box',
    ppu = 16,
    scale = 0.5,
    origin = (1, 0.5, 0)
)

player2 = Sprite(
    texture='assets/playerIdle.png',
    collider = 'box',
    ppu = 16,
    scale = 0.5,
    origin = (-1, 0.5, 0)
)

speed = 5

wall1 = Entity(
    model = 'quad',
    collider = 'box',
    scale_x = 1,
    scale_y = 100,
    position = (7, -5, 0),
    visible = True
)

wall2 = Entity(
    model = 'quad',
    collider = 'box',
    scale_x = 1,
    scale_y = 100,
    position = (-7, -5, 0),
    visible = True
)

def update():
    if held_keys['d']:
        player1.x += time.dt * speed
    if held_keys['a']:
        player1.x -= time.dt * speed 
    if held_keys['w']:
        player1.y += time.dt * speed 
    if held_keys['s']:
        player1.y -= time.dt * speed 

    if held_keys['l']:
        player2.x += time.dt * speed
    if held_keys['j']:
        player2.x -= time.dt * speed 
    if held_keys['i']:
        player2.y += time.dt * speed 
    if held_keys['k']:
        player2.y -= time.dt * speed 

    if wall1.intersects(player2).hit:
        player1.position = (-6.5, 0, 0)
        print("hit")
    if wall2.intersects(player2).hit:
        player1.position = (6.5, 0, 0)
        print("hit")
    if wall1.intersects(player1).hit:
        player1.position = (-6.5, 0, 0)
        print("hit")
    if wall2.intersects(player1).hit:
        player1.position = (6.5, 0, 0)
        print("hit")




app.run()