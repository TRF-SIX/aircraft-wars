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
from myplane import MyPlane
from enemy import *
import os

def main():
    basepath = os.path.abspath(__file__).rsplit('\\',2)[0]
    pygame.init() # 初始化
    pygame.mixer.init() #混音器初始化

    clock = pygame.time.Clock() #设置一个计时器

    transform = False #设置一个是否改变的变量
    delay = 100 #延时变量
    switch_image = True #用于切换图片


    """载入音乐文件"""
    #背景音乐
    pygame.mixer.music.load(basepath + r"\sound\game_music.ogg") #设置背景音乐
    pygame.mixer.music.set_volume(1) #设置音量

    #游戏音效
    bullet_music = mixer.Sound( basepath + r"\sound\bullet.wav") #子弹音效
    button_music = mixer.Sound(basepath + r"\sound\button.wav") #按键音效
    enemy1_down_music = mixer.Sound(basepath + r"\sound\enemy1_down.wav") #低等级敌机击毁音效
    enemy2_down_music = mixer.Sound(basepath + r"\sound\enemy2_down.wav") #中等级敌机击毁音效
    enemy3_down_music = mixer.Sound(basepath + r"\sound\enemy3_down.wav") #高等级敌机击毁音效
    enemy3_fly_music = mixer.Sound(basepath + r"\sound\enemy3_flying.wav") #高等敌机出现音效
    get_bomb_music = mixer.Sound(basepath + r"\sound\get_bomb.wav") #获得全屏炸弹音效
    get_bullet_music = mixer.Sound(basepath + r"\sound\get_bullet.wav") #获得双倍子弹补给音效
    me_down_music = mixer.Sound(basepath + r"\sound\me_down.wav") #自身飞机杯击毁音效
    supply_music = mixer.Sound(basepath + r"\sound\supply.wav") #补给产生音效a
    upgrade_music = mixer.Sound(basepath + r"\sound\upgrade.wav") #升级音效
    use_bomb_music = mixer.Sound(basepath + r"\sound\use_bomb.wav") #使用全屏炸弹音效

    """图片文件路径"""
    again_image = basepath + r"\images\again.png" #重新开始图片路径
    Background_image = basepath + r"\images\background.png" #背景图路径
    bomb_supply_image = basepath + r"\images\bomb_supply.png" #全屏炸弹补给图
    bomb_image = basepath + r"\images\bomb.png" # 全屏炸弹图
    bullet_supply_image = basepath + r"\images\bullet_supply.png" #补给子弹图
    bullet1_image = basepath + r"\images\bullet1.png" #第一种子弹图
    bullet2_image = basepath + r"\images\bullet2.png" #第二种子弹图
    enemy1_down1_image = basepath + r"\images\enemy1_down1.png"    #低级敌机撞到爆炸第一张图片
    enemy1_down2_image = basepath + r"\images\enemy1_down2.png"    #低级敌机撞到爆炸第二张图片
    enemy1_down3_image = basepath + r"\images\enemy1_down3.png"    #低级敌机撞到爆炸第三张图片
    enemy1_down4_image = basepath + r"\images\enemy1_down4.png"    #低级敌机撞到爆炸第四张图片
    enemy1_image = basepath + r"\images\enemy1.png"  #低级敌机图片
    enemy2_down1_image = basepath + r"\images\enemy2_down1.png"    #中级敌机撞到爆炸第一张图片
    enemy2_down2_image = basepath + r"\images\enemy2_down2.png"    #中级敌机撞到爆炸第二张图片
    enemy2_down3_image = basepath + r"\images\enemy2_down3.png"    #中级敌机撞到爆炸第三张图片
    enemy2_down4_image = basepath + r"\images\enemy2_down4.png"    #中级敌机撞到爆炸第四张图片
    enemy2_hit_image = basepath + r"\images\enemy2_hit.png"   #中级敌机碰撞图片
    enemy2_image = basepath + r"\images\enemy2.png"  #中级敌机图片
    enemy3_down1_image = basepath + r"\images\enemy3_down1.png"    #高级敌机撞到爆炸第四张图片
    enemy3_down2_image = basepath + r"\images\enemy3_down2.png"    #高级敌机撞到爆炸第四张图片
    enemy3_down3_image = basepath + r"\images\enemy3_down3.png"    #高级敌机撞到爆炸第四张图片
    enemy3_down4_image = basepath + r"\images\enemy3_down4.png"    #高级敌机撞到爆炸第四张图片
    enemy3_down5_image = basepath + r"\images\enemy3_down5.png"    #高级敌机撞到爆炸第四张图片
    enemy3_down6_image = basepath + r"\images\enemy3_down6.png"    #高级敌机撞到爆炸第四张图片
    enemy3_hit_image = basepath + r"\images\enemy3_hit.png"  #高级敌机碰撞图片
    enemy3_n1_image = basepath + r"\images\enemy3_n1.png"   #高级敌机图片1
    enemy3_n2_image = basepath + r"\images\enemy3_n2.png"   #高级敌机图片2
    gameover_image = basepath + r"\images\gameover.png"    #游戏结束图片
    life_image = basepath + r"\images\life.png"    #表示生命值的图片
    me_destory_1_image = basepath + r"\images\me_destroy_1.png"    #自身飞机炸毁第一张图片
    me_destory_2_image = basepath + r"\images\me_destroy_2.png"    #自身飞机炸毁第二张图片
    me_destory_3_image = basepath + r"\images\me_destroy_3.png"    #自身飞机炸毁第三张图片
    me_destory_4_image = basepath + r"\images\me_destroy_4.png"    #自身飞机炸毁第四张图片
    me1_image = basepath + r"\images\me1.png" #自身飞机第一张图片
    me2_image = basepath + r"\images\me2.png" #自身飞机第二张图片
    pause_nor_image = basepath + r"\images\pause_nor.png"   #暂停的时候图片
    pause_pressed_image = basepath + r"\images\pause_pressed.png"   #暂停到继续的中间变换图
    resume_nor_image = basepath + r"\images\resume_nor.png"  #继续的时候的图片
    resume_pressed_image =basepath + r"\images\resume_pressed.png"   #继续到暂停的中间变换图

    """设置背景"""
    bg_size = width,height = 430,700 #背景大小
    screen = pygame.display.set_mode(bg_size) #这是背景大小
    background = pygame.image.load(Background_image).convert_alpha() #画背景
    pygame.mixer.music.set_volume(1) #设置音量
    pygame.mixer.music.play(-1) #播放背景音乐，-1表示无限循环

    #生成飞机
    myself = MyPlane(bg_size)

    #生成敌机组

    def add_smallenemies(group1,group2,num):
        for i in range(num):
            e1 = SmallEnemy(bg_size)
            group1.add(e1)
            group2.add(e1)

    def add_middleenemies(group1,group2,num):
        for i in range(num):
            e2 = MiddleEnemy(bg_size)
            group1.add(e2)
            group2.add(e2)

    def add_bigenemies(group1,group2,num):
        for i in range(num):
            e3 = BigEnemy(bg_size)
            group1.add(e3)
            group2.add(e3)

    #生成敌机组
    enemies = pygame.sprite.Group() #生成整个飞机组

    smallenemies = pygame.sprite.Group() #生成小飞机组
    add_smallenemies(smallenemies,enemies,20)

    middleenemies = pygame.sprite.Group() #生成中飞机组
    add_middleenemies(middleenemies,enemies,10)

    bigenemies = pygame.sprite.Group() #生成大飞机组
    add_bigenemies(bigenemies,enemies,4)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.blit(background,(0,0)) #绘制背景

        #绘制大型敌机
        for each in bigenemies:
            each.move()
            if switch_image:
                switch_image = False
                screen.blit(each.enemy3_n1,each.rect)
            else:
                switch_image = True
                screen.blit(each.enemy3_n2,each.rect)
            #即将出现在画面中，播放音效
            if each.rect.bottom > -50:
                # print(enemy3_fly_music)
                enemy3_fly_music.play()

        #绘制中型敌机
        for each in middleenemies:
            each.move()
            screen.blit(each.enemy2,each.rect)

        #绘制小型敌机
        for each in smallenemies:
            each.move()
            screen.blit(each.enemy1,each.rect)

        #绘制飞机
        if transform: #如果改变属性为真 画第一张飞机图
            if delay == 0:
                delay = 100
            delay -= 1
            transform  =False #改变属性来达到改变图片的效果
        else: #如果改变属性为假 画第二张飞机图
            if delay == 0:
                delay = 100
            delay -= 1
            transform = True
        
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
    