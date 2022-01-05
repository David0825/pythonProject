# 导入sys和pygame模块
# 导入settings模块中的Settings类
import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源 pygame"""
        pygame.init()
        self.settings = Settings()
        # 创建游戏显示窗口，指定游戏窗口的尺寸
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 全屏模式下运行
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien_Invasion")
        # 创建一个用于存储游戏统计信息的实例
        self.stats = GameStats(self)
        #创建得分牌
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        # 设置背景色
        self.bg_color = self.settings.bg_color
        # 将子弹存储到编组中
        self.bullets = pygame.sprite.Group()
        # 创建一个用于存储外星人群的编组
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # 创建play按钮
        self.play_button = Button(self, "play")

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    # 定义管理事件的方法
    def _check_events(self):
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # #响应键盘事件
                # if event.key == pygame.K_RIGHT:
                #     #向右持续移动飞船
                #     # self.ship.rect.x += 1
                #     self.ship.moving_right = True
                # elif event.key == pygame.K_LEFT:
                #     self.ship.moving_left = True
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                # if event.key == pygame.K_RIGHT:
                #     # 停止向右持续移动飞船
                #     self.ship.moving_right = False
                # elif event.key == pygame.K_LEFT:
                #     self.ship.moving_left = False
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    # 重构_check_events()
    def _check_keydown_events(self, event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            # 向右持续移动飞船
            # self.ship.rect.x += 1
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            # 按'q退出'
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            # 停止向右持续移动飞船
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        # 开火
        """创建一颗子弹，并将其加入编组bullets中"""
        """检查未消失的子弹数量是否小于限制的子弹数量"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # 更新子弹位置
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # 检查是否有子弹击中了外星人
        # 如果是，就删除相应的子弹和外星人
        """
        collisions中每个与外星人碰撞的子弹都是字典的key，
        与每个子弹相关的值都是一个列表，其中包含该子弹击中的外星人
        """
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                #更新得分
                self.sb.prep_score()
                #检查最高分
                self.sb.check_high_score()
                #提高等级
                self.stats.level += 1
                self.sb.prep_level()
        # 生成新的外星人
        if not self.aliens:
            # 删除现有的子弹并新建一群外星人
            self.bullets.empty()
            self._create_fleet()
            #提高外星人移动速度,飞船移动速度，子弹移动速度，调整分数
            self.settings.increase_speed()

    def _update_aliens(self):
        """更新外星人群中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()
        # 检测外星人和飞船碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 检查是否有外星人到达了屏幕底端
        self._check_aliens_bottom()

    # 更新屏幕
    def _update_screen(self):
        # 每次循环时都重绘屏幕
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        # 子弹绘制到屏幕上
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 将外星人绘制到屏幕上
        self.aliens.draw(self.screen)

        #显示得分
        self.sb.show_score()
        # 如果游戏处于非活动状态，则绘制play按钮
        if not self.stats.game_active:
            self.play_button.draw_button()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _create_fleet(self):
        """创建外星人群"""
        # 创建一个外星人
        """
        创建一行外星人
        确定一行可容纳多个外星人
        available_space_x = settings.screen_with -(2 * alien_width)
        "//"整除运算符
        number_aliens_x = available_space_x // (2 * alien_width )
        """
        alien = Alien(self)
        # alien_width = alien.rect.width
        # alien.rect.size获取一个元组，包含外星人对象的宽度和高度
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # 计算屏幕可容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        for number_row in range(number_rows):
            # 创建第一行外星人
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, number_row)

    def _create_alien(self, alien_number, row_number):
        # 创建一个外星人并将其加入当前行
        alien = Alien(self)
        # alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    # 向下移动外星人群并改变移动方向
    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整群外星人下移，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """响应飞船被外星人撞到"""
        if self.stats.ships_left > 0:
            # 将ships_left 减1
            self.stats.ships_left -= 1;
            #更新剩余飞船
            self.sb.perp_ship()
            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人，并将飞船放到屏幕底端的中央
            self._create_fleet()
            self.ship.center_ship()
            # 暂停
            sleep(0.5)
        else:
            self.stats.game_active = False
            # 游戏结束后，重新显示光标
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕底端"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞到一样处理
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        # 判断玩家鼠标按下时的x,y坐标
        """在玩家单机play按钮时开始新游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #重置游戏设置
            self.settings.initialize_dynamic_settings()
            # 重置游戏统计信息
            self.stats.reset_stats()
            self.stats.game_active = True
            #重置得分
            self.sb.prep_score()
            #重置等级
            self.sb.prep_level()
            self.sb.perp_ship()

            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群新的外星人并让飞船居中
            self._create_fleet()
            self.ship.center_ship()

            # 隐藏鼠标光标
            pygame.mouse.set_visible(False)


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
