"""
Author:trf
Email:TRF_873@163.com
Time:2022/3/6
"""
import traceback
import tkinter as tk
import pygame
import math
import sys

"""我的飞机类"""

class Myplan(pygame.sprite.Sprite): #定义我的飞机类，继承动画精灵类（因为之后要进行碰撞检测）
    def __init__(self, bg_size) -> None:
        self.me1_image = r"D:\python_projects\feijidazhan\images\me1.png" #自身飞机第一张图片
        self.me2_image = r"D:\python_projects\feijidazhan\images\me2.png" #自身飞机第二张图片
        self.image1 = pygame.image.load(self.me1_image).convert_alpha() #第一张飞机图片
        self.image2 = pygame.image.load(self.me2_image).convert_alpha() #第二章飞机图片，为了做出飞机喷气的效果
        self.rect = self.image1.get_rect() #获得飞机图片的尺寸
        self.width ,self.height = bg_size[0],bg_size[1] #设置飞机允许活动地点
        self.rect.left,self.rect.top[(self.width-self.rect.width) // 2 , (self.height - self.rect.height -60)] #设置我方飞机出现的位置

        self.speed = 10 #设置飞机出现的速度


def main():
    pygame.init() # 初始化
    pygame.mixer.init() #混音器初始化

    clock = pygame.time.Clock() #设置一个计时器


    """载入音乐文件"""
    #背景音乐
    pygame.mixer.music.load(r"D:\python_projects\feijidazhan\sound\game_music.ogg") #设置背景音乐
    pygame.mixer.music.set_volume(1) #设置音量

    #游戏音效
    bullet_music = r"D:\python_projects\feijidazhan\sound\bullet.wav" #子弹音效
    button_music = r"D:\python_projects\feijidazhan\sound\bytton.wav" #按键音效
    enemy1_down_music = r"D:\python_projects\feijidazhan\sound\enemy1_down.wav" #低等级敌机击毁音效
    enemy2_down_music = r"D:\python_projects\feijidazhan\sound\enemy2_down.wav" #中等级敌机击毁音效
    enemy3_down_nusic = r"D:\python_projects\feijidazhan\sound\enemy3_down.wav" #高等级敌机击毁音效
    get_bomb_music = r"D:\python_projects\feijidazhan\sound\get_bomb.wav" #获得全屏炸弹音效
    get_bullet_music = r"D:\python_projects\feijidazhan\sound\get_bullet.wav" #获得双倍子弹补给音效
    me_down_music = r"D:\python_projects\feijidazhan\sound\me_down.wav" #自身飞机杯击毁音效
    supply_music = r"D:\python_projects\feijidazhan\sound\supply.wav" #补给产生音效
    upgrade_music = r"D:\python_projects\feijidazhan\sound\upgrade.wav" #升级音效
    use_bomb_music = r"D:\python_projects\feijidazhan\sound\use_bomb.wav" #使用全屏炸弹音效

    """图片文件路径"""
    again_image = r"D:\python_projects\feijidazhan\images\again.png" #重新开始图片路径
    Background_image = r"D:\python_projects\feijidazhan\images\background.png" #背景图路径

    """设置背景"""
    bg_size = width,height = 430,700 #背景大小
    screen = pygame.display.set_mode(bg_size) #这是背景大小
    background = pygame.image.load(Background_image).convert_alpha() #画背景
    pygame.mixer.music.play(-1) #播放背景音乐，-1表示无限循环

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(background,(0,0)) #绘制背景

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
    