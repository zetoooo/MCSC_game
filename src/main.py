import pygame, sys, os
from pygame.locals import *
from enum import Enum
import classes
from classes import animation_loop
import json

# set up pygame
pygame.init()


class Game:
    
    def __init__(self, argdict):
        #argdic is everything all the options set from the menu
        self.set_fps = argdict["set_fps"]
        self.is_online = argdict["is_online"]
        self.screen_size = argdict["screen_size"]
        self.setup_screen()
        self.setup_font()
        self.load_images()
        #self.setup_player()
        #self.setup_npcs()
    
    
    def setup_screen(self):
        self.window = pygame.display.set_mode(self.screen_size, 0, 32)
        self.clock = pygame.clock.Clock()
        
        
    def setup_font(self):
        #access font with self.fonts["Comic Sans-15"].render...
        self.fonts = []
        _fonts = [ ("Comic Sans", os.path.join('..','data', 'comic.ttf'), 15) ]
        for name, path, size in _fonts:
          key = "%s-%s" % (name, size)
          self.fonts[key] = pygame.font.Font(path, size)
    
    def load_images(self):
        #load the images that needs to be loaded for the specific level.
        #each level has a specific json file that gives the images to load
        #the json file should look like: [ ["hp_container", "../data/gui/bar_container.png"], ..]
        _images = json.loads(self.imagepath)
        for key, path in _images:
          self.images[key] = pygame.image.load(path)
   
   def run(self):
       self.bool_window = true
       self.bool_game = true
       self.bool_pause = false
       while self.bool_window:
           
         while self.bool_game:
           self.game_event()
           self.game_logic()
           self.game_draw()
           pygame.display.update()
           self.clock.tick(self.set_fps) #makes the game run at 60 fps
           
         while self.bool_pause:
           self.pause_event()
           self.pause_draw()
           pygame.display.update()
           self.clock.tick(self.set_fps) #makes the game run at 60 fps
    
   def pause_game(self):
       self.bool_game = false
       self.bool_pause = true
   
   def unpause_game(self):
       self.bool_game = true
       self.bool_pause = false
   
   def exit_game(self):
       self.bool_game = false
       self.bool_pause = false
       self.bool_window = false
       

game = Game(argdict)
game.run()

#not useful.
'''# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
'''
#rendered on the way   
'''
HP = myfont.render("HP", 1, WHITE)
MP = myfont.render("MP", 1, WHITE)
LH = myfont.render("LH", 1, WHITE)
RH = myfont.render("RH", 1, WHITE)
S1 = myfont.render("1", 1, WHITE)
S2 = myfont.render("2", 1, WHITE)
S3 = myfont.render("3", 1, WHITE)
S4 = myfont.render("4", 1, WHITE)
'''
#loaded from the menu, before the stage begins. therefore everything is in argdict
'''
health_value = 0.5 * 450
mana_value = 0.7 * 450
'''
# what is this... this doesnt make any sense because screen is filled in black in the loop.
#do this in a loop
'''
screen.fill(BLACK)
screen.blit(hp_bar, (20,830), (10,10,health_value,50) )
screen.blit(mana_bar, (970,830), (10,10,mana_value,50) )
screen.blit(hp_container, (20,830) )
screen.blit(hp_container, (970,830) )
screen.blit(enemy_bar_container, (470,20) )
screen.blit(enemy_bar, (470,20) )
screen.blit(square, (510,830) )
screen.blit(square, (580,830) )
screen.blit(square, (670,830) )
screen.blit(square, (740,830) )
screen.blit(square, (810,830) )
screen.blit(square, (880,830) )
screen.blit(HP, (20, 810))
screen.blit(MP, (970, 810))
screen.blit(LH, (510, 810))
screen.blit(RH, (580, 810))
screen.blit(S1, (670, 810))
screen.blit(S2, (740, 810))
screen.blit(S3, (810, 810))
screen.blit(S4, (880, 810))
screen.blit(boss, (700, 300))
'''

'''
# run the game loop
while True:
    screen.fill(BLACK)
    if paused:
        pass
        # don't move anything
    else:
        for thing in things_on_screen:
            thing.tick()

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                # Depending of what is going on, we will do different things.
                if state == State.playing:
                    # If not online, stop game.
                    if not is_online:
                        paused = True

                    classes.PauseMenu.show()

                    # put pause menu to focus.
                    focus = classes.PauseMenu

                    state = State.paused
                elif state == State.menu or state == State.paused:
                    # send the escape event to menu. It will 'go back' if it can. If not, then it will remove the pause menu.
                    if focus.escape_pressed() == "close_menu":
                        pass

        focus.key_event(event)
    pygame.display.update()'''
