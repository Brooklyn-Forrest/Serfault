# Manifests visual components
import pygame
import time
import math


class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = ""
        self.pyinst = pygame.init()
        self.running = True
        self.tile_size = math.floor(width / 12)
        print(self.tile_size)
        self.black_hex = [0, 0, 0]
        self.white_hex = [255, 255, 255]
        self.tile_color = self.black_hex
        self.tile_counter = 0
        self.row_counter = 0

    def open(self):
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.screen.fill(self.white_hex)

    @staticmethod
    def update_screen():
        pygame.display.update()

    def close(self):
        self.pyinst.quit()

    def draw_board(self):
        while self.row_counter < 8:
            while self.tile_counter < 8:
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


def Handler(window_obj):
    while window_obj.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_obj.running = False

def Test_Controller():
    tmpwindow = Window(1000, 750)
    tmpwindow.open()
    tmpwindow.draw_board()
    tmpwindow.update_screen()
    Handler(tmpwindow)


Test_Controller()
