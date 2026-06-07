import pygame
from pygame.locals import *
from entities import Snake, Apple   

pygame.init()
clock = pygame.time.Clock()

#Consts
CELL_SIZE = 30
GRID_WIDTH = 20
GRID_HEIGHT = 15
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
REFRESH_RATE = 10
APPLE_IMAGE_PATH = r"C:\Users\ehudg\Maple_Related\Python_proj\Helpers\Apple_Sprite.png"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game for Ernik")

def main():
    snake = Snake(GRID_WIDTH // 2, GRID_HEIGHT // 2, color=(0, 255, 0))
    apple = Apple(GRID_WIDTH, GRID_HEIGHT, CELL_SIZE, APPLE_IMAGE_PATH)
    entities = [snake, apple]
    score = 0
    running = True
    
    while running:
        #event handaling
        for event in pygame.event.get():
           
            #Closing game window
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            
            #Moving with arrows. preventing moving opposite direction
            if event.type == KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    snake.direction = (1, 0)
        
        #Making sure snake is moving only if has directions
        if snake.direction != (0, 0):
            snake.move()
            
            #Did the snake ate an apple? -> grow tail and respawn an apple
            if snake.head == (apple.x, apple.y):
                snake.grow_tail()
                apple.respawn(snake.body)
                score += 1
                print(f"Score: {score}")
            
            #Did the snake crashed? -> kill, 
            if snake.check_collisions(GRID_WIDTH, GRID_HEIGHT):
                print(f"Game Over! Final Score: {score}")
                snake = Snake(GRID_WIDTH // 2, GRID_HEIGHT // 2, color=(0, 255, 0))
                apple.respawn(snake.body)
                score = 0
                entities = [snake, apple]
        
        #Deleting last frame
        screen.fill((30, 30, 30))
        
        #Using duck-typing (thanks to Darshan) to draw entities
        for entity in entities:
            entity.draw(screen, CELL_SIZE)
        
        pygame.display.flip()
        clock.tick(REFRESH_RATE)
    
    pygame.quit()

if __name__ == "__main__":
    main()