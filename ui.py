import os
import pygame
import font
from game import *

UI_MODE = ["开始界面", "游戏界面", "排行榜界面", "关于作者界面", "设置界面"]


class UI:
    def __init__(self):
        print("UI加载成功")
        self.mode = UI_MODE[0]       # 开始界面
        self.lastmode = UI_MODE[0]
        self.game_control = None

    def show_welcome_ui(self, screen_handler):
        # mode位 置：开始界面
        self.mode = UI_MODE[0]
        # 窗口尺寸
        width = screen_handler.get_width()
        height = screen_handler.get_height()
        # 背景
        background_img = os.getcwd() + "/images/background.png"
        background_surf = pygame.image.load(background_img)
        # 字体
        btn_font = pygame.font.Font(font.SIYUAN_HEITI_LIGHT_SOURCE, 25)
        # 字体颜色
        btn_text_color = (255, 255, 255)
        # 开始游戏按钮
        starting_btn_text = "开始游戏"
        starting_btn_surf = btn_font.render(
            starting_btn_text, 1, btn_text_color)
        # 设置按钮
        setting_btn_text = "设置"
        setting_btn_surf = btn_font.render(
            setting_btn_text, 1, btn_text_color)
        # 关于这座按钮
        about_btn_text = "关于作者"
        about_btn_surf = btn_font.render(about_btn_text, 1, btn_text_color)
        # 排行榜按钮
        rank_btn_text = "排行榜"
        rank_btn_surf = btn_font.render(rank_btn_text, 1, btn_text_color)
        # 退出游戏按钮
        exit_btn_text = "退出游戏"
        exit_btn_surf = btn_font.render(exit_btn_text, 1, btn_text_color)

        images_group = [
            (background_surf, [0, 0]),
            (starting_btn_surf, [
             width/2-starting_btn_surf.get_width()/2, height/2 + 60]),
            (setting_btn_surf, [
             width/2-setting_btn_surf.get_width()/2, height/2 + 90]),
            (about_btn_surf, [
             width/2-about_btn_surf.get_width()/2, height/2 + 120]),
            (rank_btn_surf, [
             width/2-rank_btn_surf.get_width()/2, height/2 + 150]),
            (exit_btn_surf, [
             width/2-exit_btn_surf.get_width()/2, height/2 + 180]),
        ]

        screen_handler.renderGroup(images_group)

    def show_gaming_ui(self, screen_handler):
        # mode位 置：游戏界面
        self.mode = UI_MODE[1]
        if not self.lastmode == self.mode:
            self.game_control = Game(screen_handler.screen)
            self.game_control.start()
        else:
            self.game_control.element_update()

    def show_rank_ui(self, screen_handler):
        # mode位 置：排行榜界面
        self.mode = UI_MODE[2]
        # 窗口尺寸
        width = screen_handler.get_width()
        height = screen_handler.get_height()
        # 背景
        background_img = os.getcwd() + "/images/background.png"
        background_surf = pygame.image.load(background_img)

        # 字体
        btn_font = pygame.font.Font(font.SIYUAN_HEITI_LIGHT_SOURCE, 25)
        # 字体颜色
        btn_text_color = (255, 255, 255)
        # 标题
        title_btn_text = "排行榜:"
        title_btn_surf = btn_font.render(
            title_btn_text, 1, btn_text_color)
        # 返回
        exit_btn_text = "返回主界面"
        exit_btn_surf = btn_font.render(exit_btn_text, 1, btn_text_color)

        images_group = [
            (background_surf, [0, 0]),
            (title_btn_surf, [
             width/2-title_btn_surf.get_width()/2, 100]),
            (exit_btn_surf, [
             width/2-exit_btn_surf.get_width()/2, height - 100]),
        ]

        screen_handler.renderGroup(images_group)

    def show_author_ui(self, screen_handler):
        # mode位 置：关于作者界面
        self.mode = UI_MODE[3]
        # 窗口尺寸
        width = screen_handler.get_width()
        height = screen_handler.get_height()
        # 背景
        background_img = os.getcwd() + "/images/background.png"
        background_surf = pygame.image.load(background_img)

        # 字体
        btn_font = pygame.font.Font(font.SIYUAN_HEITI_LIGHT_SOURCE, 25)
        # 字体颜色
        btn_text_color = (255, 255, 255)
        # 标题
        title_btn_text = "作者:"
        title_btn_surf = btn_font.render(
            title_btn_text, 1, btn_text_color)
        # 返回
        exit_btn_text = "返回主界面"
        exit_btn_surf = btn_font.render(exit_btn_text, 1, btn_text_color)

        images_group = [
            (background_surf, [0, 0]),
            (title_btn_surf, [
             width/2-title_btn_surf.get_width()/2, 100]),
            (exit_btn_surf, [
             width/2-exit_btn_surf.get_width()/2, height - 100]),
        ]

        screen_handler.renderGroup(images_group)

    def show_setting_ui(self, screen_handler):
        # mode位 置：设置界面
        self.mode = UI_MODE[4]
        # 窗口尺寸
        width = screen_handler.get_width()
        height = screen_handler.get_height()
        # 背景
        background_img = os.getcwd() + "/images/background.png"
        background_surf = pygame.image.load(background_img)

        # 字体
        btn_font = pygame.font.Font(font.SIYUAN_HEITI_LIGHT_SOURCE, 25)
        # 字体颜色
        btn_text_color = (255, 255, 255)
        # 窗口尺寸选项
        size_btn_text = "窗口尺寸:"
        size_btn_surf = btn_font.render(
            size_btn_text, 1, btn_text_color)
        # 刷新率选项
        fps_btn_text = "刷新率:"
        fps_btn_surf = btn_font.render(
            fps_btn_text, 1, btn_text_color)
        # 语言选项
        language_btn_text = "语言:"
        language_btn_surf = btn_font.render(
            language_btn_text, 1, btn_text_color)
        # 字体选项
        font_btn_text = "字体:"
        font_btn_surf = btn_font.render(font_btn_text, 1, btn_text_color)
        # 返回
        exit_btn_text = "返回主界面"
        exit_btn_surf = btn_font.render(exit_btn_text, 1, btn_text_color)

        images_group = [
            (background_surf, [0, 0]),
            (size_btn_surf, [
             50, 100]),
            (fps_btn_surf, [
             50, 200]),
            (language_btn_surf, [
             50, 300]),
            (font_btn_surf, [
             50, 400]),
            (exit_btn_surf, [
             width/2-exit_btn_surf.get_width()/2, height - 100]),
        ]

        screen_handler.renderGroup(images_group)

    def event_handle(self, screen_handler, mouse_pos=(0, 0), mouse_type=0):
        # 窗口尺寸
        width = screen_handler.get_width()
        height = screen_handler.get_height()
        if self.mode == UI_MODE[0]:
            # 主界面
            x, y = mouse_pos
            if width / 2 - 50 <= x <= width / 2 + 50 and height / 2 + 60 <= y <= height / 2 + 86:
                # 开始游戏按钮区域
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # 如果点击
                if mouse_type == 1:
                    self.mode = UI_MODE[1]
            elif width / 2 - 25 <= x <= width / 2 + 25 and height / 2 + 90 <= y <= height / 2 + 116:
                # 设置按钮区域
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # 如果点击
                if mouse_type == 1:
                    # 不允许其他操作
                    self.mode = UI_MODE[4]
            elif width / 2 - 50 <= x <= width / 2 + 50 and height / 2 + 120 <= y <= height / 2 + 146:
                # 关于作者按钮区域
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # 如果点击
                if mouse_type == 1:
                    # 不允许其他操作
                    self.mode = UI_MODE[3]
            elif width / 2 - 37.5 <= x <= width / 2 + 37.5 and height / 2 + 150 <= y <= height / 2 + 176:
                # 排行榜区域
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # 如果点击
                if mouse_type == 1:
                    # 不允许其他操作
                    self.mode = UI_MODE[2]
            elif width / 2 - 50 <= x <= width / 2 + 50 and height / 2 + 180 <= y <= height / 2 + 206:
                # 退出游戏区域
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # 如果点击
                if mouse_type == 1:
                    # 游戏结束
                    print("游戏结束...")
                    pygame.quit()
                    exit()
            else:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
        elif self.mode == UI_MODE[1]:
            # 游戏界面
            x, y = mouse_pos
            if width / 2 - 50 <= x <= width / 2 + 50 and height - 100 <= y <= height+26:
                # 返回按钮区域
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # 如果点击
                if mouse_type == 1:
                    self.mode = UI_MODE[0]
        elif self.mode == UI_MODE[2]:
            # 排行榜界面
            x, y = mouse_pos
            if width / 2 - 50 <= x <= width / 2 + 50 and height - 100 <= y <= height+26:
                # 返回按钮区域
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # 如果点击
                if mouse_type == 1:
                    self.mode = UI_MODE[0]
        elif self.mode == UI_MODE[3]:
            # 关于作者界面
            x, y = mouse_pos
            if width / 2 - 50 <= x <= width / 2 + 50 and height - 100 <= y <= height+26:
                # 返回按钮区域
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # 如果点击
                if mouse_type == 1:
                    self.mode = UI_MODE[0]
        elif self.mode == UI_MODE[4]:
            # 设置界面
            x, y = mouse_pos
            if width / 2 - 50 <= x <= width / 2 + 50 and height - 100 <= y <= height+26:
                # 返回按钮区域
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # 如果点击
                if mouse_type == 1:
                    self.mode = UI_MODE[0]
