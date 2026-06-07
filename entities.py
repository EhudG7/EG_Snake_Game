import pygame
import random

class GameObject:
    def __init__(self, x_pos, y_pos, color):
        self.x = x_pos
        self.y = y_pos
        self.color = color
    
    def draw (self, surface, block_size):
        rect = pygame.Rect(self.x * block_size, self.y * block_size, block_size, block_size)
        pygame.draw.rect(surface, self.color, rect)
    
        
class Snake(GameObject):
    def __init__(self, x_pos, y_pos, color=(0, 255, 0)):
        super().__init__(x_pos, y_pos, color)
        self.body = [(x_pos, y_pos), (x_pos-1, y_pos), (x_pos-2, y_pos)]
        self.direction = (0, 0)
        self.remove_tail = True
    
    #Insted of writing a getter function - treats the head a normal attribute
    @property
    def head(self):
        return self.body[0]
    
    #Updating snake direction based on the current direction
    def move(self):
        head_x, head_y = self.head
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        #Inserting new head position to the begginig of the list (which is the head)
        self.body.insert(0, new_head)
        
        #checking if there's a need cut off the tail (in case an apple wasn't eaten), if not than reseting
        if self.remove_tail:
            self.body.pop()
        else:
            self.remove_tail = True
    
    #we'll use it when eating and apple - making the game not cutting the tail in next step
    def grow_tail(self):
        self.remove_tail = False  
        
    def check_collisions(self, grid_width, grid_height):
        head_x, head_y = self.head
        
        #checking walls collisions. than in loop game if True show game over
        if head_x < 0 or head_x >= grid_width or head_y < 0 or head_y >= grid_height:
            return True
        #checking the head cordinates are found in the bosy list starting from index [1]
        if self.head in self.body[1:]:
            return True

        return False
    
    def draw(self, surface, cell_size):
        
        #actually polymorphism of the parent class GsmeObject's draw method
        for segment in self.body:
            rect = pygame.Rect(segment[0] * cell_size, segment[1] * cell_size, cell_size, cell_size)
            pygame.draw.rect(surface, self.color, rect)

class Apple(GameObject):
    def __init__(self, grid_width, grid_height, cell_size, image_path):
        self.grid_width = grid_width
        self.grid_height = grid_height
        
        start_x = random.randint(0, grid_width - 1)
        start_y = random.randint(0, grid_height - 1)
        
        super().__init__(start_x, start_y, color=None)
        
        self.original_image = pygame.image.load(r"C:\Users\ehudg\Maple_Related\Python_proj\Helpers\Apple_Sprite.png").convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (cell_size, cell_size))
        

    def respawn(self, snake_body):
        #A group that includes all of our cordiantes
        #Using list comperhension to transform to a set
        all_positions = set((x, y) for x in range(self.grid_width) for y in range(self.grid_height))
        snake_positions = set(snake_body)
        
        #Checking all free blocks and putting them in a new list
        available_positions = list(all_positions - snake_positions)
        
        #If the available_positions isn't empty, using random.choice to randomly choose a coordinate 
        if available_positions:
            new_pos = random.choice(available_positions)
            self.x, self.y = new_pos
    
    def draw(self, surface, cell_size):
        x_pixel = self.x * cell_size
        y_pixel = self.y * cell_size
        surface.blit(self.image, (x_pixel, y_pixel))