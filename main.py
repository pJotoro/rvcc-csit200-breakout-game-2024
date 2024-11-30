from pyray import *

# ----- Constants -----
PLAYER_Y = 420
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 10
PLAYER_SPEED = 8

BALL_SIZE = 50
BALL_SPEED = 3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

BLOCK_WIDTH = 60
BLOCK_HEIGHT = 20
BLOCK_ROWS = 5
BLOCK_COLUMNS = 10
# ---------------------

def main():
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Breakout")
    set_target_fps(60)

    # ----- Initialize player and ball -----
    player_pos = 400

    ball_x = SCREEN_WIDTH // 2
    ball_y = SCREEN_HEIGHT // 2
    ball_dir_x = 1
    ball_dir_y = 1
    # --------------------------------------
    
    # ----- Initialize blocks -----
    blocks = []
    for row in range(BLOCK_ROWS):
        for col in range(BLOCK_COLUMNS):
            x = col * (BLOCK_WIDTH + 10) + 20
            y = row * (BLOCK_HEIGHT + 10) + 20
            blocks.append(Rectangle(x, y, BLOCK_WIDTH, BLOCK_HEIGHT))
    # -----------------------------

    while not window_should_close():
        if is_key_pressed(KeyboardKey.KEY_R):
            # TODO(Jonas): How can we avoid repeating this? Maybe with a class?
            # Reset game state if 'R' is pressed
            player_pos = 400

            ball_x = SCREEN_WIDTH // 2
            ball_y = SCREEN_HEIGHT // 2
            ball_dir_x = 1
            ball_dir_y = 1
            blocks.clear()
            for row in range(BLOCK_ROWS):
                for col in range(BLOCK_COLUMNS):
                    x = col * (BLOCK_WIDTH + 10) + 20
                    y = row * (BLOCK_HEIGHT + 10) + 20
                    blocks.append(Rectangle(x, y, BLOCK_WIDTH, BLOCK_HEIGHT))
        
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
        for block in blocks[:]:
            if check_collision_recs(
                Rectangle(block.x, block.y, block.width, block.height), 
                Rectangle(ball_x, ball_y, BALL_SIZE, BALL_SIZE)):
                blocks.remove(block)
                ball_dir_y *= -1

        begin_drawing()
        clear_background(WHITE)

        draw_rectangle(player_pos, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT, BLACK)
        draw_rectangle(ball_x, ball_y, BALL_SIZE, BALL_SIZE, BLUE)
        for block in blocks:
            draw_rectangle_rec(block, RED)
            
        end_drawing()
    close_window()

if __name__ == "__main__":
    main()
