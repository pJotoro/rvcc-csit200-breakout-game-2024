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
# ---------------------

class Block:
    def __init__(self, x, y, width, height, color):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__color = color

    def draw(self):
        draw_rectangle(self.__x, self.__y, self.__width, self.__height, self.__color)

    def get_rectangle(self):
        return Rectangle(self.__x, self.__y, self.__width, self.__height)

def main():
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Breakout")
    set_target_fps(60)

    # ----- Initialize player and ball -----
    player_x = 400

    ball_x = SCREEN_WIDTH // 2
    ball_y = SCREEN_HEIGHT // 2
    dirs = [-1, 1]
    ball_dir_x = random.choice(dirs)
    ball_dir_y = 1
    # --------------------------------------
    
    # ----- Initialize blocks -----
    blocks = []
    for row in range(BLOCK_ROWS):
        for col in range(BLOCK_COLUMNS):
            x = col * (BLOCK_WIDTH)
            y = row * (BLOCK_HEIGHT)
            color = random.choice(COLORS)
            blocks.append(Block(x, y, BLOCK_WIDTH, BLOCK_HEIGHT, color))
    blocks_destroyed = 0
    # -----------------------------

    while not window_should_close():
        if is_key_pressed(KeyboardKey.KEY_R) or ball_y > SCREEN_HEIGHT or blocks_destroyed == BLOCK_COLUMNS*BLOCK_ROWS:
            blocks_destroyed = 0

            player_x = 400

            ball_x = SCREEN_WIDTH // 2
            ball_y = SCREEN_HEIGHT // 2
            ball_dir_x = random.choice(dirs)
            ball_dir_y = 1
            blocks.clear()
            for row in range(BLOCK_ROWS):
                for col in range(BLOCK_COLUMNS):
                    x = col * (BLOCK_WIDTH)
                    y = row * (BLOCK_HEIGHT)
                    color = random.choice(COLORS)
                    blocks.append(Block(x, y, BLOCK_WIDTH, BLOCK_HEIGHT, color))
        
        # Ball collisions with the player and wall
        if check_collision_recs(
            Rectangle(player_x, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT), 
            Rectangle(ball_x, ball_y, BALL_SIZE, BALL_SIZE)):
            ball_dir_y = -1
        elif ball_y <= 0:
            ball_dir_y = 1

        # Updates the players position
        if is_key_down(KeyboardKey.KEY_LEFT):
            player_x -= PLAYER_SPEED
        if is_key_down(KeyboardKey.KEY_RIGHT):
            player_x += PLAYER_SPEED

        # ----- Collision -----

        # Check block overlapping
        ball_block_x = ball_x // BLOCK_WIDTH
        ball_block_y = ball_y // BLOCK_HEIGHT
        if ball_block_x >= 0 and ball_block_x < BLOCK_COLUMNS and ball_block_y >= 0 and ball_block_y < BLOCK_ROWS:
            block = blocks[ball_block_y*BLOCK_COLUMNS + ball_block_x]
            if block != None and check_collision_recs(block.get_rectangle(), Rectangle(ball_x, ball_y, BALL_SIZE, BALL_SIZE)):
                assert(False, "Not supposed to already be overlapping block!")

        # Check blocks vertical
        ball_block_x = ball_x // BLOCK_WIDTH
        ball_block_y = (ball_y + ball_dir_y*BALL_SPEED) // BLOCK_HEIGHT
        if ball_block_x >= 0 and ball_block_x < BLOCK_COLUMNS and ball_block_y >= 0 and ball_block_y < BLOCK_ROWS:
            block_idx = ball_block_y*BLOCK_COLUMNS + ball_block_x
            block = blocks[block_idx]
            if block != None and check_collision_recs(block.get_rectangle(), Rectangle(ball_x, ball_y + ball_dir_y*BALL_SPEED, BALL_SIZE, BALL_SIZE)):
                ball_y = ball_block_y*BLOCK_HEIGHT - ball_dir_y*BALL_SIZE
                ball_dir_y = -ball_dir_y
                blocks[block_idx] = None
                blocks_destroyed += 1

        # Check blocks horizontal
        ball_block_x = (ball_x + ball_dir_x*BALL_SPEED) // BLOCK_WIDTH
        ball_block_y = ball_y // BLOCK_HEIGHT
        if ball_block_x >= 0 and ball_block_x < BLOCK_COLUMNS and ball_block_y >= 0 and ball_block_y < BLOCK_ROWS:
            block_idx = ball_block_y*BLOCK_COLUMNS + ball_block_x
            block = blocks[block_idx]
            if block != None and check_collision_recs(block.get_rectangle(), Rectangle(ball_x + ball_dir_x*BALL_SPEED, ball_y, BALL_SIZE, BALL_SIZE)):
                ball_x = ball_block_x*BLOCK_WIDTH - ball_dir_x*BALL_SIZE
                ball_dir_x = -ball_dir_x
                blocks[block_idx] = None
                blocks_destroyed += 1

        # ---------------------        

        # Updates ball position
        ball_x += ball_dir_x * BALL_SPEED
        ball_y += ball_dir_y * BALL_SPEED
            
        if ball_x <= 0:
            ball_dir_x = 1
        elif ball_x >= SCREEN_WIDTH - BALL_SIZE:
            ball_dir_x = -1

        begin_drawing()
        clear_background(WHITE)

        draw_rectangle(player_x, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT, BLACK)
        draw_rectangle(ball_x, ball_y, BALL_SIZE, BALL_SIZE, BLUE)
        for block in blocks:
            if block != None:
                block.draw()

        draw_text("Score: " + str(blocks_destroyed), 20, SCREEN_HEIGHT - 40, 30, GREEN)

        end_drawing()
    close_window()

if __name__ == "__main__":
    main()
