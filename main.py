from ursina import *
from ursina import Ursina, camera, Entity, EditorCamera

app = Ursina(size=(1920, 1080))

music = Audio('assets/fightMusic.mp3', loop=True, autoplay=True)

background = Entity(
    parent = camera.ui,
    model = 'quad',
    color=color.red,
    texture = 'assets/gameBackground.png', 
    scale = (window.aspect_ratio, 1),
    position = (0, 0)
)

# Classes
class Character():
    def __init__(self, jumpCooldown, speed):
        pass
    
    

    def input(key):
        def jump():
            pass
            
        debounce = False
        print('key', key)
        if key == 'jump':
            pass


            
        

import subprocess
app = Ursina()
def switch_scene(scene):
    python_executable = sys.executable
    script_path = os.path.join(os.path.dirname(__file__), scene)
    try:
        subprocess.Popen([python_executable, script_path])
        print("External program launched.")
        quit()
    except Exception as e:
        print(f"Failed to launch program: {e}")
def Andrew():
    WASD = Entity(
        parent = camera.ui,
        model = 'quad',
        texture = 'assets/WASD.png',
        scale = (0.22, 0.22),
        world_position = (-6, -3))
    WASD = Entity(
        parent = camera.ui,
        model = 'quad',
        texture = 'assets/New Piskel (1).gif',
        scale = (0.22, 0.22),
        world_position = (6, -3))
    invoke(switch_scene, 'credits.py', delay=3)
def Mateo():
    WASD = Entity(
        parent = camera.ui,
        model = 'quad',
        texture = 'assets/New Piskel (1).gif',
        scale = (0.22, 0.22),
        world_position = (-6, -3))
    WASD = Entity(
        parent = camera.ui,
        model = 'quad',
        texture = 'assets/WASD.png',
        scale = (0.22, 0.22),
        world_position = (6, -3))
    invoke(switch_scene, 'credits.py', delay=3)
back = Button(text='Andrew',scale=(.2,.1),position=(-0.3,0),pressed_scale=0.95,text_size=.9)
back2 = Button(text='Mateo',scale=(.2,.1),position=(0.3,-0),pressed_scale=0.95,text_size=.9)
back._on_click = Andrew
back2._on_click = Mateo
app.run()