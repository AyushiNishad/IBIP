import pygame
import random

pygame.init()

screen_width = 700
screen_height = 600

green = (0,255,0)
red = (255,0,0)
white=(255,255,255)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None,35)
def draw_text(text,x,y):
    score_text = font.render(text,True,white)
    screen.blit(score_text,(x,y))

class Snake:
    def __init__(self):
        self.body =[(200,100),(190,100),(180,100)]
        self.direction = (10,0)
        self.grow = False

    def update(self):
        #new_head = (self.body[0][0]+self.direction[0], self.body[0][1]+self.direction[1])
        new_x = (self.body[0][0] + self.direction[0]) % screen_width
        new_y = (self.body[0][1] + self.direction[1]) % screen_height
        new_head = (new_x,new_y)
        if new_head in self.body[1:]:
            return False
        self.body.insert(0,new_head)
        if self.grow:
             self.grow = False
        else:
             self.body.pop()

        return True     
             
             


    def  change_direction(self, direction):
          if(direction[0], direction[1]) != (-self.direction[0], -self.direction[1]):
              self.direction = direction

    def grow_snake(self):
           self.grow = True

    def draw(self):
          for segment in self.body:
              pygame.draw.rect(screen, green, pygame.Rect(segment[0],segment[1], 10, 10))

class Food:
    def __init__(self):
        self.respawn()
        #self.position = (random.randint(0, (screen_width - 10)//10)*10,
                     # random.randint(0, (screen_height - 10)//10)*10)


    def respawn(self):
            self.position = (random.randint(0, (screen_width - 10)//10)*10,
                      random.randint(0, (screen_height -10)//10)*10)

    def draw(self):
             pygame.draw.rect(screen, red, pygame.Rect(self.position[0],self.position[1], 10, 10))
             
snake = Snake()
food = Food()
score = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0,-10))
                
            if event.key == pygame.K_DOWN:
                snake.change_direction((0,10))

            if event.key == pygame.K_LEFT:
                snake.change_direction((-10,0))

            if event.key == pygame.K_RIGHT:
                snake.change_direction((10,0))
    if not snake.update():
        print("Game Over!Final Score:",score)
        run = False

    if snake.body[0] == food.position:
        snake.grow_snake()
        food.respawn()
        score += 1

    screen.fill((0,0,0))
    snake.draw()
    food.draw()
    draw_text(f"Score:{score}",10,10)


    pygame.display.flip()
    clock.tick(15)

pygame.quit()    
            
            
            


            

            
                                     



                               

    
           
