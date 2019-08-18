#  飞机大战 ver:1.0.0
#  作者： 凌诗韵
import pygame
from display import *
from game import *
from ui import *


class PlaneGame:
    def __init__(self):
        # 初始化游戏
        pygame.init()
        print("游戏初始化")
        # 上一个界面
        self.lastmode = None
        # 创建显示控制
        self.screen_handler = Screen()
        # 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 创建画面ui控制
        self.ui_handler = UI()

    def start(self):
        print("游戏开始...")
        while True:
            # 刷新率
            self.clock.tick(self.screen_handler.fps)
            # 界面
            self.__create_ui()
            # 事件处理
            self.__event_handler()
            # 刷新画面
            self.screen_handler.refresh()

    def __create_ui(self):
        # 禁止重复创建
        # ui控制的mode
        mode = self.ui_handler.mode
        if mode == UI_MODE[0] and not self.lastmode == UI_MODE[0]:
            self.ui_handler.show_welcome_ui(self.screen_handler)
            self.lastmode = UI_MODE[0]
        elif mode == UI_MODE[1]:
            self.ui_handler.show_gaming_ui(self.screen_handler)
            self.ui_handler.lastmode = UI_MODE[1]
        elif mode == UI_MODE[2] and not self.lastmode == UI_MODE[2]:
            self.ui_handler.show_rank_ui(self.screen_handler)
            self.lastmode = UI_MODE[2]
        elif mode == UI_MODE[3] and not self.lastmode == UI_MODE[3]:
            self.ui_handler.show_author_ui(self.screen_handler)
            self.lastmode = UI_MODE[3]
        elif mode == UI_MODE[4] and not self.lastmode == UI_MODE[4]:
            self.ui_handler.show_setting_ui(self.screen_handler)
            self.lastmode = UI_MODE[4]

    def __event_handler(self):
        # 事件处理
        mode = self.ui_handler.mode
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.game_over()
            elif event.type == CREATE_ENEMY_EVENT and mode == UI_MODE[1]:
                import random
                # 创建一个敌机(随机生成)
                type = random.randint(1, 3)
                enemy = Enemy(type)
                self.ui_handler.game_control.add_enemy_group(enemy)
            elif event.type == PLAYER_FIRE_EVENT and mode == UI_MODE[1]:
                self.ui_handler.game_control.player.load_bullet()
            elif event.type == pygame.KEYDOWN and mode != UI_MODE[1]:
                key = event.key
                if key == pygame.K_ESCAPE:
                    PlaneGame.game_over()
            elif event.type == pygame.MOUSEBUTTONDOWN and mode != UI_MODE[1]:
                # 得到鼠标坐标
                x, y = pygame.mouse.get_pos()
                ui_mode = self.ui_handler.mode
                # 区别界面状态
                self.ui_handler.event_handle(
                    self.screen_handler, mouse_pos=(x, y), mouse_type=1)
            elif event.type == pygame.MOUSEMOTION and mode != UI_MODE[1]:
                # 得到鼠标坐标
                x, y = pygame.mouse.get_pos()
                ui_mode = self.ui_handler.mode
                # 区别界面状态
                self.ui_handler.event_handle(
                    self.screen_handler, mouse_pos=(x, y), mouse_type=0)
        if mode == UI_MODE[1]:
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                self.ui_handler.game_control.player.fly("left")
            elif key[pygame.K_RIGHT]:
                self.ui_handler.game_control.player.fly("right")
            elif key[pygame.K_UP]:
                self.ui_handler.game_control.player.fly("up")
            elif key[pygame.K_DOWN]:
                self.ui_handler.game_control.player.fly("down")

    @staticmethod
    def game_over():
        print("游戏结束...")
        # 游戏退出
        pygame.quit()
        exit()


if __name__ == "__main__":
    # 创建一个游戏实例
    game = PlaneGame()
    # 开始游戏
    game.start()
