import pygame
from settings import *
from guis import *

class saveMenu:

    def __init__(self, game):
        self.game = game
        self.loadSaveData = False
        self.savemenu = False
        self.menu = False
        self.text = ''
        self.filename = 'save.txt'
        self.savex = 0
        self.savey = 0
        self.save_data = []
        self.levelNumber = 1
    
    def show_save_screen(self):
        self.yesButton =  Button(WIDTH/2, HEIGHT/2, KEYBOARDWIDTH, KEYBOARDHEIGHT, 'Save', LIGHTGREY, self.game, FONT_SIZE, self.game.gui)
        self.noButton =  Button(self.yesButton.x, self.yesButton.y + self.yesButton.height + TILESIZE, KEYBOARDWIDTH, KEYBOARDHEIGHT, "do not save", LIGHTGREY, self.game, FONT_SIZE, self.game.gui)
        self.menu = True
        while self.menu:
            self.game.update()
            self.game.draw()
            self.game.events()
            if self.game.mouse.CollideButton(self.yesButton):
                self.save()
            if self.game.mouse.CollideButton(self.noButton):
                self.game.quit()

    def save(self):
        self.f = open("{}".format(self.filename), "w+")
        self.f.write("{}\r\n".format(self.game.player.rect.x//TILESIZE))
        self.f.write("{}\r\n".format(self.game.player.rect.y//TILESIZE))
        self.f.write("{}\r\n".format(self.game.player.weapon))
        self.f.write("{}\r\n".format(self.game.levelNumber))
        self.savemenu = False 
        self.game.quit()

    def LoadSaveMenu(self):
        self.Savebutton =  Button(WIDTH/2, HEIGHT/2, KEYBOARDWIDTH, KEYBOARDHEIGHT, 'Open Save', LIGHTGREY, self.game, FONT_SIZE, self.game.gui)
        self.NewSavebutton =  Button(self.Savebutton.x, self.Savebutton.y + self.Savebutton.height + TILESIZE, KEYBOARDWIDTH, KEYBOARDHEIGHT, 'new save', LIGHTGREY, self.game, FONT_SIZE, self.game.gui)
        #self.keyboard  = Keyboard(self.Savebutton.x, self.NewSavebutton.y + KEYBOARDHEIGHT + TILESIZE, KEYBOARDWIDTH, KEYBOARDHEIGHT, self.game, self.game.gui, 'Enter filename here', 32)
        self.menu = True
        while self.menu:
            self.game.update()
            self.game.draw()
            self.game.events()
            if self.game.mouse.CollideButton(self.Savebutton):
                self.Savebutton.kill()
                self.NewSavebutton.kill()
                self.loadSaveData = True
                self.menu = False
            if self.game.mouse.CollideButton(self.NewSavebutton):
                self.Savebutton.kill()
                self.NewSavebutton.kill()
                self.menu = False
                self.loadSaveData = False
    
    def load_save(self):
        self.LoadSaveMenu()
        self.save_data = []
        if self.loadSaveData == True:
            with open(self.filename, "rt") as f:
                for line in f:
                    self.save_data.append(line.strip())
            
            self.savex = self.save_data[0]
            self.savey = self.save_data[1]
            self.savex = int(self.savex)
            self.savey = int(self.savey)
            self.levelNumber = self.save_data[3]