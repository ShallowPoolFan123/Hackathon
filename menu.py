from ursina import *
import time

app = Ursina(size=(600, 400))
music = Audio('Sound/Sound/bossTime.mp3', loop=True, autoplay=True)

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
        pressed_sound = 'assets/Sound/sword_slash.mp3',
        text_size = 1.5,)

    menuPlayButton = Button(
        text = "Play Game",
        color = color.green,
        origin = (-2, 0),
        scale = (0.3,0.2),
        pressed_sound = 'assets/Sound/sword_slash.mp3',
        text_size = 1.5,)

    menuQuitButton = Button(
        text = 'Quit',
        color=color.red,
        origin=(-2,-1.5),
        scale=(.3,.2),
        pressed_sound = 'assets/Sound/sword_slash.mp3',
        text_size=1.5
    )

    def setupCredits():

        creditsText = Text(
            text='Coders: Mateo, Cedric, Andrew\n\nArt: Max, Quinn, Andrew, Cedric, Mateo',
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
        
        
    #music = Audio('assets/fightMusic.mp3', loop=True, autoplay=True)    
    menuPlayButton._on_click = startGame
    menuCreditsButton._on_click = setupCredits
    menuQuitButton._on_click = quitGame

background = Entity(
    model = 'quad',
    color = color.violet,
    texture = 'assets/gameBackground.png', 
    scale = (16, 9, 1),
    position = (0,0,3)
    )

class Player(Sprite):
    def __init__(self, texture, position):
        super().__init__(
            texture = texture, 
            ppu = 16,
            scale = 1.2,
            speed = 5,
            position = position,
            velocity = 0
            )
        
        self.collider = BoxCollider(self, center=Vec3(0,0,0), size=Vec3(.3,1,5))
        self.health = 100
        self.lastkey = {}

player1 = Player('assets/idlePlayer.png', (-4, -2, 2))
player2 = Player('assets/idlePlayer2.png', (4, -2, 2))

wall1 = Entity(
    model = 'quad',
    collider = 'box',
    color = color.magenta,
    scale_x = 1,
    scale_y = 100,
    position = (-7, -5, -1),
    visible = False
        )

wall2 = Entity(
    model = 'quad',
    collider = 'box',
    color = color.yellow,
    scale_x = 1,
    scale_y = 100,
    position = (7, -5, -1),
    visible = False
    )


def update():
    player1Origin = player1.world_position
    player1Ray = raycast(player1Origin, direction=Vec2(1,0), ignore=(player1,wall1, wall2), distance=player1.velocity, debug=False)
    if player1Ray.hit: print('player 1 hit')

    if held_keys['d'] and not held_keys['a']:        
        if not player1Ray.hit:
            if player1.velocity < -0.01:
                player1.velocity = 0.05
            elif player1.velocity < 0.05:
                player1.velocity += time.dt * player1.speed/10 # right


    elif held_keys['a'] and not held_keys['d']:
        if not player1Ray.hit:
            if player1.velocity > 0.01:
                player1.velocity = -0.05
            elif player1.velocity > -0.05:
                player1.velocity -= time.dt * player1.speed/10 # left

    else:
        player1.velocity = lerp(player1.velocity, 0, 0.2)
    
    player1.velocity = round(player1.velocity, 3)
    if player1.velocity == 0.002 or player1.velocity == -0.002:
        player1.velocity = 0 

    player2Origin = player2.world_position
    player2Ray = raycast(player2Origin, direction=Vec2(1,0), ignore=(player2,wall1, wall2), distance=player2.velocity, debug=False)
    if player2Ray.hit: print('player 2 hit')

    if held_keys['l'] and not held_keys['j']:        
        if not player2Ray.hit:
            if player2.velocity < -0.01:
                player2.velocity = 0.05
            elif player2.velocity < 0.05:
                player2.velocity += time.dt * player2.speed/10 # right


    elif held_keys['j'] and not held_keys['l']:
        if not player2Ray.hit:
            if player2.velocity > 0.01:
                player2.velocity = -0.05
            elif player2.velocity > -0.05:
                player2.velocity -= time.dt * player2.speed/10 # left

    else:
        player2.velocity = lerp(player2.velocity, 0, 0.2)
    
    player2.velocity = round(player2.velocity, 3)
    if player2.velocity == 0.002 or player2.velocity == -0.002:
        player2.velocity = 0 

    player1.x += player1.velocity
    player2.x += player2.velocity
    
    if player1.intersects(wall1).hit:
        player1.x = -6.3
    if player1.intersects(wall2).hit:
        player1.x = 6.3
    if player2.intersects(wall1).hit:
        player2.x = -6.3
    if player2.intersects(wall2).hit:
        player2.x = 6.3

def exitGame():
    time.sleep(1)
    quit()

setupMenu()

app.run()