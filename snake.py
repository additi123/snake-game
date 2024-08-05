import pygame
import random

### Initialization
pygame.init()
font = pygame.font.SysFont('Arial', 30)

# Colours
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Update the size of the snake and fruit
snake_size = 20  
snake_speed = 15
snake_x = screen_width / 2
snake_y = screen_height / 2
snake_length = 1
snake_blocks = []

fruit_x = 300
fruit_y = 400

speed_x = 0
speed_y = 0

game_over = False

running = True
clock = pygame.time.Clock()

def reset_game():
    global snake_x, snake_y, snake_blocks, snake_length, speed_x, speed_y, fruit_x, fruit_y, game_over
    snake_x = screen_width / 2
    snake_y = screen_height / 2
    snake_blocks = []
    snake_length = 1
    speed_x = 0
    speed_y = 0
    fruit_x = round(random.randrange(0, screen_width - snake_size) / snake_size) * snake_size
    fruit_y = round(random.randrange(0, screen_height - snake_size) / snake_size) * snake_size
    game_over = False

# Game Loop
while running:
    if not game_over:
        screen.fill(black)  

        # Update snake position
        snake_x += speed_x
        snake_y += speed_y

        # Add new head to the snake
        snake_head = [snake_x, snake_y]
        snake_blocks.append(snake_head)

        # Remove the tail segment if snake length exceeds
        if len(snake_blocks) > snake_length:
            del snake_blocks[0]

        # Check if snake collides with itself
        if snake_head in snake_blocks[:-1]:
            game_over = True

        # Check if snake hits the boundaries
        if (snake_x >= screen_width or snake_x < 0 or
            snake_y >= screen_height or snake_y < 0):
            game_over = True

        # Draw snake
        for block in snake_blocks:
            pygame.draw.rect(screen, blue, [block[0], block[1], snake_size, snake_size])

        # Draw fruit
        pygame.draw.rect(screen, red, [fruit_x, fruit_y, snake_size, snake_size])

        # Check if snake eats the fruit
        if snake_x == fruit_x and snake_y == fruit_y:
            fruit_x = round(random.randrange(0, screen_width - snake_size) / snake_size) * snake_size
            fruit_y = round(random.randrange(0, screen_height - snake_size) / snake_size) * snake_size
            snake_length += 1

    else:
        # Game over screen
        screen.fill(blue)
        score = font.render('You scored ' + str(snake_length - 1), True, black)  # -1 to match length
        screen.blit(score, (10, screen_height / 2 - 50))
        text = font.render('You lost! Press \'Q\' to quit, or Spacebar to play again', True, black)
        screen.blit(text, (10, screen_height / 2))

    pygame.display.flip()
    clock.tick(snake_speed)

    ### Event Loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_SPACE:
                reset_game()
            if event.key == pygame.K_UP and speed_y == 0:
                speed_x = 0
                speed_y = -snake_size
            if event.key == pygame.K_DOWN and speed_y == 0:
                speed_x = 0
                speed_y = snake_size
            if event.key == pygame.K_LEFT and speed_x == 0:
                speed_x = -snake_size
                speed_y = 0
            if event.key == pygame.K_RIGHT and speed_x == 0:
                speed_x = snake_size
                speed_y = 0
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
