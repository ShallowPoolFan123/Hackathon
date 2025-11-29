from ursina import *
import menu
app = Ursina(size=(1920, 1080))
menu.setupMenu()
app.run()