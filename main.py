from ursina import *
app = Ursina()
back = Button(text='Andrew',scale=(1.8,.1),origin=(-0,-0),pressed_scale=0.95,text_size=.9)
back2 = Button(text='Mateo',scale=(1.8,.1),origin=(-0, -0, -1000),pressed_scale=0.95,text_size=.9)
app.run()