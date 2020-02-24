# Manifests visual components
import pygame
import time
import math


class Window:

    def __init__(self):

        # Initiate pygame and calculate window dimensions
        self.pyinst = pygame.init()
        self.running = True
        self.infoObject = pygame.display.Info()
        self.width = math.floor(self.infoObject.current_w * .8)
        self.height = math.floor(self.infoObject.current_h * .85)

        # Visual vars
        self.screen = ""
        self.black_hex = [0, 0, 0]
        self.white_hex = [255, 255, 255]
        self.grey_hex = [209, 203, 204]
        self.tile_color = self.black_hex
        self.selected_p1_color = "Red"
        self.selected_p2_color = "Grey"

        # Board tiles
        self.tile_size = math.floor(self.width / 18)
        self.tile_counter = 0
        self.row_counter = 0
        self.border_edges = self.tile_size * 10
        print(self.tile_size)

        self.listeners = []

    def open(self):
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.screen.fill(self.grey_hex)
        pygame.display.set_caption('Serfault')
        ico = pygame.image.load("img_attempt_cap1_GZW_icon.ico")
        pygame.display.set_icon(ico)


    @staticmethod
    def update_screen():
        pygame.display.update()

    def close(self):
        self.pyinst.quit()

    def draw_board(self):
        while self.row_counter < 10:
            while self.tile_counter < 10:
                coordinate_x = self.tile_size * self.tile_counter
                coordinate_y = self.tile_size * self.row_counter
                pygame.draw.rect(self.screen, self.tile_color, (coordinate_x, coordinate_y, self.tile_size,
                                                                self.tile_size))
                self.tile_counter = self.tile_counter + 1
                if self.tile_color == self.black_hex:
                    self.tile_color = self.white_hex
                else:
                    self.tile_color = self.black_hex

            self.row_counter = self.row_counter + 1
            self.tile_counter = 0
            if self.tile_color == self.black_hex:
                self.tile_color = self.white_hex
            else:
                self.tile_color = self.black_hex

    def draw_main_ui(self):
        font = pygame.font.SysFont('arial', 30)
        font_2 = pygame.font.SysFont('arial', 20)
        small_font = pygame.font.SysFont('arial', 13)
        title_text = font.render('Serfault', False, (0, 0, 0))
        self.screen.blit(title_text, (self.border_edges+self.border_edges*.35, 0))

        pygame.draw.line(self.screen, self.black_hex, (self.border_edges, 40), (self.infoObject.current_w, 40))

        menu_text = font_2.render('Main Menu', False, (0, 0, 0))
        self.screen.blit(menu_text, (self.border_edges + 15, 60))

        mode_text = small_font.render('Select Your Gamemode', False, (0, 0, 0))
        self.screen.blit(mode_text, (self.border_edges + 30, 100))

        com_text = small_font.render('V Computer', False, (0,0,0))
        self.screen.blit(com_text, (self.border_edges + 50, 120))

        p2_text = small_font.render('2 Players', False, (0, 0, 0))
        self.screen.blit(p2_text, (self.border_edges + 140, 120))

        s = pygame.Surface((50, 20), pygame.SRCALPHA)  # per-pixel alpha
        s.fill((255, 255, 255, 128))  # notice the alpha value in the color
        self.screen.blit(s, (self.border_edges + 140, 120))

        self.listeners.append({"com": com_text})
        self.listeners.append({"2p": p2_text})
        self.listeners.append({"outline": s})

        color_text = small_font.render('Select Your Color', False, (0, 0, 0))
        self.screen.blit(color_text, (self.border_edges + 30, 150))

        col_sel = pygame.Surface((32, 32))
        col_sel.fill(self.black_hex)
        self.screen.blit(col_sel, (self.border_edges + 56.5, 166.5))

        red = pygame.Surface((25, 25))
        red.fill([224, 16, 16])
        self.screen.blit(red, (self.border_edges + 60, 170))

        grey = pygame.Surface((25, 25))
        grey.fill([138, 125, 125])
        self.screen.blit(grey, (self.border_edges + 120, 170))

        self.listeners.append({"red_col": red})
        self.listeners.append({"grey_col": grey})

        start_game = pygame.Surface((70, 20))
        start_game.fill(self.white_hex)
        start_text = small_font.render("Start Game!", False, self.black_hex)
        self.screen.blit(start_game, (self.border_edges + self.border_edges * .28, self.border_edges*.51))
        self.screen.blit(start_text, (self.border_edges + self.border_edges * .29, self.border_edges*.51))

        self.listeners.append({"start_button": start_game})


def Handler(window_obj):
    while window_obj.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_obj.running = False

def Test_Controller():
    tmpwindow = Window()
    tmpwindow.open()
    tmpwindow.draw_board()
    tmpwindow.draw_main_ui()
    tmpwindow.update_screen()
    Handler(tmpwindow)


Test_Controller()
