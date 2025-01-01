import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        screen.fill("black")

        pygame.draw.circle(screen, "white", player_pos, 40)

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            player_pos.y -= 100 * dt
        
        if keys[pygame.K_s]:
            player_pos.y += 100 * dt
        
        if keys[pygame.K_a]:
            player_pos.x -= 100 * dt
        
        if keys[pygame.K_d]:
            player_pos.x += 100 * dt
        
        pygame.display.flip()

        dt = clock.tick(120) / 1000
    

pygame.quit()        