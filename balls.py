import pygame
import sys
from math import *
import random

pygame.init()
width = 660
height = 360
outerHeight = 400
margin = 30
display = pygame.display.set_mode((width, outerHeight))
pygame.display.set_caption("8 Ball Pool")
clock = pygame.time.Clock()

background = (51, 51, 51)
white = (236, 240, 241)
gray = (123, 125, 125)
black = (23, 32, 42)
blue = (52, 152, 219)
red = (203, 67, 53)
orange = (230, 126, 34)
stickColor = (249, 231, 159)

colors = [blue, red, orange]

balls = []
noBalls = 15
radius = 10
friction = 0.005

# Ball Class
class Ball:
    def __init__(self, x, y, speed, color, angle, ballNum):
        self.x = x + radius
        self.y = y + radius
        self.color = color
        self.angle = angle
        self.speed = speed
        self.ballNum = ballNum
        self.font = pygame.font.SysFont("Agency FB", 10)

    # Draws Balls on Display Window
    def draw(self, x, y):
        pygame.draw.ellipse(display, self.color, (x - radius, y - radius, radius*2, radius*2))
        if self.color == black or self.ballNum == "cue":
            ballNo = self.font.render(str(self.ballNum), True, white)
        else:
            ballNo = self.font.render(str(self.ballNum), True, black)

            if int(self.ballNum) > 9:
                display.blit(ballNo, (x - 6, y - 5))
            else:
                display.blit(ballNo, (x - 5, y - 5))

    # Moves the Ball around the Screen
    def move(self):
        self.speed -= friction
        if self.speed <= 0:
            self.speed = 0
        self.x = self.x + self.speed*cos(radians(self.angle))
        self.y = self.y + self.speed*sin(radians(self.angle))

        if not (self.x < width - radius - margin):
            self.x = width - radius - margin
            self.angle = 180 - self.angle
        if not(radius + margin < self.x):
            self.x = radius + margin
            self.angle = 180 - self.angle
        if not (self.y < height - radius - margin):
            self.y = height - radius - margin
            self.angle = 360 - self.angle
        if not(radius + margin < self.y):
            self.y = radius + margin
            self.angle = 360 - self.angle


# Checks Collision
def collision(ball1, ball2):
    dist = ((ball1.x - ball2.x)**2 + (ball1.y - ball2.y)**2)**0.5
    if dist <= radius*2:
        return True
    else:
        return False

# Checks if Cue Ball hits any Ball
def checkCueCollision(cueBall):
    for i in range(len(balls)):
        if collision(cueBall, balls[i]):
            if balls[i].x == cueBall.x:
                angleIncline = 2*90
            else:
                u1 = balls[i].speed
                u2 = cueBall.speed

                balls[i].speed = ((u1*cos(radians(balls[i].angle)))**2 + (u2*sin(radians(cueBall.angle)))**2)**0.5
                cueBall.speed = ((u2*cos(radians(cueBall.angle)))**2 + (u1*sin(radians(balls[i].angle)))**2)**0.5

                tangent = degrees((atan((balls[i].y - cueBall.y)/(balls[i].x - cueBall.x)))) + 90
                angle = tangent + 90

                balls[i].angle = (2*tangent - balls[i].angle)
                cueBall.angle = (2*tangent - cueBall.angle)

                balls[i].x += (balls[i].speed)*sin(radians(angle))
                balls[i].y -= (balls[i].speed)*cos(radians(angle))
                cueBall.x -= (cueBall.speed)*sin(radians(angle))
                cueBall.y += (cueBall.speed)*cos(radians(angle))


# Checks Collision Between Balls
def checkCollision():
    for i in range(len(balls)):
        for j in range(len(balls) - 1, i, -1):
            if collision(balls[i], balls[j]):
                if balls[i].x == balls[j].x:
                    angleIncline = 2*90
                else:
                    u1 = balls[i].speed
                    u2 = balls[j].speed

                    balls[i].speed = ((u1*cos(radians(balls[i].angle)))**2 + (u2*sin(radians(balls[j].angle)))**2)**0.5
                    balls[j].speed = ((u2*cos(radians(balls[j].angle)))**2 + (u1*sin(radians(balls[i].angle)))**2)**0.5

                    tangent = degrees((atan((balls[i].y - balls[j].y)/(balls[i].x - balls[j].x)))) + 90
                    angle = tangent + 90

                    balls[i].angle = (2*tangent - balls[i].angle)
                    balls[j].angle = (2*tangent - balls[j].angle)

                    balls[i].x += (balls[i].speed)*sin(radians(angle))
                    balls[i].y -= (balls[i].speed)*cos(radians(angle))
                    balls[j].x -= (balls[j].speed)*sin(radians(angle))
                    balls[j].y += (balls[j].speed)*cos(radians(angle))

def border():
    pygame.draw.rect(display, gray, (0, 0, width, 30))
    pygame.draw.rect(display, gray, (0, 0, 30, height))
    pygame.draw.rect(display, gray, (width - 30, 0, width, height))
    pygame.draw.rect(display, gray, (0, height - 30, width, height))

# def score():
#     font = pygame.font.SysFont("Agency FB", 30)

#     pygame.draw.rect(display, (51, 51, 51), (0, height, width, outerHeight))
#     for i in range(len(balls)):
#         balls[i].draw((i + 1)*2*(radius + 1), height + radius + 10)

#     text = font.render("Remaining Balls: " + str(len(balls)), True, stickColor)
#     display.blit(text, (width/2 + 50, height + radius/2))


def reset():
    global balls, noBalls
    noBalls = 3
    balls = []

    s = 70

    b1 = Ball(s, height/2 - 4*radius, 0, colors[0], 0, 1)
    b2 = Ball(s + 100, height/2 - 3*radius, 0, colors[1], 0, 2)
    b3 = Ball(s + 200, height/2 - 2*radius, 0, colors[2], 0, 3)


    balls.append(b1)
    balls.append(b2)
    balls.append(b3)




def gameOver():
    font = pygame.font.SysFont("Agency FB", 75)
    if len(balls) == 0:
        text = font.render("You Won!", True, (133, 193, 233))
    else:
        text = font.render("You Lost! Black in Hole!", True, (241, 148, 138))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()

                if event.key == pygame.K_r:
                    poolTable()
        display.blit(text, (50, height/2))

        pygame.display.update()
        clock.tick()

def close():
    pygame.quit()
    sys.exit()

# Main Function
def poolTable():
    loop = True
    reset()


    start = 0
    end = 0

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()

                if event.key == pygame.K_r:
                    poolTable()



        display.fill(background)

        border()
        for i in range(len(balls)):
            balls[i].draw(balls[i].x, balls[i].y)
        pygame.display.update()
        clock.tick(60)

poolTable()
