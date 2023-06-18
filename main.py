import pygame, random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 700, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge block")

# Set up the clock
clock = pygame.time.Clock()

#player
player_size = 30
playerx = WIDTH / 2 - player_size//2
playery = 400
playerx_change = 0
def player_move():
  pygame.draw.rect(screen, (255, 0, 0), (playerx, playery, player_size, player_size))

#obstacle
obstacle_sizes = []
obstaclexs = []
obstacleys = []
obstacles = 3
obstacley_change = 4

for _ in range(obstacles):
  obstacle_sizes.append(40)
  obstaclexs.append(random.randint(55, 662))
  obstacleys.append(random.randint(-120, -50))

def obstacle_move(obstaclex, obstacley, obstacle_size):
  pygame.draw.rect(screen, (0, 255, 0), (obstaclex, obstacley, obstacle_size, obstacle_size))

#score
score_value = 0
score_size = 32
font_path = "Anton-Regular.ttf" 
font = pygame.font.Font(font_path, score_size)
scorex = 0
scorey= 0
def score():
  score_text = font.render("Score : " + str(score_value), True, "brown")
  screen.blit(score_text, (scorex, scorey))

# Main game loop
running = True
while running:
    # Draw to the screen
    screen.fill((0, 0, 255))
    # Draw other game elements here
    player_move()
    score()
    for obstacle in range(obstacles):
      
      obstacleys[obstacle] += obstacley_change
      
    # if obstacle already at the bottom
      if obstacleys[obstacle] >= 530:
        score_value += 1
        obstacleys[obstacle] = -50
        obstaclexs[obstacle] = random.randint(55,662)

      obstacle_move(obstaclexs[obstacle], obstacleys[obstacle], obstacle_sizes[obstacle])

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
              playerx_change = -5
            elif event.key == pygame.K_RIGHT:
              playerx_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0


    # Update game logic
    playerx += playerx_change

    # if player hit wall
    if playerx >= 672:
      playerx = 672
    elif playerx <= 0:
      playerx = 0

    # collision
    player_rect = pygame.Rect(playerx, playery, player_size, player_size)
    for obstacle in range(obstacles):
        obstacle_rect = pygame.Rect(obstaclexs[obstacle], obstacleys[obstacle], obstacle_sizes[obstacle], obstacle_sizes[obstacle])
        if player_rect.colliderect(obstacle_rect):
            score_size = 60
            scorex = (WIDTH // 2 - score_size // 2) - 50
            scorey = HEIGHT // 2 - score_size // 2
            for obstacle in range(obstacles):
              obstacleys[obstacle] = -60
            obstacley_change = 0
      
    # Update the display
    pygame.display.update()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Clean up
pygame.quit()