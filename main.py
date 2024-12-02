from pyray import *
import random

# ----- Constants -----
PLAYER_Y = 420
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 10
PLAYER_SPEED = 8

BALL_SIZE = 20
BALL_SPEED = 3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

BLOCK_WIDTH = 50
BLOCK_HEIGHT = 20
BLOCK_ROWS = 5
BLOCK_COLUMNS = SCREEN_WIDTH // BLOCK_WIDTH

COLORS = [DARKGRAY,
          MAROON,
          ORANGE,
          DARKGREEN,
          DARKBLUE,
          DARKPURPLE,
          DARKBROWN,
          GRAY,
          RED,
          GOLD,
          LIME,
          BLUE,
          VIOLET,
          BROWN,
          LIGHTGRAY,
          PINK,
          YELLOW,
          GREEN,
          SKYBLUE,
          PURPLE,
          BEIGE]

POWERUP_SIZE = 15
POWERUP_SPEED = 3
POWERUP_EFFECTS = ["widen", "slow_ball", "extra_life"]
# ---------------------



class Block:
    def __init__(self, x, y, width, height, color):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__color = color
        self.__powerup = powerup

    def draw(self):
        draw_rectangle(self.__x, self.__y, self.__width, self.__height, self.__color)

    def get_rectangle(self):
        return Rectangle(self.__x, self.__y, self.__width, self.__height)

    def has_powerup(self):
              return self.__powerup

    def get_powerup(self):
              return self.__powerup
class Powerup:
    def __init__(self, x, y, effect):
        self.x = x
        self.y = y
        self.effect = effect

    def draw(self):
        draw_circle(self.x, self.y, POWERUP_SIZE, GOLD)

    def update(self):
        self.y += POWERUP_SPEED

    def get_rectangle(self):
        return Rectangle(self.x - POWERUP_SIZE, self.y - POWERUP_SIZE, POWERUP_SIZE * 2, POWERUP_SIZE * 2)   
          

def main():
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Breakout")
    set_target_fps(60)

    # ----- Initialize player and ball -----
    player_pos = 400

    ball_x = SCREEN_WIDTH // 2
    ball_y = SCREEN_HEIGHT // 2
    dirs = [-1, 1]
    ball_dir_x = random.choice(dirs)
    ball_dir_y = 1
    powerups = []
    # --------------------------------------
    
    # ----- Initialize blocks -----
    blocks = []
    for row in range(BLOCK_ROWS):
        for col in range(BLOCK_COLUMNS):
            x = col * (BLOCK_WIDTH)
            y = row * (BLOCK_HEIGHT)
            color = random.choice(COLORS)
            powerup = random.choice(POWERUP_EFFECTS) if random.random() < 0.15 else none
            blocks.append(Block(x, y, BLOCK_WIDTH, BLOCK_HEIGHT, color, powerup))
    # -----------------------------

    while not window_should_close():
        if is_key_pressed(KeyboardKey.KEY_R) or ball_y > SCREEN_HEIGHT:
            player_pos = 400

            ball_x = SCREEN_WIDTH // 2
            ball_y = SCREEN_HEIGHT // 2
            ball_dir_x = random.choice(dirs)
            ball_dir_y = 1
            blocks.clear()
            powerups.clear()
            for row in range(BLOCK_ROWS):
                for col in range(BLOCK_COLUMNS):
                    x = col * (BLOCK_WIDTH)
                    y = row * (BLOCK_HEIGHT)
                    color = random.choice(COLORS)
                    powerup = random.choice(POWERUP_EFFECTS) if random.random() < 0.15 else none
                    blocks.append(Block(x, y, BLOCK_WIDTH, BLOCK_HEIGHT, color, powerup))
        
        # Updates the players position
        if is_key_down(KeyboardKey.KEY_LEFT):
            player_pos -= PLAYER_SPEED
        if is_key_down(KeyboardKey.KEY_RIGHT):
            player_pos += PLAYER_SPEED
            
        # Updates ball position
        ball_x += ball_dir_x * BALL_SPEED
        ball_y += ball_dir_y * BALL_SPEED
        
        # Ball collisions with the player and wall
        if check_collision_recs(
            Rectangle(player_pos, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT), 
            Rectangle(ball_x, ball_y, BALL_SIZE, BALL_SIZE)):
            ball_dir_y = -1
        elif ball_y <= 0:
            ball_dir_y = 1

        if ball_x <= 0:
            ball_dir_x = 1
        elif ball_x >= SCREEN_WIDTH - BALL_SIZE:
            ball_dir_x = -1

        # if ball hits block
        block_idx = 0
        while block_idx < len(blocks):
            block = blocks[block_idx]
            if check_collision_recs(
                block.get_rectangle(), 
                Rectangle(ball_x, ball_y, BALL_SIZE, BALL_SIZE)):
                ball_dir_y *= -1

                    if block.has_powerup():
                              powerup_effect = block.get_powerup()
                              powerups.append(PowerUp(block.get_rectangle().x + BLOCK_WIDTH // 2, block.get_rectangle().y, powerup_effect))

                    blocks.pop(block_idx)
          else:
                    block_idx += 1
          # draws power ups
          powerup_idx = 0
          while powerup_idx < len(powerups):
                    powerup = powerups[powerup_idx]
                    powerup.update()

                    if powerup.y > SCREEN_HEIGHT
                              powerups.pop(powerup_idx)
                    elif check_collision_recs(
                              Rectangle(player_pos, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT),
                              powerup.get_rectangle()):
                    if powerup.effect == "widen":
                              PLAYER_WIDTH =+ 10 # makes the pad wider
                    elif powerup.effect == "slow_ball":
                              BALL_SPEED = max(1, BALL_SPEED -1) # makes the ball move slower
                    elif powerup.effect == "extra_life":
                              print("You got an extra life!") # gives you an extra life
                    powerups.pop(powerup_idx)
                    else:
                     powerup_idx += 1
          

          

        begin_drawing()
        clear_background(WHITE)

        draw_rectangle(player_pos, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT, BLACK)
        draw_rectangle(ball_x, ball_y, BALL_SIZE, BALL_SIZE, BLUE)
        for block in blocks:
            block.draw()

        for powerup in powerups
              powerup.draw()

        end_drawing()
    close_window()

if __name__ == "__main__":
    main()
