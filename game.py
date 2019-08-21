import os
import random
import pygame
from font import *

# 敌机出现
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 玩家发射子弹事件
PLAYER_FIRE_EVENT = pygame.USEREVENT + 1
# 敌机1
ENEMY1_IMG = os.getcwd() + "\\images\\enemy1.png"
# 敌机2
ENEMY2_IMG = os.getcwd() + "\\images\\enemy2.png"
# boss
ENEMY3_IMG = os.getcwd() + "\\images\\enemy3_n1.png"
# 玩家飞机
PLAYER_IMG = os.getcwd() + "\\images\\me1.png"
# 背景图片
BACKGROUND_IMG = os.getcwd() + "\\images\\background.png"
# 子弹1
BULLET1_IMG = os.getcwd() + "\\images\\bullet1.png"
# 子弹2
BULLET2_IMG = os.getcwd() + "\\images\\bullet2.png"
# 屏幕尺寸
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)


# 运动元素
class AniElement:
    def __init__(self, image_src):
        import uuid
        self.key = uuid.uuid4()                                # 用于唯一标识
        self.image = pygame.image.load(image_src)              # 用于绘制
        self.rect = self.image.get_rect()                      # 得到图片的区域尺寸

    def draw(self, screen):
        # 如果screen类型错误 , 报错
        assert [isinstance(screen, pygame.Surface),
                "screen类型错误,应该是pygame.Surface"]

        screen.blit(self.image, [self.rect.centerx, self.rect.centery])
        if hasattr(self, "_hp"):
            hp_progress = pygame.Surface(
                (self.rect.width * self._hp / self.hp, 10))
            hp_progress_bg = pygame.Surface((self.rect.width, 10))
            hp_progress.fill((144, 238, 144))
            hp_progress_bg.fill((200, 200, 200))
            screen.blit(hp_progress_bg, [
                        self.rect.centerx, self.rect.centery - 15])
            screen.blit(hp_progress, [
                        self.rect.centerx, self.rect.centery - 15])


# 飞机类
class Plane(AniElement):
    def __init__(self, image_src, hp=10, speedX=1, speedY=0, life=1, bullet=None):
        import random
        super().__init__(image_src)
        self.image_src = image_src
        self.hp = hp                                           # hp
        self._hp = hp                                          # 用于计算是否被击落
        self.speedX = speedX                                   # 水平移动速度
        self.speedY = speedY                                   # 竖直移动速度
        self.life = life                                       # 生命
        self.bullet = bullet                                   # 装载的子弹
        self.bullet_group = list()                             # 子弹集
        self.rect.centerx = random.randint(1, 480)             # 初始水平坐标
        self.rect.centery = -self.rect.height                  # 初始竖直坐标

    def fly(self):
        # 移动
        self.rect.centerx += self.speedX
        self.rect.centery += self.speedY

        # 判断是否出界
        if self.rect.centery > SCREEN_RECT.bottom:
            self.kill()

    def kill(self):
        # 销毁
        self.life = 0

    def load_bullet(self):
        # 发射子弹
        if self.bullet:          # 如果没有装子弹，不能发射
            bullet = self.bullet.generate()
            bullet.set_pos(self.rect.left +
                           self.rect.width, self.rect.centery)
            self.bullet_group.append(bullet)
            return True
        else:
            return False

    def attack(self, screen):
        for index, bullet in enumerate(self.bullet_group):
            bullet.fly()
            bullet.draw(screen)
            if bullet.life < 1:
                del self.bullet_group[index]

    def be_attacked(self, damage):
        print("受到伤害:", damage)
        self._hp -= damage
        if self._hp <= 0:
            self.kill()


# 子弹
class Bullet(AniElement):
    def __init__(self, type=0, damage=10):
        # self.type = type
        self.type = type
        self.life = 1
        self.damage = damage
        self.speedY = 10
        if type == 0:
            super().__init__(BULLET1_IMG)
        else:
            super().__init__(BULLET2_IMG)
        self.rect.centerx = 0
        self.rect.centery = 0

    def fly(self):
        self.rect.centery -= self.speedY             # 子弹是反向飞行
        # 判断是否出界
        if self.rect.centery < SCREEN_RECT.top:
            self.kill()

    def set_pos(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y

    def generate(self):
        return Bullet(self.type, self.damage)

    def kill(self):
        self.life = 0

    def set_damage(self, damage):
        self.damage = damage

# 敌机


class Enemy(Plane):
    def __init__(self, type=1):
        if type <= 60:                # 小型
            data = {
                "image_src": ENEMY1_IMG, "hp": 10, "speedX": 0, "speedY": 5, "life": 1, "bullet": None
            }
        elif type <= 90:              # 中型
            data = {
                "image_src": ENEMY2_IMG, "hp": 30, "speedX": 0, "speedY": 3, "life": 1, "bullet": None
            }
        elif type <= 100:              # 大型
            data = {
                "image_src": ENEMY3_IMG, "hp": 150, "speedX": 0, "speedY": 1, "life": 1, "bullet": None
            }
        else:
            data = {
                "image_src": ENEMY1_IMG, "hp": 10, "speedX": 0, "speedY": 5, "life": 1, "bullet": None
            }
        super().__init__(**data)


# 玩家飞机
class Player(Plane):
    # TODO: 击落一定飞机，提升等级
    def __init__(self, image_src=PLAYER_IMG, hp=10, speed=10, speedX=0, speedY=0, life=1, bullet=Bullet(0)):
        super().__init__(image_src=PLAYER_IMG, hp=hp, speedX=speedX,
                         speedY=speedY, life=life, bullet=bullet)
        self.rect.centerx = SCREEN_RECT.width / 2 - self.rect.width / 2          # 初始x
        self.rect.centery = SCREEN_RECT.height - self.rect.height               # 初始y
        # 玩家的移动速度
        self.speed = speed
        # 玩家分数
        self.score = 0
        # 玩家等级
        self.level = 1
        # 上个位置
        self.last_pos = (self.rect.centerx, self.rect.centery)

    def fly(self, direction: str = "stay"):
        # FIXME: 飞行界限判断不准确, rect不熟悉
        if direction == "right":
            self.rect.centerx += self.speed
        elif direction == "left":
            self.rect.centerx -= self.speed
        elif direction == "up":
            self.rect.centery -= self.speed
        elif direction == "down":
            self.rect.centery += self.speed

        # 判断是否出界
        if self.rect.centery < SCREEN_RECT.top:
            self.rect.centery = SCREEN_RECT.top
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

        if self.rect.centerx < SCREEN_RECT.left:
            self.rect.centerx = SCREEN_RECT.left
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def add_score(self, value):
        self.score += value
        if self.score // self.bullet.damage >= 100:
            self.level_up()
            self.update_bullet_damage()
            self.update_bullet_tension()
        elif self.score // self.bullet.damage >= 50:
            self.level_up()
            self.update_bullet_damage()

    def level_up(self):
        self.level += 1
        print("升级,当前等级:", self.level)

    def update_bullet_damage(self):
        self.bullet.set_damage(self.bullet.damage+5)
        print("升级,当前子弹伤害:", self.bullet.damage)

    def update_bullet_tension(self):
        Game.set_player_fire_event_interval(
            int(Game.player_fire_interval*0.98))
        print("升级,当前子弹攻击速度:", Game.player_fire_interval)

    def get_score(self):
        return self.score

    def get_level(self):
        return self.level

    def get_last_pos(self):
        return self.last_pos

    def get_speed(self):
        return self.speed


class Background(AniElement):
    def __init__(self, image_src=BACKGROUND_IMG, speedY: int = 1, is_alt=False):
        super().__init__(image_src)
        self.rect.centerx = 0
        self.is_alt = is_alt
        if self.is_alt:
            self.rect.centery = -self.rect.height
        else:
            self.rect.centery = 0
        self.speedY = speedY

    def move(self):
        self.rect.centery += self.speedY
        if self.rect.centery > self.rect.height and not self.is_alt:
            self.rect.centery = 0
        elif self.rect.centery > 0 and self.is_alt:
            self.rect.centery = - self.rect.height


class ScoreInfo:
    def __init__(self, score: int = 0):
        self.score = score
        self.text = "分数:\t\t" + str(self.score)
        self.font = pygame.font.Font(SIYUAN_HEITI_MEDIUM_SOURCE, 18)
        self.surf = self.font.render(self.text, 1, (0, 0, 0))

    def update(self, score):
        self.score = score
        self.text = "分数:\t\t" + str(self.score)

    def add(self, increment):
        self.score += increment

    def minus(self, decrement):
        self.score -= decrement

    def multiply(self, multiplier):
        self.score *= multiplier

    def divide(self, divisor):
        self.score /= divisor

    def draw(self, screen):
        # 如果screen类型错误 , 报错
        self.surf = self.font.render(self.text, 1, (0, 0, 0))
        assert [isinstance(screen, pygame.Surface),
                "screen类型错误,应该是pygame.Surface"]

        screen.blit(self.surf, [360, 40])


# FIXME: 生成的飞机比例有误，高难度的太多
class Game:
    def __init__(self, screen):
        # Game Control Class
        self.screen = screen
        self.player = Player()
        self.background = Background()
        self.background2 = Background(is_alt=True)
        self.scoreinfo = ScoreInfo()
        self.enemy_group = list()
        self.create_enemey_event_interval = 1000                 # 毫秒
        self.player_fire_event_interval = 500                    # 毫秒
        # 每1.5秒生成一个敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 每0.5秒发射子弹
        pygame.time.set_timer(PLAYER_FIRE_EVENT, 500)

    def set_player_fire_event_interval(self, interval):
        self.player_fire_event_interval = interval
        pygame.time.set_timer(PLAYER_FIRE_EVENT, interval)

    def set_create_enemy_event_interval(self, interval):
        self.create_enemey_event_interval = interval
        pygame.time.set_timer(CREATE_ENEMY_EVENT, interval)

    @staticmethod
    @property
    def create_enemey_interval(self):
        return self.create_enemey_event_interval

    @staticmethod
    @property
    def player_fire_interval(self):
        return self.player_fire_event_interval

    def start(self):
        # 开始游戏
        self.scoreinfo.draw(self.screen)
        self.background.draw(self.screen)
        self.background2.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()

    def pause(self):
        # 暂停游戏
        pass

    def end(self):
        # 游戏结束，出示分数
        print(abs(self.player.score))
        exit()

    def add_enemy_group(self, enemy):
        assert [isinstance(enemy, Enemy), "类型错误"]
        self.enemy_group.append(enemy)

    def element_update(self):
        # 更新画面
        self.screen.fill((255,255,255))
        self.background.move()
        self.background2.move()
        self.player.fly()
        self.collision_check()
        self.scoreinfo.update(self.player.get_score())
        self.background.draw(self.screen)
        self.background2.draw(self.screen)
        self.player.attack(self.screen)
        self.player.draw(self.screen)
        self.scoreinfo.draw(self.screen)
        for index, enemy in enumerate(self.enemy_group):
            if not enemy.life < 1:
                enemy.fly()
                enemy.draw(self.screen)
            else:
                del self.enemy_group[index]
        pygame.display.flip()

    def collision_check(self):
        # FIXME: 需要修正一些失效的碰撞反应
        # 检测碰撞
        enemy_group = self.enemy_group
        bullet_group = self.player.bullet_group
        player = self.player
        for enemy in enemy_group:
            # 检测敌机是否与子弹碰撞
            for bullet in bullet_group:
                if pygame.Rect.colliderect(bullet.rect, enemy.rect):
                    enemy.be_attacked(bullet.damage)
                    if enemy.life < 1:
                        player.add_score(enemy.hp)
                    bullet.kill()
            # 检测敌机与玩家碰撞
            if pygame.Rect.colliderect(enemy.rect, player.rect):
                enemy.kill()
                print("得分:", player.score)
                # self.end()
