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
    script_path = os.path.join(os.path.dirname(__file__), 'Credits.py')

    try:
        subprocess.Popen([python_executable, script_path])
        print("External program launched.")
    except Exception as e:
        print(f"Failed to launch program: {e}")

creditsButton = Button(
    text = "Play Credits",
    color = color.blue,
    scale = .1,
    x = 0,
    y = 0
)

creditsButton._on_click = startCredits

app.run()