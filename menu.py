from ursina import *
import subprocess
import sys
import os

app = Ursina()

background = Entity(
    parent = camera.ui,
    model = 'quad',
    color = color.red,
    scale = (window.aspect_ratio, 1),
    position = (0, 0)
)

def startCredits():

    print("Attempting to start external credits...")

    python_executable = sys.executable
    script_path = os.path.join(os.path.dirname(__file__), 'credits.py')

    try:
        subprocess.Popen([python_executable, script_path])
        print("External program launched.")
        quit()
    except Exception as e:
        print(f"Failed to launch program: {e}")
    

creditsButton = Button(
    text = "Play Credits",
    color = color.blue,
    origin = (2, 0),
    scale = (0.3,0.2),
    text_size = 1.5,
)

creditsButton._on_click = startCredits

app.run()