from ursina import *
import subprocess
import sys
import os
import time
import Game
import Credits

music = Audio('assets/bossTime.mp3', loop=True, autoplay=True)

### Objects ###

# Run game
def background():
    menuBackground = Entity(
        parent = camera.ui,
        model = 'quad',
        texture = 'assets/background.png', 
        scale = (window.aspect_ratio, 1),
        position = (0, 0, 0))
# Menu
def setupMenu():
    scene.clear()
    background()
    menuCreditsButton = Button(
        text = "Play Credits",
        color = color.blue,
        origin = (2, 0),
        scale = (0.3,0.2),
        pressed_sound = 'assets/sword_slash.mp3',
        text_size = 1.5,)

    menuPlayButton = Button(
        text = "Play Game",
        color = color.green,
        origin = (-2, 0),
        scale = (0.3,0.2),
        pressed_sound = 'assets/sword_slash.mp3',
        text_size = 1.5,)

    menuQuitButton = Button(
        text = 'Quit',
        color=color.red,
        origin=(-2,-1.5),
        scale=(.3,.2),
        pressed_sound = 'assets/sword_slash.mp3',
        text_size=1.5
    )
    def quitGame():
        quit()
    menuCreditsButton._on_click = lambda: Credits.setupCredits(setupMenu)
    menuQuitButton._on_click = quitGame
    menuPlayButton._on_click = Game.play