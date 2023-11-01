import pygame
import random

#Okno init
width = 640
height = 480

pygame.display.set_caption('Had by Josef Mikulka')
screen = pygame.display.set_mode((width, height))

#Barvy
background = (200, 200, 241)
snake_color = (65, 185, 105)
food_color = (255, 80, 80)

#Rychlost / FPS
FPS = pygame.time.Clock()
speed = 15

#Ostatni vars
head_pos = [100, 50]
snake = [[100, 50]]
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True
score = 0

#Hlavni cyklus
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #Ovladani
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and dir != 'R':
                dir = 'L'
            if event.key == pygame.K_RIGHT and dir != 'L':
                dir = 'R'
            if event.key == pygame.K_UP and dir != 'D':
                dir = 'U'
            if event.key == pygame.K_DOWN and dir != 'U':
                dir = 'D'
    #Pohyb
    if dir == 'L':
        head_pos[0] -= 10
    if dir == 'R':
        head_pos[0] += 10
    if dir == 'U':
        head_pos[1] -= 10
    if dir == 'D':
        head_pos[1] += 10

    #Pridej cast tela
    snake.insert(0, list(head_pos))
    print(snake) #DEBUG
    
    #Pokud na jidle nemaz
    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
        score += 1
        speed += 0.1
        print(speed) #DEBUG
        food_spawn = False
    #Jinak smaz cast (Dochazi k posunu seznamu i -> i-1)
    else:
        snake.pop()
    
    #Random spawn jidla
    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
    if food_pos not in snake:
        food_spawn = True
    
    #Vykreslovani
    screen.fill(background)
    for pos in snake:
        pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(head_pos[0], head_pos[1], 10, 10))
    pygame.draw.rect(screen, food_color, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    
    #Detekce kolize
    if head_pos[0] < 0 or head_pos[1] < 0 or head_pos[0] > width or head_pos[1] > height:
        pygame.quit()
        print("Vase skore:" + str(score))
        exit()

    for body in snake[1:]:
        if head_pos[0] == body[0] and head_pos[1] == body[1]:
            pygame.quit()
            print("Vase skore:" + str(score))
            exit()

    pygame.display.update()
    FPS.tick(speed)