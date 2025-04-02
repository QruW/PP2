import pygame

# Initialize pygame
def main():
    pygame.init()
    # Set up the display
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    # Set up the drawing parameters
    radius = 15
    mode = 'blue'
    drawing = False
    shape_mode = None  # "circle", "rectangle", "eraser", "square", "right_triangle", "equilateral_triangle", "rhombus"
    start_pos = None
    color = (0, 0, 255)
    
    while True:
        pressed = pygame.key.get_pressed() # Get the state of all keys
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
                if event.key == pygame.K_ESCAPE: # Exit the program \/
                    return
                if event.key == pygame.K_r: # Change color to red
                    mode = 'red'
                    color = (255, 0, 0)
                elif event.key == pygame.K_g: # Change color to green
                    mode = 'green'
                    color = (0, 255, 0)
                elif event.key == pygame.K_b: # Change color to blue
                    mode = 'blue'
                    color = (0, 0, 255)
                elif event.key == pygame.K_c: # For drawing a circle
                    shape_mode = "circle"
                elif event.key == pygame.K_e: # For erasing
                    shape_mode = "eraser"
                elif event.key == pygame.K_t: # For drawing a rectangle
                    shape_mode = "rectangle"
                elif event.key == pygame.K_s: # For drawing a square
                    shape_mode = "square"
                elif event.key == pygame.K_y: # For drawing a right triangle
                    shape_mode = "right_triangle"
                elif event.key == pygame.K_q: # For drawing an equilateral triangle
                    shape_mode = "equilateral_triangle"
                elif event.key == pygame.K_m: # For drawing a rhombus
                    shape_mode = "rhombus"
            
            if event.type == pygame.MOUSEBUTTONDOWN: # Left click to start drawing
                if event.button == 1:  # Left click
                    start_pos = event.pos
                    drawing = True
                elif event.button == 3:  # Right click to change radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEBUTTONUP: # Stop drawing on mouse button release
                drawing = False
                start_pos = None
            
            if event.type == pygame.MOUSEMOTION and drawing and start_pos: # Draw while moving the mouse
                end_pos = event.pos
                if shape_mode == "circle": # Draw a circle
                    pygame.draw.circle(screen, color, end_pos, radius)
                elif shape_mode == "rectangle": # Draw a rectangle
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, color, rect, 2)
                elif shape_mode == "square": # Draw a square
                    side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], side, side), 2)
                elif shape_mode == "right_triangle": # Draw a right triangle
                    pygame.draw.polygon(screen, color, [start_pos, (end_pos[0], start_pos[1]), end_pos], 2)
                elif shape_mode == "equilateral_triangle": # Draw an equilateral triangle
                    height = (3 ** 0.5) / 2 * abs(end_pos[0] - start_pos[0])
                    pygame.draw.polygon(screen, color, [start_pos, (end_pos[0], start_pos[1]), (start_pos[0] + (end_pos[0] - start_pos[0]) // 2, start_pos[1] - height)], 2)
                elif shape_mode == "rhombus": # Draw a rhombus
                    width = abs(end_pos[0] - start_pos[0])
                    height = abs(end_pos[1] - start_pos[1])
                    pygame.draw.polygon(screen, color, [(start_pos[0], start_pos[1] - height // 2), (start_pos[0] + width // 2, start_pos[1]), (start_pos[0], start_pos[1] + height // 2), (start_pos[0] - width // 2, start_pos[1])], 2)
                elif shape_mode == "eraser": # Erase by drawing a circle with the background color
                    pygame.draw.circle(screen, (0, 0, 0), end_pos, radius)
                
        pygame.display.flip()
        clock.tick(60)

main()
