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

def check_around(maze, row, column):
    etraf = []
    try:
        etraf.append(maze[row][column+1])
    except:
        etraf.append(-1)
    try:
        if column-1 < 0:
            etraf.append(-1)
        else:
            etraf.append(maze[row][column-1])
    except:
        etraf.append(-1)
    try:
        etraf.append(maze[row+1][column])
    except:
        etraf.append(-1)
    try:
        if row-1 < 0:
            etraf.append(-1)
        else:
            etraf.append(maze[row-1][column])
    except:
        etraf.append(-1)
    
    return etraf

def movement(row,column,index):
    if index == 0:  #right
        column += 1
    elif index == 1:  #left
        column -= 1
    elif index == 2:  #down
        row += 1
    else:  #up
        row -= 1
    return row , column
font = pygame.font.Font(None, 70)
text = font.render("Solvable",True,(255,0,0))

running = True
row = 0
column = 0


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
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]]


while running:
    screen.fill(WHITE)
    draw_labirent(maze)
    etraf = check_around(maze, row, column)
    if 0 in etraf:
        index = etraf.index(0)
        row , column = movement(row,column,index)
        maze[row][column] = 2
    elif 2 in etraf:
        maze[row][column] = 3
        index = etraf.index(2)
        row , column = movement(row,column,index)
    else:
        back = False #check any possible ways if it stucks
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if (maze[i][j] == 2) and (0 in check_around(maze,i,j)):
                    row=i
                    column=j
                    back = True
        if not back:  #if not solvable end it
            print(row,column)
            print("çzülemez")
            running = False
            break
    if row == len(maze)-1 and column == len(maze[0])-1: #finish check
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