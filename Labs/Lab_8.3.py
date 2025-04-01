import pygame

# Initialize pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    drawing = False
    shape_mode = None  # "circle", "rectangle", "eraser"
    start_pos = None
    color = (0, 0, 255)
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    mode = 'green'
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    mode = 'blue'
                    color = (0, 0, 255)
                elif event.key == pygame.K_c:
                    shape_mode = "circle"
                elif event.key == pygame.K_e:
                    shape_mode = "eraser"
                elif event.key == pygame.K_t:
                    shape_mode = "rectangle"
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    start_pos = event.pos
                    drawing = True
                elif event.button == 3:  # Right click to change radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                start_pos = None
            
            if event.type == pygame.MOUSEMOTION and drawing and start_pos:
                end_pos = event.pos
                if shape_mode == "circle":
                    pygame.draw.circle(screen, color, end_pos, radius)
                elif shape_mode == "rectangle":
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, color, rect, 2)
                elif shape_mode == "eraser":
                    pygame.draw.circle(screen, (0, 0, 0), end_pos, radius)
                
        pygame.display.flip()
        clock.tick(60)

main()
