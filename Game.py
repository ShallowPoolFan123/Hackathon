from ursina import *
import Credits
import menu
#app = Ursina()
def Andrew():
    WASD = Entity(
        parent = camera.ui,
        model = 'quad',
        texture = 'assets/WASD.png',
        scale = (0.22, 0.22),
        world_position = (-6, -3, -1))
    WASD = Entity(
        parent = camera.ui,
        model = 'quad',
        texture = 'assets/New Piskel (1).gif',
        scale = (0.22, 0.22),
        world_position = (6, -3, -1))
    invoke(Credits.setupCredits, delay=5)
def Mateo():
    WASD = Entity(
        parent = camera.ui,
        model = 'quad',
        texture = 'assets/New Piskel (1).gif',
        scale = (0.22, 0.22),
        world_position = (-6, -3, -1))
    WASD = Entity(
        parent = camera.ui,
        model = 'quad',
        texture = 'assets/WASD.png',
        scale = (0.22, 0.22),
        world_position = (6, -3, -1))
    invoke(Credits.setupCredits, delay=5)

def play():
    scene.clear()
    menu.background()
    back = Button(text='Andrew',scale=(.2,.1),world_position=(-6, 0, -1),pressed_scale=0.95,text_size=.9, color=color.black)
    back2 = Button(text='Mateo',scale=(.2,.1),world_position=(6, 0, -1),pressed_scale=0.95,text_size=.9, color=color.black)
    back._on_click = Andrew
    back2._on_click = Mateo