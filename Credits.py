from ursina import *
import random

app = Ursina()

# Variables
creditsText = 'Coders: Mateo, Cedric, Andrew\n\nArt: Max, Quinn'

# Entities
background = Entity(model='quad', color=color.rgb32(223, 144, 232), scale=15)
text = Text(text=creditsText,size=4,origin=(0,0))
back = Button(text='Back',scale=(1.8,.1),origin=(-0,-0),pressed_scale=0.95,text_size=.9,rotation=(random.randint(30,100),random.randint(30,100),random.randint(30,100)))

app.run()