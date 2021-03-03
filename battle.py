from settings import *
import pygame
from guis import *
import random

class BattleSystem:

    def __init__(self, game):
        self.game = game

        self.playerimg = self.game.player.walkUp[0]
        for x in range(4): 
            self.playerimg = pygame.transform.scale2x(self.playerimg)
        #self.playerimg = pygame.Surface((TILESIZE * 20, TILESIZE * 20))
        #self.playerimg.fill(YELLOW)

        #self.mobimg = pygame.Surface((TILESIZE * 20, TILESIZE * 20))
        #self.mobimg.fill(RED)
        self.mobimg = pygame.image.load('assets/GhostLeft1.png')
        for x in range(4): 
            self.mobimg = pygame.transform.scale2x(self.mobimg)
        
        self.playerHealthBar = pygame.Surface((TILESIZE * PLAYER_HEALTH, TILESIZE))
        self.playerHealthBar.fill(RED)
        self.mobHealthBar = pygame.Surface((TILESIZE, TILESIZE * 2))
        self.mobHealthBar.fill(RED)

        self.Battling = False
        self.width = 64
        self.height = 64

    def battle(self, mob):
        self.Battling = True
        while self.Battling:
            self.game.events()
            self.playerHealthBar = pygame.Surface((TILESIZE * self.game.player.health * 2, TILESIZE))
            self.playerHealthBar.fill(RED)
            self.mobHealthBar = pygame.Surface((TILESIZE * mob.health * 2, TILESIZE))
            self.mobHealthBar.fill(RED)
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