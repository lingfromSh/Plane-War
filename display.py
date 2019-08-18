import random
import pygame
from file import *

# 窗口默认大小
DEFAULT_WINDOW_SIZE = (480, 700)
# 游戏默认刷新率
DEFAULT_FRAME_PER_SEC = 60
# TODO:显示模式(全屏, 无边框)
DISPLAY_MODE = 0


class Screen:
    def __init__(self, size=DEFAULT_WINDOW_SIZE, fps=DEFAULT_FRAME_PER_SEC):
        # 创建窗口
        self.screen = self.setWindowSize(self.getWindowSize() or size)
        # 设置窗口标题
        pygame.display.set_caption("飞机大战 ver:1.0.0")
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 刷新率
        self.fps = self.getFPS()

    # 功能：得到窗口大小, 若未找到或者新窗口尺寸非法则使用默认尺寸
    def getWindowSize(self):
        import json
        # 读取json配置文件
        try:
            with open("./setting.json", "r+", encoding="utf8") as f:
                setting_string = f.read()
                size = eval(json.loads(setting_string)["size"])
                if not isinstance(size, tuple):
                    print("采用默认窗口尺寸", DEFAULT_WINDOW_SIZE)
                    return DEFAULT_WINDOW_SIZE
                else:
                    print("采用配置窗口尺寸", size)
                    return size
        except FileNotFoundError as e:
            print("配置文件未找到")
            return DEFAULT_WINDOW_SIZE

    # 功能: 设置窗口大小, 成功返回True,失败返回False
    def setWindowSize(self, size=None):
        if not isinstance(size, tuple):
            return False
        # 更改窗口尺寸成功
        return pygame.display.set_mode(size)

    # 功能: 从配置文件中读取Fps大小
    def getFPS(self):
        import json
        # 读取json配置文件
        try:
            with open("./setting.json", "r+", encoding="utf8") as f:
                setting_string = f.read()
                fps = json.loads(setting_string)["fps"]
                if not isinstance(fps, int):
                    print("采用默认刷新率:", DEFAULT_FRAME_PER_SEC)
                    return DEFAULT_FRAME_PER_SEC
                else:
                    print("采用配置刷新率:", fps)
                    return fps
        except FileNotFoundError as e:
            print("配置文件未找到")
            return DEFAULT_FRAME_PER_SEC

    # 功能：设置游戏显示刷新率, 成功返回True,失败返回False
    def setFPS(self, fps=DEFAULT_FRAME_PER_SEC):
        # 默认刷新率 60
        if not isinstance(fps, int):
            return False
        return True

    # 返回窗口宽度
    @property
    def width(self):
        return self.get_width()

    # 返回窗口高度
    @property
    def height(self):
        return self.get_height()
    
    # 返回窗口宽度
    def get_width(self):
        return self.screen.get_width()
    
    # 返回窗口高度
    def get_height(self):
        return self.screen.get_height()
    
    # 画
    def render(self, image, position):
        self.screen.blit(image, position)
        self.refresh()
    
    # 画集体
    def renderGroup(self, images_group, flag=True):
        self.screen.blits(images_group)
        if flag:
            self.refresh()

    # 刷新画面
    def refresh(self):
        pygame.display.update()
    