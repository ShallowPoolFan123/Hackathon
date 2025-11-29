from ursina import *
import subprocess
import sys
import os
import time
import main
import Credits


app = Ursina(size=(1920, 1080))
music = Audio('assets/bossTime.mp3', loop=True, autoplay=True)


### Objects ###

# Run game

def startGame():
    pass
     

# Menu
def setupMenu():
    scene.clear()
    menuBackground = Entity(
        parent = camera.ui,
        model = 'quad',
        texture = 'assets/background.png', 
        scale = (window.aspect_ratio, 1),
        position = (0, 0))

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

    def deleteMenu():
        destroy(menuBackground)
        destroy(menuCreditsButton)
        destroy(menuPlayButton)
        destroy(menuQuitButton)
    def startGame():
        deleteMenu()
    def quitGame():
        quit()
         

    menuPlayButton._on_click = startGame
    print(dir(Credits))
    menuCreditsButton._on_click = Credits.setupCredits
    menuQuitButton._on_click = quitGame






### Credits ###
def notsetupCredits():
    scene.clear()
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


    def deleteMenu():
        destroy(menuBackground)
        destroy(menuCreditsButton)
        destroy(menuPlayButton)
        destroy(menuQuitButton)

    def startGame():
        deleteMenu()

    def quitGame():
        quit()

    def startGame():
        deleteMenu()
        

    menuPlayButton._on_click = startGame
    menuCreditsButton._on_click = setupCredits
    menuQuitButton._on_click = quitGame






### Credits ###




### Functions ###

# Menu


    


    

def exitGame():
    time.sleep(1)
    quit()





setupMenu()

app.run()