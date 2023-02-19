import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the game screen
screen_width = 1366
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))

# Load images and sounds
ghost_image = pygame.image.load("ghost.png")
dot_image = pygame.image.load("dot1.png")
chomp_sound = pygame.mixer.Sound("Bite.mp3")
background_image = pygame.image.load("background2.png")


# Define game objects
ghost = pygame.Surface((51, 51))
ghost.blit(ghost_image, (0, 0))
dot = pygame.Surface((20, 20))
dot.blit(dot_image, (0, 0))
background = pygame.Surface((screen_width, screen_height))
background.blit(background_image, (0, 0))

# screen.blit(background, (0, 0))

# Set the initial position of the ghost
ghost_x = screen_width / 2
ghost_y = screen_height / 2

# Set the initial position of the dot
dot_x = random.randint(0, screen_width - 51)
dot_y = random.randint(0, screen_height - 51)

# Set up the game loop
start_time = time.time()
running = True
score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the ghost based on user input
    keys = pygame.key.get_pressed()
    speed = 0.5
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        speed = 1.2
    if keys[pygame.K_w]:
        ghost_y -= speed
    if keys[pygame.K_a]:
        ghost_x -= speed
    if keys[pygame.K_s]:
        ghost_y += speed
    if keys[pygame.K_d]:
        ghost_x += speed
        
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    if ghost_x < 0:
        ghost_x = 0
    if ghost_x > screen_width - 51:
        ghost_x = screen_width - 51
    if ghost_y < 0:
        ghost_y = 0
    if ghost_y > screen_height - 51:
        ghost_y = screen_height - 51

    
# Check for collisions between the ghost and dot
    if (ghost_x < dot_x + 20) and (ghost_x + 51 > dot_x) and (ghost_y < dot_y + 20) and (ghost_y + 51 > dot_y):
        dot_x = random.randint(0, screen_width - 20)
        dot_y = random.randint(0, screen_height - 20)
        score += 1
        chomp_sound.play()

    
    # End the game after 30 seconds
    if time.time() - start_time >= 30:
        running = False
    
    # Draw the game objects on the screen
    screen.blit(background, (0, 0))
    # screen.fill((0, 0, 0))
    screen.blit(ghost, (ghost_x, ghost_y))
    screen.blit(dot, (dot_x, dot_y))
    
    # Display the score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Calculate the remaining time
    remaining_time = 30 - (time.time() - start_time)

    # Display the countdown
    countdown_text = font.render("Time: " + str(int(remaining_time)), True, (255, 255, 255))
    screen.blit(countdown_text, (screen_width - 150, 10))
    
    # Update the display
    pygame.display.update()
# Set up the game over loop
game_over = True
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_over = False
                # Reset the game variables
                start_time = time.time()
                running = True
                score = 0
                ghost_x = screen_width / 2
                ghost_y = screen_height / 2
                dot_x = random.randint(0, screen_width - 51)
                dot_y = random.randint(0, screen_height - 51)
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()

    # Draw the game over screen
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    game_over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (screen_width / 2 - 100, screen_height / 2 - 50))
    score_text = font.render("SCORE : " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (screen_width / 2 - 100, screen_height / 2 + 50))
    # play_again_text = font.render("Press Enter to Play Again", True, (255, 255, 255))
    # screen.blit(play_again_text, (screen_width / 2 - 100, screen_height / 2 + 50))
    # quit_text = font.render("Press Escape to Quit", True, (255, 255, 255))
    # screen.blit(quit_text, (screen_width / 2 - 80, screen_height / 2 + 100))

    # Update the display
    pygame.display.update()


# Quit the game
pygame.quit()
