import pygame
import random
import time
CELL_SIZE = 30
WIDTH = 20 * CELL_SIZE
HEIGHT = 20 * CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PathFinder")

def draw_labirent(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            color = WHITE
            if maze[row][col] == 1:
                color = BLACK
            elif maze[row][col] == 2:
                color = GREEN
            elif maze[row][col] == 3:
                color = BLUE
            elif maze[row][col] == 4:
                color = RED
            elif maze[row][col] == 5:
                color = ORANGE

            pygame.draw.rect(screen, color, pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen,RED,pygame.Rect(0,0,CELL_SIZE,CELL_SIZE))
            pygame.draw.rect(screen,ORANGE,pygame.Rect(570,570,CELL_SIZE,CELL_SIZE))
    
    pygame.display.flip()

def etrafi_bul(maze, satır, sütun):
    etraf = []
    try:
        etraf.append(maze[satır][sütun+1])
    except:
        etraf.append(-1)
    try:
        if sütun-1 < 0:
            etraf.append(-1)
        else:
            etraf.append(maze[satır][sütun-1])
    except:
        etraf.append(-1)
    try:
        etraf.append(maze[satır+1][sütun])
    except:
        etraf.append(-1)
    try:
        if satır-1 < 0:
            etraf.append(-1)
        else:
            etraf.append(maze[satır-1][sütun])
    except:
        etraf.append(-1)
    
    return etraf

def hareket(satır,sütun,index):
    if index == 0:  # sağ
        sütun += 1
    elif index == 1:  # sol
        sütun -= 1
    elif index == 2:  # aşağı
        satır += 1
    else:  # yukarı
        satır -= 1
    return satır , sütun
font = pygame.font.Font(None, 70)
text = font.render("ULAŞTINIZ",True,(255,0,0))

running = True
satır = 0
sütun = 0


maze = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]]


while running:
    screen.fill(WHITE)
    draw_labirent(maze)
    etraf = etrafi_bul(maze, satır, sütun)
    if 0 in etraf:
        index = etraf.index(0)
        satır , sütun = hareket(satır,sütun,index)
        maze[satır][sütun] = 2
    elif 2 in etraf:
        maze[satır][sütun] = 3
        index = etraf.index(2)
        satır , sütun = hareket(satır,sütun,index)
    else:
        back = False #geri dönüş sıkıştığında
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if (maze[i][j] == 2) and (0 in etrafi_bul(maze,i,j)):
                    satır=i
                    sütun=j
                    back = True
        if not back:  #geri dönemesse bitir
            print(satır,sütun)
            print("çzülemez")
            running = False
            break
    if satır == len(maze)-1 and sütun == len(maze[0])-1: #bitiş kontrol
        screen.blit(text,(HEIGHT/2,WIDTH/2))
        pygame.display.flip()
        print("Ulaştınız!")
        running = False
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
time.sleep(1)

pygame.quit()