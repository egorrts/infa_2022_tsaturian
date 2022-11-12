import pygame

WIDTH, HEIGHT = 500, 500
FPS_MAX = 30

pygame.init()

screen = pygame.display.set_mode((HEIGHT, WIDTH))
clock = pygame.time.Clock()
screen.fill((200, 200, 200))

pos = (HEIGHT / 2, WIDTH / 2)


def distance(pos1, pos2):
    dist_x = pos1[0] - pos2[0]
    dist_y = pos1[1] - pos2[1]
    return dist_x, dist_y

screen.fill((200, 200, 200))
pygame.draw.circle(screen, (255, 255, 0), pos, 120, 0)
pygame.draw.circle(screen, (0, 0, 0), pos, 120, 1)

pygame.draw.circle(screen, (255, 0, 0), distance(pos, (30, 15)), 18, 0)
pygame.draw.circle(screen, (0, 0, 0), distance(pos, (30, 15)), 18, 1)
pygame.draw.circle(screen, (0, 0, 0), distance(pos, (30, 15)), 8, 0)
pygame.draw.circle(screen, (255, 0, 0), distance(pos, ( - 30, 15)), 13, 0)
pygame.draw.circle(screen, (0, 0, 0), distance(pos, ( - 30, 15)), 13, 1)
pygame.draw.circle(screen, (0, 0, 0), distance(pos, ( - 30, 15)), 8, 0)

pygame.draw.polygon(screen, (0, 0, 0), [distance(pos, (40, 40)), distance(pos, (60, 60)), distance(pos, (30, 30)), distance(pos, (20, 20))], 15)
pygame.draw.polygon(screen, (0, 0, 0), [distance(pos, ( - 40, 40)), distance(pos, ( - 60, 60)), distance(pos, ( - 30, 30)), distance(pos, ( - 20, 20))], 15)
pygame.draw.rect(screen, (0, 0, 0), (pos[0] + -40, pos[1] + 40, 100, 10))

pygame.display.update()

while True:
    clock.tick(FPS_MAX)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

