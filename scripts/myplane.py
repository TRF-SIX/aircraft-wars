"""我的飞机类"""
import pygame
import os
class MyPlane(pygame.sprite.Sprite): #定义我的飞机类，继承动画精灵类（因为之后要进行碰撞检测）
    def __init__(self, bg_size) -> None:
        self.basepath = os.path.abspath(__file__).rsplit('\\',2)[0]
        self.me1_image = self.basepath + r"\images\me1.png" #自身飞机第一张图片
        self.me2_image = self.basepath + r"\images\me2.png" #自身飞机第二张图片
        self.image1 = pygame.image.load(self.me1_image).convert_alpha() #第一张飞机图片
        self.image2 = pygame.image.load(self.me2_image).convert_alpha() #第二章飞机图片，为了做出飞机喷气的效果
        self.rect = self.image1.get_rect() #获得飞机图片的尺寸
        self.width ,self.height = bg_size[0],bg_size[1] #设置飞机允许活动地点
        self.rect.left,self.rect.top = [(self.width-self.rect.width) // 2 , (self.height - self.rect.height -60)] #设置我方飞机出现的位置

        self.speed = 10 #设置飞机出现的速度
    
    def moveup(self): #飞机向上飞的函数
        if self.rect.top > 0: #如果我方飞机没有飞出 上边界
            self.rect.top -= 10 #那么我方飞机向上飞10个元素
        else: #飞出 上边界
            self.rect.top = 0 #锁定在0位置，不再发生变化

    def movedown(self): #飞机向下飞的函数
        if self.rect.bottom < (self.height -60): #如果我方飞机没有飞出 下方边界
            self.rect.bottom += 10 #那么我方飞机向下飞10个元素
        else: #飞出 下边界
            self.rect.bottom = (self.height -60) #锁定在下边界上方60位置，不再发生变化

    def moveleft(self): #飞机向左飞的函数
        if self.rect.left >0: #如果我方飞机没有飞出左边界
            self.rect.left -= 10 #那么我方飞机向左飞10个元素
        else: #飞出 左边界
            self.rect.left = 0 #锁定在左边界的位置，不再发生变化

    def moveright(self): #飞机向右飞的函数
        if self.rect.right < self.width: #如果我方飞机没有飞出 右边界
            self.rect.right += 10 #那么我方飞机向右飞10个元素
        else: #飞出 右边界
            self.rect.right = self.width #锁定在右边界位置，不再发生 变化
