import pygame
import sys
import time
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
FPS = 60

# Colors
BLUE = (0, 100, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
VIOLET = (138, 43, 226)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game Menu")
clock = pygame.time.Clock()

# Load and play music
try:
    pygame.mixer.music.load('assets/Sound/bossTime.mp3')
    pygame.mixer.music.play(-1)  # -1 means loop forever
except Exception as e:
    print(f"Warning: Could not load background music: {e}")

# Load sound effects
try:
    sword_slash_sound = pygame.mixer.Sound('assets/Sound/sword_slash.mp3')
except:
    sword_slash_sound = None
    print("Warning: Could not load sword slash sound")

# Load images
try:
    menu_background_img = pygame.image.load('assets/background.png')
    menu_background_img = pygame.transform.scale(menu_background_img, (WINDOW_WIDTH, WINDOW_HEIGHT))
except:
    menu_background_img = None
    print("Warning: Could not load menu background")

try:
    game_background_img = pygame.image.load('assets/gameBackground.png')
    game_background_img = pygame.transform.scale(game_background_img, (WINDOW_WIDTH, WINDOW_HEIGHT))
except:
    game_background_img = None
    print("Warning: Could not load game background")

# Button class
class Button:
    def __init__(self, text, color, x, y, width, height, text_size=30):
        self.text = text
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.text_size = text_size
        self.font = pygame.font.Font(None, text_size)
        self.hovered = False

    def draw(self, screen):
        # Draw button background
        color = tuple(min(c + 30, 255) for c in self.color) if self.hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, WHITE, self.rect, 2)  # Border

        # Draw text
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def update(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)

# Player class
class Player(pygame.sprite.Sprite):
    REGULAR = 0
    INVERTED = 1

    def __init__(self, texture_path, punches, x, y):
        super().__init__()
        def loadAsset(texture_path):
            try:
                original_image = pygame.image.load(texture_path)
                image = pygame.transform.scale(original_image, (60, 80))
            except:
                # Create a placeholder if image doesn't load
                image = pygame.Surface((60, 80))
                image.fill(GREEN)
            return [image, pygame.transform.flip(image, True, False)]
        self.image = self.idleImage = loadAsset(texture_path)
        self.punches = list(map(loadAsset, punches))
        self.rect = self.image[Player.REGULAR].get_rect()
        self.rect.center = (x, y)
        self.health = 100
        self.velocity = 0
        self.speed = 5

    def update_texture(self, texture_path):
        try:
            original_image = pygame.image.load(texture_path)
            self.image = pygame.transform.scale(original_image, (60, 80))
        except:
            pass

# Game state
class GameState:
    MENU = 0
    CREDITS = 1
    PLAYING = 2

current_state = GameState.MENU

# Create players (initially not visible)
player1 = None
player2 = None
wall1_rect = None
wall2_rect = None

def init_game():
    global player1, player2, wall1_rect, wall2_rect

    # Convert ursina coordinates to pygame coordinates
    # Ursina: (-4, -2) to pygame: approximately (150, 300)
    player1_x = WINDOW_WIDTH // 4
    player1_y = WINDOW_HEIGHT - 100

    player2_x = 3 * WINDOW_WIDTH // 4
    player2_y = WINDOW_HEIGHT - 100

    player1 = Player('assets/idlePlayer.png', ['assets/player1Punch1.png', 'assets/player1Punch2.png'], player1_x, player1_y)
    player2 = Player('assets/idlePlayer2.png', ['assets/player2Punch1.png', 'assets/player2Punch2.png'], player2_x, player2_y)

    # Create walls (invisible boundaries)
    wall1_rect = pygame.Rect(0, 0, 50, WINDOW_HEIGHT)
    wall2_rect = pygame.Rect(WINDOW_WIDTH - 50, 0, 50, WINDOW_HEIGHT)

def lerp(a, b, t):
    """Linear interpolation"""
    return a + (b - a) * t

def draw_menu(screen):
    # Draw background
    if menu_background_img:
        screen.blit(menu_background_img, (0, 0))
    else:
        screen.fill(BLACK)

    # Create buttons
    button_width = 180
    button_height = 80

    play_button = Button(
        "Play Game",
        GREEN,
        WINDOW_WIDTH // 4 - button_width // 2,
        WINDOW_HEIGHT // 2 - button_height // 2,
        button_width,
        button_height,
        40
    )

    credits_button = Button(
        "Play Credits",
        BLUE,
        3 * WINDOW_WIDTH // 4 - button_width // 2,
        WINDOW_HEIGHT // 2 - button_height // 2,
        button_width,
        button_height,
        40
    )

    quit_button = Button(
        "Quit",
        RED,
        WINDOW_WIDTH // 4 - button_width // 2,
        3 * WINDOW_HEIGHT // 4 - button_height // 2,
        button_width,
        button_height,
        40
    )

    return play_button, credits_button, quit_button

def draw_credits(screen):
    screen.fill(BLACK)

    # Draw credits text
    font = pygame.font.Font(None, 40)
    credits_lines = [
        "Coders: Mateo, Cedric, Andrew",
        "",
        "Art: Max, Quinn, Andrew, Cedric, Mateo"
    ]

    y_offset = WINDOW_HEIGHT // 4
    for line in credits_lines:
        text_surface = font.render(line, True, WHITE)
        text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, y_offset))
        screen.blit(text_surface, text_rect)
        y_offset += 50

    # Back button
    back_button = Button(
        "Back",
        BLUE,
        WINDOW_WIDTH // 2 - 100,
        3 * WINDOW_HEIGHT // 4,
        200,
        50,
        30
    )

    return back_button

def draw_game(screen, dt):
    global player1, player2

    # Draw background
    if game_background_img:
        screen.blit(game_background_img, (0, 0))
    else:
        screen.fill(VIOLET)

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Player 1 movement (A/D keys)
    if keys[pygame.K_d] and not keys[pygame.K_a]:
        if player1.velocity < -0.01:
            player1.velocity = 0.05
        elif player1.velocity < 0.05:
            player1.velocity += dt * player1.speed / 10
    elif keys[pygame.K_a] and not keys[pygame.K_d]:
        if player1.velocity > 0.01:
            player1.velocity = -0.05
        elif player1.velocity > -0.05:
            player1.velocity -= dt * player1.speed / 10
    else:
        player1.velocity = lerp(player1.velocity, 0, 0.2)

    player1.velocity = round(player1.velocity, 3)
    if abs(player1.velocity) == 0.002:
        player1.velocity = 0

    # Player 2 movement (J/L keys)
    if keys[pygame.K_l] and not keys[pygame.K_j]:
        if player2.velocity < -0.01:
            player2.velocity = 0.05
        elif player2.velocity < 0.05:
            player2.velocity += dt * player2.speed / 10
    elif keys[pygame.K_j] and not keys[pygame.K_l]:
        if player2.velocity > 0.01:
            player2.velocity = -0.05
        elif player2.velocity > -0.05:
            player2.velocity -= dt * player2.speed / 10
    else:
        player2.velocity = lerp(player2.velocity, 0, 0.2)

    player2.velocity = round(player2.velocity, 3)
    if abs(player2.velocity) == 0.002:
        player2.velocity = 0

    # Update positions
    player1.rect.centerx += player1.velocity * 100  # Scale for pygame
    player2.rect.centerx += player2.velocity * 100

    # Update textures based on actions
    if keys[pygame.K_k]:
        player2_texture = random.choice(player2.punches)
    else:
        player2_texture = player2.idleImage

    if keys[pygame.K_s]:
        player1_texture = random.choice(player1.punches)
    else:
        player1_texture = player1.idleImage

    # Check if players should face each other
    if player1.rect.centerx > player2.rect.centerx:
        player1_texture = player1_texture[Player.INVERTED]
        player2_texture = player2_texture[Player.INVERTED]
    else:
        player1_texture = player1_texture[Player.REGULAR]
        player2_texture = player2_texture[Player.REGULAR]

    player1.image = player1_texture
    player2.image = player2_texture

    # Wall collision
    if player1.rect.left < 50:
        player1.rect.left = 50
        player1.absolute_x = player1.rect.centerx
    if player1.rect.right > WINDOW_WIDTH - 50:
        player1.rect.right = WINDOW_WIDTH - 50
        player1.absolute_x = player1.rect.centerx

    if player2.rect.left < 50:
        player2.rect.left = 50
        player2.absolute_x = player2.rect.centerx
    if player2.rect.right > WINDOW_WIDTH - 50:
        player2.rect.right = WINDOW_WIDTH - 50
        player2.absolute_x = player2.rect.centerx

    # Draw players
    screen.blit(player1.image, player1.rect)
    screen.blit(player2.image, player2.rect)

def main():
    global current_state

    running = True
    menu_buttons = None
    credits_button = None

    while running:
        dt = clock.tick(FPS) / 1000.0  # Delta time in seconds
        mouse_pos = pygame.mouse.get_pos()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if current_state == GameState.MENU and menu_buttons:
                    play_btn, credits_btn, quit_btn = menu_buttons

                    if play_btn.is_clicked(mouse_pos):
                        if sword_slash_sound:
                            sword_slash_sound.play()
                        init_game()
                        current_state = GameState.PLAYING
                    elif credits_btn.is_clicked(mouse_pos):
                        if sword_slash_sound:
                            sword_slash_sound.play()
                        current_state = GameState.CREDITS
                    elif quit_btn.is_clicked(mouse_pos):
                        if sword_slash_sound:
                            sword_slash_sound.play()
                        running = False

                elif current_state == GameState.CREDITS and credits_button:
                    if credits_button.is_clicked(mouse_pos):
                        current_state = GameState.MENU

        # Rendering
        if current_state == GameState.MENU:
            menu_buttons = draw_menu(screen)
            # Update button hover states
            for btn in menu_buttons:
                btn.update(mouse_pos)
                btn.draw(screen)

        elif current_state == GameState.CREDITS:
            credits_button = draw_credits(screen)
            credits_button.update(mouse_pos)
            credits_button.draw(screen)

        elif current_state == GameState.PLAYING:
            draw_game(screen, dt)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
