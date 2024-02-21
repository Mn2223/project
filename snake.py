import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define the size of each grid cell and the number of cells in the grid
cell_size = 20
grid_width = width // cell_size
grid_height = height // cell_size

# Initialize the snake's position and direction
snake_pos = [(grid_width // 2, grid_height // 2)]
snake_dir = (1, 0)

# Initialize the food's position
food_pos = (random.randint(0, grid_width - 1), random.randint(0, grid_height - 1))

# Initialize the score and game over flag
score = 0
game_over = False

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Get the current state of the keyboard arrow keys
    keys = pygame.key.get_pressed()

    # Change the snake's direction based on arrow key input
    if keys[pygame.K_UP] and snake_dir != (0, 1):
        snake_dir = (0, -1)
    elif keys[pygame.K_DOWN] and snake_dir != (0, -1):
        snake_dir = (0, 1)
    elif keys[pygame.K_LEFT] and snake_dir != (1, 0):
        snake_dir = (-1, 0)
    elif keys[pygame.K_RIGHT] and snake_dir != (-1, 0):
        snake_dir = (1, 0)

    # Update the snake's position
    x, y = snake_pos[0]
    dx, dy = snake_dir
    new_pos = ((x + dx) % grid_width, (y + dy) % grid_height)

    # Check if the snake has collided with itself
    if new_pos in snake_pos:
        game_over = True

    # Check if the snake has collided with the food
    if new_pos == food_pos:
        score += 1
        food_pos = (random.randint(0, grid_width - 1), random.randint(0, grid_height - 1))
    else:
        # Remove the tail of the snake if it hasn't eaten food
        snake_pos.pop()

    # Add the new head to the front of the snake
    snake_pos.insert(0, new_pos)

    # Clear the window
    window.fill(BLACK)

    # Draw the food
    pygame.draw.rect(window, RED, (food_pos[0] * cell_size, food_pos[1] * cell_size, cell_size, cell_size))

    # Draw the snake
    for pos in snake_pos:
        pygame.draw.rect(window, GREEN, (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to control game speed
    clock.tick(10)

# Game over message
print("Game Over")
print("Your Score:", score)

# Quit Pygame
pygame.quit()
