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
    player_pos = 400

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
    # -----------------------------

    while not window_should_close():
        if is_key_pressed(KeyboardKey.KEY_R) or ball_y > SCREEN_HEIGHT:
            player_pos = 400

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

                blocks.pop(block_idx)
            else:
                block_idx += 1

        begin_drawing()
        clear_background(WHITE)

        draw_rectangle(player_pos, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT, BLACK)
        draw_rectangle(ball_x, ball_y, BALL_SIZE, BALL_SIZE, BLUE)
        for block in blocks:
            block.draw()

        end_drawing()
    close_window()

if __name__ == "__main__":
    main()
