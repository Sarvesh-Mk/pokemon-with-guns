from settings import *
import pygame
from guis import *
import random

class BattleSystem:

    def __init__(self, game):
        self.game = game

        #self.playerimg = self.game.player.walkUp[0]
        #for x in range(4): 
        #    self.playerimg = pygame.transform.scale2x(self.playerimg)
        self.playerimg = pygame.Surface((300, 300))
        self.playerimg.fill(YELLOW)
        
        self.mobimg = pygame.Surface((300, 300))
        self.mobimg.fill(RED)
        #self.mobimg = pygame.image.load('assets/GhostLeft1.png')
        #for x in range(4): 
        #    self.mobimg = pygame.transform.scale2x(self.mobimg)

        self.Battling = False
        self.width = 300
        self.height = 300

    def battle(self, mob):
        self.Battling = True
        while self.Battling:
            self.game.events()
            self.playerHealthBar = Bar(self.game.player.rect.x, self.game.player.rect.y, 16 * self.game.player.health * 2, 16, self.game.battles)
            self.mobHealthBar = Bar(mob.rect.x, mob.rect.y, TILESIZE * mob.health * 2, TILESIZE, self.game.battles)
            self.game.update()
            for sprite in self.game.battles:
                sprite.update()
            self.game.draw()
            #self.check(mob)
    
    def hit(self, mob):
        self.keyboard.text = ''
        self.keyboard.screenText = ''
        self.text = 0
        mob.health -= 1
        if mob.health == 0:
            self.Battling = False
            mob.kill()
    
    def miss(self):
        pass