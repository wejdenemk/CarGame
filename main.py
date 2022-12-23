import os
import pygame
import random
from pygame.locals import *

size = width, height= (1200,800)
width_GO = 600
height_GO = 400
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 1

pygame.init()
running = True

#Sound Mixer
pygame.mixer.init()
s = 'sound'
ouch = pygame.mixer.Sound(os.path.join(s, 'ouch.mp3'))
move = pygame.mixer.Sound(os.path.join(s, 'move.mp3'))

play = True

#Set Windiw Size
screen = pygame.display.set_mode((size))

#Set Title
pygame.display.set_caption("Wej's Car Game")

#Set Background CoLOR
screen.fill((60, 220, 0))

#Apply Changes
pygame.display.update()

#Load Player Car
car = pygame.image.load("img/car.png")
car_loc = car.get_rect()
car_loc.center= right_lane , height*0.8

#Load Enemy Car
car2 = pygame.image.load("img/otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center= left_lane , height*0.2

#GAME OVER
end = pygame.image.load("img/gameOver.png")
end = pygame.transform.scale(end, (600,600))
end_loc = end.get_rect()
end_loc.center= ((width_GO),(height_GO))

#Game Loop
counter = 0
while running:
    if play == True : 
        counter +=1
        if counter == 5000:
            speed += 0.15
            counter = 0
            print("Level up", speed)
        car2_loc[1]+= speed
        if car2_loc[1] > height:
            if random.randint(0,1) == 0:
                car2_loc.center = right_lane, -200
            else:
                car2_loc.center = left_lane, -200

    
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key in [K_a, K_LEFT]:
                    pygame.mixer.Sound.play(move)
                    car_loc = car_loc.move([-int(road_w/2),0])
                if event.key in [K_d, K_RIGHT]:
                    pygame.mixer.Sound.play(move)
                    car_loc = car_loc.move([int(road_w/2),0])

        #Draw Graphics
        pygame.draw.rect(
            screen,
            (50,50,50),
            (width/2-road_w/2, 0, road_w, height)
        )

        pygame.draw.rect(
            screen,
            (255,240,60),
            (width/2- roadmark_w/2 , 0, roadmark_w , height)
        )

        pygame.draw.rect(
            screen,
            (255,255,255),
            (width/2- road_w/2+roadmark_w*2, 0, roadmark_w , height)
        )

        pygame.draw.rect(
            screen,
            (255,255,255),
            (width/2+ road_w/2-roadmark_w*3, 0, roadmark_w , height)
        )
        screen.blit(car , car_loc)
        screen.blit(car2 , car2_loc)

    else:
        pygame.mixer.Sound.play(ouch)
        pygame.time.delay(400) 
        screen.fill((0, 0, 0))
        screen.blit(end,end_loc)
        pygame.display.flip()
        pygame.time.delay(1000) 
        running = False 

    #Car Crash  
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        play = False
        

    pygame.display.update()
 
pygame.quit()
