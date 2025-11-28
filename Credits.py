from ursina import *
import subprocess
import sys
import os


app = Ursina()

# Variables
creditsText = 'Coders: Mateo, Cedric, Andrew\n\nArt: Max, Quinn'

# Entities
background = Entity(model='quad', color=color.rgb32(223, 144, 232), scale=15)
text = Text(text=creditsText,size=4,origin=(0,0))
back = Button(text='Back',scale=(1.8,.1),origin=(-0,-0),pressed_scale=0.95,text_size=.9,rotation=(random.randint(5,85),random.randint(5,85),random.randint(5,85)))

def returnToMenu():

    print("Attempting to start external credits...")

    python_executable = sys.executable
    script_path = os.path.join(os.path.dirname(__file__), 'menu.py')

    try:
        subprocess.Popen([python_executable, script_path])
        print("External program launched.")
        quit()
    except Exception as e:
        print(f"Failed to launch program: {e}")

back._on_click = returnToMenu
app.run()