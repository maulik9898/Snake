import random

import pygame
from Snake.Axis import Axis
from Snake.Snake import Snake

snake = Snake(600, 600, 15)


def food_spawn():
    x = random.randrange(0, snake.width, snake.size)
    y = random.randrange(0, snake.height, snake.size)
    return Axis(x, y)


pygame.init()

screen = pygame.display.set_mode((snake.height, snake.width))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

running = True
current_food = food_spawn()
pygame.draw.rect(screen, (0, 255, 0), [current_food.x, current_food.y, snake.size, snake.size])
pygame.display.update()
dead = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.change_direction(0, 1)
            if event.key == pygame.K_UP:
                snake.change_direction(0, -1)
                prev = pygame.K_UP
            if event.key == pygame.K_LEFT:
                snake.change_direction(-1, 0)
            if event.key == pygame.K_RIGHT:
                snake.change_direction(1, 0)
            if event.key == pygame.K_p:
                dead = False
                snake = Snake(600, 600, 15)
                snake.position.y = snake.height // 2
                snake.position.x = snake.width // 2
                current_food = food_spawn()
    if dead:
        screen.fill((125, 125, 125))
        g_font = pygame.font.Font('freesansbold.ttf', 32)
        p_font = pygame.font.Font('freesansbold.ttf', 16)
        game_over_text = g_font.render('Game Over : ' + str(snake.total), True, (0, 255, 0))
        play_text = g_font.render('Press "P" to play again ', True, (0, 0, 255))
        textRect = game_over_text.get_rect()
        play_rect = play_text.get_rect()
        textRect.center = (snake.width // 2, snake.height // 2)
        play_rect.center = (snake.width // 2, snake.height // 2 + 50)
        screen.blit(game_over_text, textRect)
        screen.blit(play_text, play_rect)

    else:
        screen.fill((0, 0, 0))
        pygame.display.update()
        if current_food.x == snake.position.x and current_food.y == snake.position.y:
            current_food = food_spawn()
            pygame.draw.rect(screen, (0, 255, 0), [current_food.x, current_food.y, snake.size, snake.size])
            snake.eat_food()
        if not snake.move_snake(snake.width, snake.height):
            dead = True
        pygame.draw.rect(screen, (0, 255, 0), [current_food.x, current_food.y, snake.size, snake.size])
        for i in range(0, len(snake.tail)):
            pygame.draw.rect(screen, (255, 255, 255), [snake.tail[i].x, snake.tail[i].y, snake.size, snake.size])

        pygame.draw.rect(screen, (255, 255, 255), [snake.position.x, snake.position.y, snake.size, snake.size])
    pygame.display.update()
    clock.tick(10)
