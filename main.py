"""
Author:trf
Email:TRF_873@163.com
Time:2022/3/6
"""
import traceback
from pygame import *
import tkinter as tk
import pygame
import math
import sys

"""我的飞机类"""

class MyPlane(pygame.sprite.Sprite): #定义我的飞机类，继承动画精灵类（因为之后要进行碰撞检测）
    def __init__(self, bg_size) -> None:
        self.me1_image = r"D:\python_projects\aircraft-wars\images\me1.png" #自身飞机第一张图片
        self.me2_image = r"D:\python_projects\aircraft-wars\images\me2.png" #自身飞机第二张图片
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


def main():
    delay = 100
    pygame.init() # 初始化
    pygame.mixer.init() #混音器初始化

    clock = pygame.time.Clock() #设置一个计时器


    """载入音乐文件"""
    #背景音乐
    pygame.mixer.music.load(r"D:\python_projects\aircraft-wars\sound\game_music.ogg") #设置背景音乐
    pygame.mixer.music.set_volume(1) #设置音量

    #游戏音效
    bullet_music = r"D:\python_projects\aircraft-wars\sound\bullet.wav" #子弹音效
    button_music = r"D:\python_projects\aircraft-wars\sound\bytton.wav" #按键音效
    enemy1_down_music = r"D:\python_projects\aircraft-wars\sound\enemy1_down.wav" #低等级敌机击毁音效
    enemy2_down_music = r"D:\python_projects\aircraft-wars\sound\enemy2_down.wav" #中等级敌机击毁音效
    enemy3_down_nusic = r"D:\python_projects\aircraft-wars\sound\enemy3_down.wav" #高等级敌机击毁音效
    get_bomb_music = r"D:\python_projects\aircraft-wars\sound\get_bomb.wav" #获得全屏炸弹音效
    get_bullet_music = r"D:\python_projects\aircraft-wars\sound\get_bullet.wav" #获得双倍子弹补给音效
    me_down_music = r"D:\python_projects\aircraft-wars\sound\me_down.wav" #自身飞机杯击毁音效
    supply_music = r"D:\python_projects\aircraft-wars\sound\supply.wav" #补给产生音效
    upgrade_music = r"D:\python_projects\aircraft-wars\sound\upgrade.wav" #升级音效
    use_bomb_music = r"D:\python_projects\aircraft-wars\sound\use_bomb.wav" #使用全屏炸弹音效

    """图片文件路径"""
    again_image = r"D:\python_projects\aircraft-wars\images\again.png" #重新开始图片路径
    Background_image = r"D:\python_projects\aircraft-wars\images\background.png" #背景图路径
    bomb_supply_image = r"D:\python_projects\aircraft-wars\images\bomb_supply.png" #全屏炸弹补给图
    bomb_image = r"D:\python_projects\aircraft-wars\images\bomb.png" # 全屏炸弹图
    bullet_supply_image = r"D:\python_projects\aircraft-wars\images\bullet_supply.png" #补给子弹图
    bullet1_image = r"D:\python_projects\aircraft-wars\images\bullet1.png" #第一种子弹图
    bullet2_image = r"D:\python_projects\aircraft-wars\images\bullet2.png" #第二种子弹图
    enemy1_down1_image = r"D:\python_projects\aircraft-wars\images\enemy1_down1.png"    #低级敌机撞到爆炸第一张图片
    enemy1_down2_image = r"D:\python_projects\aircraft-wars\images\enemy1_down2.png"    #低级敌机撞到爆炸第二张图片
    enemy1_down3_image = r"D:\python_projects\aircraft-wars\images\enemy1_down3.png"    #低级敌机撞到爆炸第三张图片
    enemy1_down4_image = r"D:\python_projects\aircraft-wars\images\enemy1_down4.png"    #低级敌机撞到爆炸第四张图片
    enemy1_image = r"D:\python_projects\aircraft-wars\images\enemy1.png"  #低级敌机图片
    enemy2_down1_image = r"D:\python_projects\aircraft-wars\images\enemy2_down1.png"    #中级敌机撞到爆炸第一张图片
    enemy2_down2_image = r"D:\python_projects\aircraft-wars\images\enemy2_down2.png"    #中级敌机撞到爆炸第二张图片
    enemy2_down3_image = r"D:\python_projects\aircraft-wars\images\enemy2_down3.png"    #中级敌机撞到爆炸第三张图片
    enemy2_down4_image = r"D:\python_projects\aircraft-wars\images\enemy2_down4.png"    #中级敌机撞到爆炸第四张图片
    enemy2_hit_image = r"D:\python_projects\aircraft-wars\images\enemy2_hit.png"   #中级敌机碰撞图片
    enemy2_image = r"D:\python_projects\aircraft-wars\images\enemy2.png"  #中级敌机图片
    enemy3_down1_image = r"D:\python_projects\aircraft-wars\images\enemy3_down1.png"    #高级敌机撞到爆炸第四张图片
    enemy3_down2_image = r"D:\python_projects\aircraft-wars\images\enemy3_down2.png"    #高级敌机撞到爆炸第四张图片
    enemy3_down3_image = r"D:\python_projects\aircraft-wars\images\enemy3_down3.png"    #高级敌机撞到爆炸第四张图片
    enemy3_down4_image = r"D:\python_projects\aircraft-wars\images\enemy3_down4.png"    #高级敌机撞到爆炸第四张图片
    enemy3_down5_image = r"D:\python_projects\aircraft-wars\images\enemy3_down5.png"    #高级敌机撞到爆炸第四张图片
    enemy3_down6_image = r"D:\python_projects\aircraft-wars\images\enemy3_down6.png"    #高级敌机撞到爆炸第四张图片
    enemy3_hit_image = r"D:\python_projects\aircraft-wars\images\enemy3_hit.png"  #高级敌机碰撞图片
    enemy3_n1_image = r"D:\python_projects\aircraft-wars\images\enemy3_n1.png"   #高级敌机图片1
    enemy3_n2_image = r"D:\python_projects\aircraft-wars\images\enemy3_n2.png"   #高级敌机图片2
    gameover_image = r"D:\python_projects\aircraft-wars\images\gameover.png"    #游戏结束图片
    life_image = r"D:\python_projects\aircraft-wars\images\life.png"    #表示生命值的图片
    me_destory_1_image = r"D:\python_projects\aircraft-wars\images\me_destroy_1.png"    #自身飞机炸毁第一张图片
    me_destory_2_image = r"D:\python_projects\aircraft-wars\images\me_destroy_2.png"    #自身飞机炸毁第二张图片
    me_destory_3_image = r"D:\python_projects\aircraft-wars\images\me_destroy_3.png"    #自身飞机炸毁第三张图片
    me_destory_4_image = r"D:\python_projects\aircraft-wars\images\me_destroy_4.png"    #自身飞机炸毁第四张图片
    me1_image = r"D:\python_projects\aircraft-wars\images\me1.png" #自身飞机第一张图片
    me2_image = r"D:\python_projects\aircraft-wars\images\me2.png" #自身飞机第二张图片
    pause_nor_image = r"D:\python_projects\aircraft-wars\images\pause_nor.png"   #暂停的时候图片
    pause_pressed_image = r"D:\python_projects\aircraft-wars\images\pause_pressed.png"   #暂停到继续的中间变换图
    resume_nor_image = r"D:\python_projects\aircraft-wars\images\resume_nor.png"  #继续的时候的图片
    resume_pressed_image =r"D:\python_projects\aircraft-wars\images\resume_pressed.png"   #继续到暂停的中间变换图

    """设置背景"""
    bg_size = width,height = 430,700 #背景大小
    screen = pygame.display.set_mode(bg_size) #这是背景大小
    background = pygame.image.load(Background_image).convert_alpha() #画背景
    pygame.mixer.music.play(-1) #播放背景音乐，-1表示无限循环

    #生成飞机
    myself = MyPlane(bg_size)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.blit(background,(0,0)) #绘制背景

        #绘制飞机
        if pygame.transform: #如果改变属性为真 画第一张飞机图
            if delay == 0:
                delay = 100
            delay -= 1
            pygame.transform  =False #改变属性来达到改变图片的效果
        else: #如果改变属性为假 画第二张飞机图
            if delay == 0:
                delay = 100
            delay -= 1
            pygame.transform = True
        
        if delay % 5:
            screen.blit(myself.image2,myself.rect) #绘制第二张飞机图
        elif not delay % 5 :
            screen.blit(myself.image1,myself.rect) #绘制第一张飞机图

        #检查是否有上下左右或wasd按下，如果有则对飞机进行相应控制
        key_press = pygame.key.get_pressed()
        if key_press[K_w] or key_press[K_UP]: #上
            myself.moveup()
        elif key_press[K_s] or key_press[K_DOWN]: #下
            myself.movedown()
        elif key_press[K_a] or key_press[K_DOWN]: #左
            myself.moveleft()
        elif key_press[K_d] or key_press[K_RIGHT]: #右
            myself.moveright()

        pygame.display.flip() #不停的刷新画面，不停的绘画

        clock.tick(60) #设置帧率

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
    