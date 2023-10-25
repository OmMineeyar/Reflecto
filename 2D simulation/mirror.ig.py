import pygame
import sys
import math
import numpy as np
def reflected(incident_vector,normal):
        
        incident_vector = norm(incident_vector)
        normal=norm(normal)
        reflection_vector = incident_vector - 2 * np.dot(incident_vector, normal) * normal
        return reflection_vector
    
def magnitude(vector):
   return np.sqrt(np.dot(np.array(vector),np.array(vector)))

def norm(vector):
   return np.array(vector)/magnitude(np.array(vector))

class Laser:
    def __init__(self,coordinates,initial_direction):
        self.source=pygame.math.Vector2(coordinates)
        self.direction=pygame.Vector2(initial_direction)#.normalize()
    def draw(self,screen):
        pygame.draw.line(screen,'Blue',self.source,self.source + 100*self.direction)
        
class Mirror:

    def __init__(self,mid_point, normal_vec):
        self.pos = pygame.math.Vector2(mid_point)
        self.normal=pygame.Vector2(normal_vec)
        if normal_vec[1]==0:
            self.mirror_vector= pygame.Vector2(0,1)
        else:
            self.mirror_vector= pygame.Vector2(1/math.sqrt(1**2+((-1*normal_vec[0])/(normal_vec[1]))**2),(-1*normal_vec[0])/(normal_vec[1])/math.sqrt(1**2+((-1*normal_vec[0])/(normal_vec[1]))**2))
        self.endpoints=[self.pos + 10 * self.mirror_vector,self.pos- 10 * self.mirror_vector]
    def draw(self,screen):
        pygame.draw.line(screen,'Red',self.pos,self.pos + 10 * self.mirror_vector)
        pygame.draw.line(screen,'Red',self.pos,self.pos - 10 * self.mirror_vector)
    
pygame.init()

screen = pygame.display.set_mode((700, 300))
pygame.display.set_caption("Mirror and Light Source")
M=[Mirror((150,150),(1,-1)), Mirror((150,250),(1,-1)),Mirror((700,300),(-1,0)),Mirror((700,200),(3,4))]
L=Laser((0,200),(100,100))
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #L.draw(screen)
    M[0].draw(screen)
    M[1].draw(screen)
    M[2].draw(screen)
    M[3].draw(screen)
    for j in range(0,5):
        k=0
        for i in range(0,4):
            rayOrigin = np.array(L.source)
            rayDirection = np.array(norm(L.direction))
            point1 = np.array(M[i].endpoints[0])
            point2 = np.array(M[i].endpoints[1])
            v1 = rayOrigin - point1
            v2 = point2 - point1
            if np.dot(rayDirection,M[i].normal)>0:
                continue
            v3 = np.array([-rayDirection[1], rayDirection[0]])
            v2dv3=np.dot(v2, v3)
            if v2dv3==0:
                print("Hi" , i,j)
                continue
            t1 = np.cross(v2, v1) / np.dot(v2, v3)
            t2 = np.dot(v1, v3) / np.dot(v2, v3)
            if t1 > 0.0 and t2 >= 0.0 and t2 <= 1.0:
                k=k+1
                pygame.draw.line(screen,'Blue',rayOrigin,rayOrigin + t1 * rayDirection)
                L.direction=reflected(rayDirection,M[i].normal)
                L.source=rayOrigin + t1 * rayDirection
                print(L.direction)
                print(L.source)
                continue
        if k==0:
            pygame.draw.line(screen,'Blue',rayOrigin,rayOrigin + 1000 * rayDirection)
            continue
        
    pygame.display.update()
    pygame.time.Clock().tick(60)
pygame.quit()
sys.exit()
