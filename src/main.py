from os import path
# import pygame as pg
from pygame import init as pginit
from pygame import Surface
from pygame import Rect
from pygame import display
from pygame import draw
from pygame import time
from pygame import event as pgevent
from pygame.constants import *
from pygame.math import Vector2
# import pygame_gui
from pygame_gui import UIManager
from pygame_gui.windows import UIFileDialog
from pygame_gui.elements import UILabel
from pygame_gui.elements import UIDropDownMenu
from pygame_gui.elements import UITextEntryLine
from pygame_gui.elements import UIButton
from pygame_gui import UI_FILE_DIALOG_PATH_PICKED
from pygame_gui import UI_BUTTON_PRESSED
from pygame_gui import UI_DROP_DOWN_MENU_CHANGED


vec = Vector2
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGRAY = (40, 40, 40)
LIGHTGRAY = (140, 140, 140)
GAME_WIDTH = 803
GAME_HEIGHT = 803

pginit()
screen = display.set_mode((GAME_WIDTH+300, GAME_HEIGHT))
game = Surface((GAME_WIDTH, GAME_HEIGHT))
clock = time.Clock()

class Background:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        draw.rect(screen,LIGHTGRAY,Rect((0, 0), (self.width, self.height)))
        draw.line(screen,WHITE,(GAME_WIDTH+1,0),(GAME_WIDTH+1,GAME_HEIGHT),5)


def open_file():
    path = UIFileDialog(Rect((GAME_WIDTH+15, 10), (275, 300)), manager, "Open file", "./maps/")
    return path


running = True
manager = UIManager((GAME_WIDTH+300, GAME_HEIGHT))
menu = Rect((GAME_WIDTH+15, 10), (275, 20))
menux = UIDropDownMenu(['A*', 'D*', 'Bug', 'Potential Fields'], 'Choose algorithm', menu, manager)

path_text = UITextEntryLine(Rect((GAME_WIDTH+15, 30), (235, 20)),manager)
button_open = UIButton(Rect((GAME_WIDTH+250, 30), (40, 29)), '...', manager)
button_go = UIButton(Rect((GAME_WIDTH+13, GAME_HEIGHT-40), (275, 29)), 'GO', manager)

UILabel(Rect((GAME_WIDTH+15, GAME_HEIGHT-70), (100, 25)), "Turns:", manager)
turns = UILabel(Rect((GAME_WIDTH+120, GAME_HEIGHT-70), (165, 25)), "0", manager)
UILabel(Rect((GAME_WIDTH+15, GAME_HEIGHT-100), (100, 25)), "Steps:", manager)
steps = UILabel(Rect((GAME_WIDTH+120, GAME_HEIGHT-100), (165, 25)), "0", manager)

bug_choose_drop = Rect((GAME_WIDTH + 145, 120), (145, 29))
water_flow_drop = Rect((GAME_WIDTH+145, 120), (145, 29))
choose_drop = Rect((GAME_WIDTH+145, 150), (145, 29))
dir_drop = Rect((GAME_WIDTH+145, 210), (145, 29))


algorithm = None

while running:
    time_delta = clock.tick(FPS)
    for event in pgevent.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == USEREVENT:
            if event.user_type == UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == menux:
                    if event.text == "D*":
                        algorithm = event.text
                        try:
                            water_flow_dropx.kill()
                            water_flow_label.kill()
                            choose_dropx.kill()
                            choose_label.kill()
                            field_size_text_entry.kill()
                            field_size_label.kill()
                            dir_dropx.kill()
                            dir_choose_label.kill()
                        except Exception:
                            pass
                        pass
                    if event.text == "A*":
                        algorithm = event.text
                        try:
                            water_flow_dropx.kill()
                            water_flow_label.kill()
                            choose_dropx.kill()
                            choose_label.kill()
                            field_size_text_entry.kill()
                            field_size_label.kill()
                            dir_dropx.kill()
                            dir_choose_label.kill()
                            bug_choose_label.kill()
                            bug_choose_dropx.kill()
                        except Exception:
                            pass
                    if event.text == "Bug":
                        algorithm = event.text
                        try:
                            water_flow_dropx.kill()
                            water_flow_label.kill()
                            choose_dropx.kill()
                            choose_label.kill()
                            field_size_text_entry.kill()
                            field_size_label.kill()
                            dir_dropx.kill()
                            dir_choose_label.kill()
                        except Exception:
                            pass
                        bug_choose_label = UILabel(Rect((GAME_WIDTH + 15, 122), (130, 25)), "Algorithm:", manager)
                        bug_choose_dropx = UIDropDownMenu(['Bug1', 'Bug2'], 'Bug1', bug_choose_drop, manager)
                    if event.text == "Potential Fields":
                        algorithm = event.text

                        water_flow_label = UILabel(Rect((GAME_WIDTH+15, 122), (130, 25)), "Water flow:", manager)
                        water_flow_dropx = UIDropDownMenu(['True', 'False'], 'True', water_flow_drop, manager)

                        choose_label = UILabel(Rect((GAME_WIDTH+15, 152), (130, 25)), "Type of fields:", manager)
                        choose_dropx = UIDropDownMenu(['Make squares', 'Make neighbours'], 'Make squares', choose_drop,
                                                      manager)

                        field_size_label = UILabel(Rect((GAME_WIDTH+15, 182), (130, 25)), "Field size:", manager)
                        field_size_text_entry = UITextEntryLine(Rect((GAME_WIDTH+145, 180), (145, 20)), manager)
                        field_size_text_entry.set_text("1")

                        dir_choose_label = UILabel(Rect((GAME_WIDTH+15, 212), (130, 25)), "Direction:", manager)
                        dir_dropx = UIDropDownMenu(['Straight', 'Diagonal'], 'Straight', dir_drop, manager)

            if event.user_type == UI_BUTTON_PRESSED:
                if event.ui_element == button_open:
                    path = open_file()
                if event.ui_element == button_go:
                    if algorithm:

                        if algorithm == "D*":
                            map_to_solve = path_text.get_text()
                            turns.set_text("0")
                            steps.set_text("0")
                            if map_to_solve:
                                pass
                            else:
                                pass

                        if algorithm == "A*":
                            pass
                        if algorithm == "Bug":
                            map_to_solve = path_text.get_text()
                            if bug_choose_dropx.selected_option == "Bug1":
                                turns.set_text("0")
                                steps.set_text("0")
                                if map_to_solve:
                                    pass
                                else:
                                    pass
                            if bug_choose_dropx.selected_option == "Bug2":
                                turns.set_text("0")
                                steps.set_text("0")
                                if map_to_solve:
                                    pass
                                else:
                                    pass

                        if algorithm == "Potential Fields":
                            if water_flow_dropx.selected_option == "True":
                                water_flow = True
                            else:
                                water_flow = False

                            if choose_dropx.selected_option == "Make squares":
                                alg_fields = 0
                            else:
                                alg_fields = 1

                            field_size = int(field_size_text_entry.get_text())
                            if dir_dropx.selected_option == "Straight":
                                dirs = 0
                            else:
                                dirs = 1
                            map_to_solve = path_text.get_text()
                            turns.set_text("0")
                            steps.set_text("0")
                            if map_to_solve:
                                pass


            if event.user_type == UI_FILE_DIALOG_PATH_PICKED:
                path_text.set_text(str(path.current_file_path))

        manager.process_events(event)

    manager.update(time_delta)
    display.set_caption("{:.2f}".format(clock.get_fps()))

    background = Background(GAME_WIDTH+300, GAME_HEIGHT)
    background.draw()
    game.fill(DARKGRAY)
    # manager.update(time)
    # screen.blit(game,(0,0))
    manager.draw_ui(screen)
    screen.blit(game, (0, 0))

    display.update()

