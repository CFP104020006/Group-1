import pygame
import sys
from math import *
import random
import numpy as np
import matplotlib.pyplot as plt
import time

pygame.init()
width = 480
height = 660
main_surface = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
#大分子圓球 橘色
orange = (255,165,0)
#小分子圓球 紅色
red = (255,0,0)
blue = (20, 100, 150)
balls = []
g=0.2
bar_height = 600
# Ball Class

class Ball:
    def __init__(self, x, y, vx, vy, color, hard, radius, mass):
        self.x = x
        self.y = y
        self.color = color
        self.vx = vx
        self.vy = vy
        self.hard = hard
        self.radius = radius
        self.mass = mass

    # Draws Balls on Display Window
    def draw(self, x, y):
        pygame.draw.circle(main_surface, self.color, [int(x), int(y)], self.radius)

    # Moves the Ball around the Screen
    def move(self):

        if self.hard == 1:
            self.vx = 0
            self.vy = 0
        self.x = self.x + self.vx
        self.y = self.y + self.vy

        if (self.x + self.radius >= width):
            self.x = width - self.radius
            self.vx = -self.vx
        if (self.radius >= self.x):
            self.x = self.radius
            self.vx = -self.vx
        if (self.y + self.radius >= height):
            self.y = height - self.radius
            self.hard = 1
#             self.angle = 360 - self.angle
            self.vy = -self.vy
        if (self.radius >= self.y):
            self.y = self.radius
            self.vy=-self.vy

def collision(ball1, ball2):
    r12 = [ball2.x-ball1.x, ball2.y-ball1.y]
    v1 = [ball1.vx, ball1.vy]
    v2 = [ball2.vx, ball2.vy]
    dist = ((ball1.x - ball2.x)**2 + (ball1.y - ball2.y)**2)**0.5
    if dist <= ball1.radius + ball2.radius:

        if  r12[0]*v2[0] + r12[1]*v2[1] > 0 and r12[0]*v1[0] + r12[1]*v1[1] < 0 :

            return False
        elif (r12[0]*v2[0] + r12[1]*v2[1])*(r12[0]*v1[0] + r12[1]*v1[1]) > 0 :
            if r12[0]*v2[0] + r12[1]*v2[1] > 0 and (r12[0]*v1[0] + r12[1]*v1[1])-(r12[0]*v2[0] + r12[1]*v2[1])<0:
                return False
            elif r12[0]*v2[0] + r12[1]*v2[1] < 0 and (r12[0]*v1[0] + r12[1]*v1[1])-(r12[0]*v2[0] + r12[1]*v2[1])>0:
                return False
        elif r12[0]*v1[0] + r12[1]*v1[1] < 0:
            return False
        else:
            return True

    else:
        return False

# Checks Collision Between Balls
def checkCollision():
    for i in range(len(balls)):
        for j in range(len(balls) - 1, i, -1):
            if collision(balls[i], balls[j]):
                vx1 = balls[i].vx
                vx2 = balls[j].vx
                vy1 = balls[i].vy
                vy2 = balls[j].vy
                v1 = (balls[i].vx**2+balls[i].vy**2)**0.5
                v2 = (balls[j].vx**2+balls[j].vy**2)**0.5
                if vx1 or vx2 or vy1 or vy2 == 0:
                    ang1 = pi/2
                    ang2 = pi/2

                else:
                    ang1 = acos(vx1/v1)
                    ang2 = acos(vx2/v2)
                m1 = balls[i].mass
                m2 = balls[j].mass

                if balls[i].x == balls[j].x:
                    phi = pi/2
                else:
                    phi = atan((balls[j].y-balls[i].y)/(balls[j].x-balls[i].x))
                phi2 = pi-phi
                vxr1 = v1*cos(ang1-phi)
                vyr1 = v1*sin(ang1-phi)
                vxr2 = v2*cos(ang2-phi)
                vyr2 = v2*sin(ang2-phi)
                vfxr1 = ((m1-m2)*vxr1+(2*m2)*vxr2)/(m1+m2)
                vfxr2 = ((2*m1)*vxr1+(m2-m1)*vxr2)/(m1+m2)
                vfyr1 = vyr1
                vfyr2 = vyr2
                vfx1 = cos(phi)*vfxr1 + cos(phi+pi/2)*vfyr1
                vfy1 = sin(phi)*vfxr1 + sin(phi+pi/2)*vfyr1
                vfx2 = cos(phi)*vfxr2 + cos(phi+pi/2)*vfyr2
                vfy2 = sin(phi)*vfxr2 + sin(phi+pi/2)*vfyr2
                balls[i].vx = vfx1
                balls[i].vy = vfy1
                balls[j].vx = vfx2
                balls[j].vy = vfy2


def reset():
    global beginning_time
    global times
    beginning_time = time.time()
    times = []

    global balls
    # (x, y, vx, vy, color, hard, radius, mass)
#     running balls
    for i in range(2):
        for j in range(10):
            b = Ball(10 + i*10, 31+j*10, 1*np.random.normal(0,10), 1*np.random.normal(0,1), orange, 0, 3, 5)
            balls.append(b)

#     static balls
    for i in range(8):
        for j in range(4):
            b = Ball(30+60*i, 200+90*j, 0, 0, blue, 1, 20, 100)
            balls.append(b)

    for i in range(7):
        for j in range(3):
            b = Ball(60+60*i, 245+90*j, 0, 0, blue, 1, 20, 100)
            balls.append(b)


def close():
    pygame.quit()
    plot_time_dist(times)
    sys.exit()

def main():
    reset()
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            close()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                close()

            if event.key == pygame.K_r:
                main()



        main_surface.fill((0,0,0))

        checkCollision()
        for b in balls:
            if b.y>bar_height:
                balls.remove(b)
                times.append(time.time() - beginning_time)



        for b in balls:
            b.vy=b.vy+g
            b.draw(b.x, b.y)
            b.move()



        pygame.display.update()
        clock.tick(60)


def plot_time_dist(times):
    print(times)
    times_bins = [_ / 2 for _ in range((floor(times[-1]) + 1) * 2 + 1)]
    plt.hist(times, bins=times_bins)
    plt.show()


main()
