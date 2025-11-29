from ursina import *

app = Ursina(size=(1920, 1080))

music = Audio('assets/fightMusic.mp3', loop=True, autoplay=True)

background = Entity(
    parent = camera.ui,
    model = 'quad',
<<<<<<< HEAD
    #texture = 'assets/background.png', 
    color=color.red,
=======
    texture = 'assets/gameBackground.png', 
>>>>>>> 89d04169cc5b7764bd144ed2afe862e25498c0cc
    scale = (window.aspect_ratio, 1),
    position = (0, 0)
)

# Classes
class Character():
    def __init__(self, jumpCooldown, speed):
        pass
    
    

    def input(key):
        def jump():
            if 
            
        debounce = False
        print('key', key)
        if key == 'jump':


            
        

app.run()