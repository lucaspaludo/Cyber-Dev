import pygame
import math
import sys
import random
from dataclasses import dataclass

WIDTH, HEIGHT = 960, 540
FPS = 60
GRAVITY = 2200
MOVE_SPEED = 350
JUMP_SPEED = 900
FRICTION = 0.0008
ANALOG_DEADZONE = 0.2
BULLET_SPEED = 750
MAX_BULLETS = 6

BTN_A_OR_CROSS = 0
BTN_B_OR_CIRCLE = 1
BTN_X_OR_SQUARE = 2
BTN_Y_OR_TRIANGLE = 3
BTN_LB = 4
BTN_RB = 5
BTN_BACK = 6
BTN_START = 7
BTN_LS = 8
BTN_RS = 9

@dataclass
class Bullet:
    x: float
    y: float
    vx: float
    vy: float
    owner: int
    life: float = 1.6

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.life -= dt

    def alive(self):
        return 0 <= self.x <= WIDTH and 0 <= self.y <= HEIGHT and self.life > 0

class Player:
    def __init__(self, x, y, color=(80,200,255)):
        self.start_x = x
        self.start_y = y
        self.color = color
        self.reset()

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.vx = 0
        self.vy = 0
        self.w = 40
        self.h = 56
        self.on_ground = False
        self.facing = 1
        self.cooldown = 0
        self.lives = 10
        self.score = 0

    def rect(self):
        return pygame.Rect(int(self.x - self.w/2), int(self.y - self.h), self.w, self.h)

    def update(self, dt, platforms):
        self.vy += GRAVITY * dt
        self.vy = max(min(self.vy, 1500), -1500)
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.on_ground = False
        r = self.rect()
        for p in platforms:
            if r.colliderect(p):
                prev_r = pygame.Rect(int(self.x - self.w/2), int(self.y - self.h - self.vy * dt), self.w, self.h)
                if prev_r.bottom <= p.top and self.vy > 0:
                    self.y = p.top
                    self.vy = 0
                    self.on_ground = True
                elif prev_r.top >= p.bottom and self.vy < 0:
                    self.y = p.bottom + self.h
                    self.vy = 0
                else:
                    prev_r = pygame.Rect(int(self.x - self.w/2 - self.vx * dt), int(self.y - self.h), self.w, self.h)
                    if prev_r.right <= p.left and self.vx > 0:
                        self.x = p.left - self.w/2
                        self.vx = 0
                    elif prev_r.left >= p.right and self.vx < 0:
                        self.x = p.right + self.w/2
                        self.vx = 0
                r = self.rect()
        if self.on_ground:
            if abs(self.vx) < 5:
                self.vx = 0
            else:
                self.vx -= self.vx * FRICTION * (dt * 1000)
        if self.cooldown > 0:
            self.cooldown -= dt

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect(), border_radius=8)
        eye_x = self.rect().centerx + (self.w//4) * self.facing
        eye_y = self.rect().top + 16
        pygame.draw.circle(surf, (10, 30, 40), (eye_x, eye_y), 4)

    def move_axis(self, ax):
        self.vx = MOVE_SPEED * ax
        if abs(ax) > 0.05:
            self.facing = 1 if ax > 0 else -1

    def jump(self):
        if self.on_ground:
            self.vy = -JUMP_SPEED
            return True
        return False

    def can_shoot(self):
        return self.cooldown <= 0

    def shoot(self, owner_id):
        self.cooldown = 0.18
        bx = self.rect().centerx + self.facing * (self.w//2)
        by = self.rect().centery - 6
        return Bullet(bx, by, BULLET_SPEED * self.facing, 0, owner=owner_id)

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 36
        self.h = 40
        self.vx = random.choice([-80, 80])
        self.color = (200, 70, 70)
        self.alive = True

    def rect(self):
        return pygame.Rect(int(self.x - self.w/2), int(self.y - self.h), self.w, self.h)

    def update(self, dt, platforms):
        self.x += self.vx * dt
        r = self.rect()
        for p in platforms:
            if r.colliderect(p):
                if r.bottom <= p.top + 5:
                    self.y = p.top
                if r.left <= p.left or r.right >= p.right:
                    self.vx *= -1

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect(), border_radius=6)

class Collectible:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 10
        self.color = (255, 220, 0)
        self.collected = False

    def rect(self):
        return pygame.Rect(int(self.x-self.r), int(self.y-self.r), self.r*2, self.r*2)

    def draw(self, surf):
        if not self.collected:
            pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), self.r)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Jogo 2 Jogadores (Controle + Teclado)")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 20)

        self.level = 1
        self.player1 = Player(380, 270, (80,200,255))  
        self.player2 = Player(330, 270, (80,255,120))  
        self.platforms = []
        self.bullets = []
        self.enemies = []
        self.collectibles = []

        pygame.joystick.init()
        self.joy = None
        self._scan_joysticks()

        self.running = True
        self.paused = False
        self.game_over = False

        self.create_level(self.level)

    def create_level(self, level):
        base_y = HEIGHT - 40
        self.platforms = [
            pygame.Rect(0, base_y, WIDTH, 40),
            pygame.Rect(100, base_y-100, 200, 20),
            pygame.Rect(400, base_y-200, 240, 20),
            pygame.Rect(700, base_y-300, 140, 20),
            pygame.Rect(50, base_y-350, 120, 20)
        ]
        self.enemies = []
        for plat in self.platforms[1:]:
            for _ in range(level):
                x = random.randint(plat.left+20, plat.right-20)
                y = plat.top
                self.enemies.append(Enemy(x, y))
        self.collectibles = []
        for plat in self.platforms[1:]:
            x = random.randint(plat.left+20, plat.right-20)
            y = plat.top - 20
            self.collectibles.append(Collectible(x, y))
        self.player1.reset()
        self.player2.reset()
        self.bullets = []

    def _scan_joysticks(self):
        self.joy = None
        for i in range(pygame.joystick.get_count()):
            j = pygame.joystick.Joystick(i)
            j.init()
            self.joy = j
            break

    def handle_input(self, dt):
        keys = pygame.key.get_pressed()

        move_axis2 = 0
        if keys[pygame.K_a]:
            move_axis2 -= 1
        if keys[pygame.K_d]:
            move_axis2 += 1
        self.player2.move_axis(move_axis2)
        if keys[pygame.K_w]:
            self.player2.jump()
        if keys[pygame.K_RETURN]:
            if self.player2.can_shoot() and len(self.bullets) < MAX_BULLETS:
                self.bullets.append(self.player2.shoot(owner_id=2))

        move_axis1 = 0
        jump1 = False
        shoot1 = False
        if keys[pygame.K_LEFT]:
            move_axis1 -= 1
        if keys[pygame.K_RIGHT]:
            move_axis1 += 1
        if keys[pygame.K_UP]:
            jump1 = True
        if keys[pygame.K_RCTRL]:
            shoot1 = True
        if self.joy:
            ax0 = self.joy.get_axis(0)
            if abs(ax0) < ANALOG_DEADZONE:
                ax0 = 0.0
            move_axis1 = ax0 if abs(ax0) > abs(move_axis1) else move_axis1
            def safe_btn(i):
                return self.joy.get_button(i) if i < self.joy.get_numbuttons() else 0
            if safe_btn(BTN_A_OR_CROSS):
                jump1 = True
            if safe_btn(BTN_B_OR_CIRCLE) or safe_btn(BTN_RB) or safe_btn(BTN_X_OR_SQUARE):
                shoot1 = True

        self.player1.move_axis(move_axis1)
        if jump1:
            self.player1.jump()
        if shoot1 and self.player1.can_shoot() and len(self.bullets) < MAX_BULLETS:
            self.bullets.append(self.player1.shoot(owner_id=1))

    def update(self, dt):
        if self.paused or self.game_over:
            return
        self.player1.update(dt, self.platforms)
        self.player2.update(dt, self.platforms)
        for b in self.bullets:
            b.update(dt)
        self.bullets = [b for b in self.bullets if b.alive()]
        for e in self.enemies:
            e.update(dt, self.platforms)

        for player_id, player in enumerate([self.player1, self.player2], start=1):
            for e in self.enemies:
                if e.alive and player.rect().colliderect(e.rect()):
                    player.lives -= 1
                    e.alive = False
            for b in self.bullets:
                if b.owner == player_id:
                    for e in self.enemies:
                        if e.alive and e.rect().collidepoint(b.x, b.y):
                            e.alive = False
                            player.score += 50
            for c in self.collectibles:
                if not c.collected and player.rect().colliderect(c.rect()):
                    c.collected = True
                    player.score += 100

        self.enemies = [e for e in self.enemies if e.alive]
        if all(c.collected for c in self.collectibles) or len(self.enemies) == 0:
            self.level += 1
            self.create_level(self.level)
        if self.player1.lives <= 0 and self.player2.lives <= 0:
            self.game_over = True

    def draw(self):
        self.screen.fill((18,18,20))
        for p in self.platforms:
            pygame.draw.rect(self.screen, (60,65,90), p, border_radius=6)
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)
        for b in self.bullets:
            pygame.draw.circle(self.screen, (255,240,90), (int(b.x), int(b.y)), 6)
        for e in self.enemies:
            e.draw(self.screen)
        for c in self.collectibles:
            c.draw(self.screen)
        hud1 = self.font.render(f"P1 Score: {self.player1.score} Lives: {self.player1.lives}", True, (200,220,255))
        hud2 = self.font.render(f"P2 Score: {self.player2.score} Lives: {self.player2.lives}", True, (200,255,200))
        level_text = self.font.render(f"Level: {self.level}", True, (255,255,255))
        self.screen.blit(hud1, (16,16))
        self.screen.blit(hud2, (16,40))
        self.screen.blit(level_text, (WIDTH//2 - level_text.get_width()//2, 16))
        if self.game_over:
            s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            s.fill((0,0,0,180))
            self.screen.blit(s,(0,0))
            gmsg = self.font.render("GAME OVER - Pressione qualquer tecla", True, (255,60,60))
            self.screen.blit(gmsg, (WIDTH//2 - gmsg.get_width()//2, HEIGHT//2))
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS)/1000.0
            self.handle_events()
            self.handle_input(dt)
            self.update(dt)
            self.draw()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Game().run()
