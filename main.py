from ursina import *

app = Ursina()

background = Entity(
    parent = camera.ui,
    model = 'quad',
    #texture = 'assets/background.png', 
    color=color.red,
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