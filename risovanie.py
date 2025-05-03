def highliht_closest_point(mouse_pos):
    closest_point = None
    closest_distance = float('inf')
    for point in points:
        distance=((point[0] - mouse_pos[0]) ** 2 + (point[1] - mouse_pos[1]) ** 2)**0.5
        if distance <= point_radius**2 and distance <closest_distance:
            closest_point = point
            closest_distance = distance
    if closest_point is not None:
        pygame.draw.circle(screen,highlight_color,closest_point,point_radius)

def remove_point(mouse_pos):
    for point in points:
        if ((point[0] - mouse_pos[0])**2+(point[1]- mouse_pos[1])**2 <= point_radius**2):
            points.remove(point)
            break
from all_colors import*
import pygame
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Рисование линии")
BACKGROUND = (0,0,0)
screen.fill(BACKGROUND)
points = []
point_radius = 5
highlight_color = (255,0,0)
line_color = (255,255,255)
preview_color = (192,192,192)
show_preview = True
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                points.append(event.pos)
            elif event.button ==2:
                points = []
            elif event.button == 3:
                remove_point(event.pos)






    #Основная логика
    #Отрисовка объектов
    screen.fill(BACKGROUND)
    for i in range(len(points) - 1):
        start_pos = points[i]
        end_pos = points[i+1]
        pygame.draw.line(screen,line_color,start_pos,end_pos,3)
    if len(points)>1 and show_preview == True:
        last_point = points[i]
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.line(screen,preview_color,mouse_pos,last_point,1)
        pos = pygame.mouse.get_pos()
        highliht_closest_point(pos)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()