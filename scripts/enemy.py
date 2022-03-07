from pygame.locals import *
from random import *
from pygame import sprite
import pygame
import sys
import os 

class SmallEnemy(sprite.Sprite):
    def __init__(self,bg_size ) :
        pygame.sprite.Sprite.__init__(self)
        self.basepath = os.path.abspath(__file__).rsplit('\\',2)[0]
        self.enemy1_image = self.basepath + r"\images\enemy1.png" #低级敌机图片
        self.enemy1 = pygame.image.load(self.enemy1_image).convert_alpha() #载入低级敌机图片
        self.width,self.height = bg_size[0],bg_size[1] #获取生成低级敌机的活动范围
        self.rect = self.enemy1.get_rect() #获得低级敌机的尺寸
        self.rect.left,self.rect.top = [randint(0,self.width - self.rect.width),randint(-5 * self.height,0)] #在窗口的5倍之上的距离产生飞机

        self.speed  = 3 #设置小敌机的移动速度


    def move(self): #小敌机移动函数
        if self.rect.top < self.height : #如果小飞机的底超出窗口的下边框
            self.rect.top += self.speed #小飞机向下移动的速度
        else: #如果小飞机已经超出窗口的下边界框
            self.reset() #重置小飞机
    
    def reset(self): #重置小飞机函数
        self.rect.left,self.rect.top = [randint(0,self.width - self.rect.width),randint(-5 * self.height,0)] #在窗口的5倍之上的距离产生飞机


class MiddleEnemy(sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.basepath = os.path.abspath(__file__).rsplit('\\',2)[0]
        self.enemy2_image = self.basepath + r"\images\enemy2.png" #中级敌机图片
        self.enemy2 = pygame.image.load(self.enemy2_image).convert_alpha() #载入中级敌机图片
        self.width,self.height = bg_size[0],bg_size[1] #获取生成中级敌机的活动范围
        self.rect = self.enemy2.get_rect() #获得中级敌机的尺寸
        self.rect.left,self.rect.top = [randint(0,self.width - self.rect.width),randint(-5 * self.height,0)] #在窗口的5倍之上的距离产生飞机

        self.speed  = 3 #设置中敌机的移动速度


    def move(self): #中敌机移动函数
        if self.rect.top < self.height : #如果中飞机的底超出窗口的下边框
            self.rect.top += self.speed #中飞机向下移动的速度
        else: #如果中飞机已经超出窗口的下边界框
            self.reset() #重置中飞机
    
    def reset(self): #重置中飞机函数
        self.rect.left,self.rect.top = [randint(0,self.width - self.rect.width),randint(-5 * self.height,0)] #在窗口的5倍之上的距离产生飞机

class BigEnemy(sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.basepath = os.path.abspath(__file__).rsplit('\\',2)[0]
        self.enemy3_n1_image = self.basepath + r"\images\enemy3_n1.png" #高级敌机图片
        self.enemy3_n1 = pygame.image.load(self.enemy3_n1_image).convert_alpha() #载入高级敌机图片
        self.enemy3_n2_image = self.basepath + r"\images\enemy3_n2.png" #高级敌机图片
        self.enemy3_n2 = pygame.image.load(self.enemy3_n2_image).convert_alpha() #载入高级敌机图片
        self.width,self.height = bg_size[0],bg_size[1] #获取生成高级敌机的活动范围
        self.rect = self.enemy3_n1.get_rect() #获得高级敌机的尺寸
        self.rect.left,self.rect.top = [randint(0,self.width - self.rect.width),randint(-5 * self.height,0)] #在窗口的5倍之上的距离产生飞机

        self.speed  = 3 #设置大敌机的移动速度


    def move(self): #大敌机移动函数
        if self.rect.top < self.height : #如果大飞机的底超出窗口的下边框
            self.rect.top += self.speed #大飞机向下移动的速度
        else: #如果大飞机已经超出窗口的下边界框
            self.reset() #重置大飞机
    
    def reset(self): #重置大飞机函数
        self.rect.left,self.rect.top = [randint(0,self.width - self.rect.width),randint(-5 * self.height,0)] #在窗口的5倍之上的距离产生飞机
