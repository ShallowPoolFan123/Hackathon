from ursina import *
import time


app = Ursina(size=(1920, 1080))
music = Audio('assets/bossTime.mp3', loop=True, autoplay=True)

### updateloop ###



# Run game

     

# Menu
def setupMenu():
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

    def setupCredits():

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


    def quitGame():
        quit()

    def startGame():
        deleteMenu()
        
        
    music = Audio('assets/fightMusic.mp3', loop=True, autoplay=True)    
    menuPlayButton._on_click = startGame
    menuCreditsButton._on_click = setupCredits
    menuQuitButton._on_click = quitGame

# def gherigh():
#     global game
#     game = False
    
# gherigh()


background = Entity(
    model = 'quad',
    color = color.violet,
    texture = 'assets/gameBackground.png', 
    scale = (16, 9, 1),
    position = (0,0,3)
    )

player1 = Sprite(
    texture='assets/idlePlayer.png',
    collider = 'box',
    ppu = 16,
    scale = 1.2,
    position = (-4, -2, -1)
    )

player2 = Sprite(
    texture='assets/idlePlayer2.png',
    collider = 'box',
    ppu = 16,
    scale = 1.2,
    position = (4, -2, -1)
    )

speed = 5

wall1 = Entity(
    model = 'quad',
    collider = 'box',
    color = color.magenta,
    scale_x = 1,
    scale_y = 100,
    position = (-7, -5, -1),
    visible = True
        )

wall2 = Entity(
    model = 'quad',
    collider = 'box',
    color = color.yellow,
    scale_x = 1,
    scale_y = 100,
    position = (7, -5, -1),
    visible = True
    )


game1 = False
def update():
    if held_keys['d']:
        player1.x += time.dt * speed
    if held_keys['a']:
        player1.x -= time.dt * speed 

    if held_keys['l']:
        player2.x += time.dt * speed
    if held_keys['j']:
        player2.x -= time.dt * speed 

    if player1.intersects(wall1).hit:
        player1.x = -5.6
        print("hit")
    if player1.intersects(wall2).hit:
        player1.x = 5.6
        print("hit")
    if player2.intersects(wall1).hit:
        player2.x = -5.6
        print("hit")
    if player2.intersects(wall2).hit:
        player2.x = 5.6
        print("hit")

def exitGame():
    time.sleep(1)
    quit()

setupMenu()

app.run()