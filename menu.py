from ursina import *
import time

app = Ursina(size=(1920, 1080))
music = Audio('assets/bossTime.mp3', loop=True, autoplay=True)

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
            position = position
            )
        self.collider = BoxCollider(self, center=Vec3(0,0,0), size=Vec3(.3,1,1))
        self.health = 100

player1 = Player('assets/idlePlayer.png', (-4, -2, -1))
player2 = Player('assets/idlePlayer2.png', (4, -2, -1))

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
    p1Origin = player1.world_position
    p1hitInfoR = raycast(p1Origin, direction=Vec3(1,0,0), ignore=(player1,wall1, wall2), distance=time.dt * player1.speed, debug=False)
    p1hitInfoL = raycast(p1Origin, direction=Vec3(-1,0,0), ignore=(player1,wall1,wall2), distance=time.dt * player1.speed, debug=False)
    if held_keys['d']:        
        if not p1hitInfoR.hit:
            player1.x += time.dt * player1.speed # right
    if held_keys['a']:
        if not p1hitInfoL.hit:
            player1.x -= time.dt * player1.speed # left

    


    p2Origin = player2.world_position
    p2hitInfoR = raycast(p2Origin, direction=Vec3(1,0,0), ignore=(player2,wall1, wall2), distance=time.dt * player2.speed, debug=False)
    p2hitInfoL = raycast(p2Origin, direction=Vec3(-1,0,0), ignore=(player2,wall1,wall2), distance=time.dt * player2.speed, debug=False)
    if held_keys['l']:        
        if not p2hitInfoR.hit:
            player2.x += time.dt * player2.speed # right
    if held_keys['j']:
        if not p2hitInfoL.hit:
            player2.x -= time.dt * player2.speed # left


    if p1hitInfoR.hit and p2hitInfoL.hit:
        player1.x -= player1.speed * time.dt * 2 # left
        player2.x += player2.speed * time.dt * 2 # right

    if p1hitInfoL.hit and p2hitInfoR.hit:
        player1.x += player1.speed * time.dt * 2 # right
        player2.x -= player2.speed * time.dt * 2 # left

    # if held_keys['l']:
    #     player2.x += time.dt * speed
    # if held_keys['j']:
    #     player2.x -= time.dt * speed 

    # def move(player1):
    #     player1.direction = Vec3(
    #         player1.right * (held_keys['d'] - held_keys['a'])).normalized()
    #     origin = player1.world_position
    #     hit_info = raycast(origin, player1.direction, ignore=(player1,), distance=.5, debug=False)
    #     if not hit_info.hit:
    #         player1.position += player1.direction * 5 * time.dt

    if player1.intersects(wall1).hit:
        player1.x = -6.3
        print("hit")
    if player1.intersects(wall2).hit:
        player1.x = 6.3
        print("hit")
    if player2.intersects(wall1).hit:
        player2.x = -6.3
        print("hit")
    if player2.intersects(wall2).hit:
        player2.x = 6.3
        print("hit")

def exitGame():
    time.sleep(1)
    quit()

setupMenu()

app.run()