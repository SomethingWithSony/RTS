import pygame
import colors
import settings

class GameLoop:
    def __init__(self):
        pygame.init() # Initialize pygame

         # Setup window
        pygame.display.set_caption("RTS")
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.surface = pygame.Surface((settings.WIDTH, settings.HEIGHT), pygame.SRCALPHA) # Surface used for trasnparency

        self.clock = pygame.time.Clock()
        self.running = True

        # Setup map
        self.grid = self.create_grid()

    def create_grid(self):
        grid = []
        for row in range(int(settings.WIDTH / settings.CELL_SIZE)):
            grid.append([])
            for col in range(int(settings.HEIGHT / settings.CELL_SIZE)):
                grid[row].append( { 
                                    "rect" : pygame.Rect(row * settings.CELL_SIZE, col * settings.CELL_SIZE, settings.CELL_SIZE,settings.CELL_SIZE),
                                    "color" : (0,0,0),
                                    "pos" : [row * settings.CELL_SIZE, col * settings.CELL_SIZE] # top left pos
                                }  )  
                
        return grid

    
    def render_grid(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                color = self.grid[row][col]["color"]
                pygame.draw.rect(self.screen, color, self.grid[row][col]["rect"], 1)

    def run(self):
        while self.running:
            # Clear screen and surface
            self.screen.fill(colors.BACKGROUND)
            self.surface.fill((0, 0, 0, 0))  # Clear with transparent

            self.render_grid()

            """ Input Handling """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            
            self.screen.blit(self.surface, (0, 0))
            pygame.display.flip()

            self.clock.tick(settings.FRAMERATE)