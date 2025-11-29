from ursina import *
app = Ursina()
back = Button(text='Andrew',scale=(.2,.1),position=(-0,0.1),pressed_scale=0.95,text_size=.9)
back2 = Button(text='Mateo',scale=(.2,.1),position=(-0,-0.1),pressed_scale=0.95,text_size=.9)
app.run()