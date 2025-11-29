from ursina import *
import subprocess
import sys
import os
import time


app = Ursina(size=(1920, 1080))
music = Audio('assets/bossTime.mp3', loop=True, autoplay=True)


### Objects ###

# Menu

background = Entity(
    parent = camera.ui,
    model = 'quad',
    texture = 'assets/background.png', 
    scale = (window.aspect_ratio, 1),
    position = (0, 0))

creditsButton = Button(
    text = "Play Credits",
    color = color.blue,
    origin = (2, 0),
    scale = (0.3,0.2),
    pressed_sound = 'assets/sword_slash.mp3',
    text_size = 1.5,)

mainButton = Button(
    text = "Play Game",
    color = color.green,
    origin = (-2, 0),
    scale = (0.3,0.2),
    pressed_sound = 'assets/sword_slash.mp3',
    text_size = 1.5,)

quitButton = Button(
    text = 'Quit',
    color=color.red,
    origin=(-2,-1.5),
    scale=(.3,.2),
    pressed_sound = 'assets/sword_slash.mp3',
    text_size=1.5
)

### Credits ###
def startCredits():

    creditsText = Text(
        text='Coders: Mateo, Cedric, Andrew\n\nArt: Max, Quinn, Andrew',
        size=4,
        origin=(0,0)
    )

    creditsBack = Button(
        text= 'Back',
        scale = (1.8, 0.1),
        origin = (0, 4),
        pressed_scale = 0.95,
        text_size = 0.9,
    )
    

    def deleteCredits():
            destroy(creditsText)
            destroy(creditsBack)
    creditsBack._on_click = deleteCredits



### Functions ###

# Menu


    

def startGame():
    print("Attempting to start game...")
    python_executable = sys.executable
    script_path = os.path.join(os.path.dirname(__file__), 'main.py')
    try:
        subprocess.Popen([python_executable, script_path])
        print("External program launched.")
        time.sleep(1)
        quit()
    except Exception as e:
        print(f"Failed to launch program: {e}")

def exitGame():
    time.sleep(1)
    quit()






creditsButton._on_click = startCredits
mainButton._on_click = startGame
quitButton._on_click = exitGame
app.run()