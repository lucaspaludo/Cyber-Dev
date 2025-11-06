                    
import pygame
from sys import exit
import random

LARGURA_JANELA = 551
ALTURA_JANELA = 720

pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))


imagensPassaros = [
                    pygame.image.load('assets/bird_down.png'),
                    pygame.image.load('assets/bird_mid.png'),
                    pygame.image.load('assets/bird_up.png')
                  ]
imagemFundo = pygame.image.load('assets/background.png')
imagemRodape = pygame.image.load('assets/ground.png')
imagemBlocoSuperior = pygame.image.load('assets/pipe_top.png')
imagemBlocoInferior = pygame.image.load('assets/pipe_bottom.png')

scroll_vel = 1
posicao_inicial_passaro = (100, 250)

class Passaro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagensPassaros[0]
        self.rect = self.image.get_rect()
        self.rect.center = posicao_inicial_passaro
        self.image_index = 0
        self.vel = 0
        self.voando = False

    def update(self, entrada_usuario):
        #animação do pássaro
        self.image_index +=1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = imagensPassaros[self.image_index // 10]

        #gravidade e vôo
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 500:
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.voando = False

        #rotacionar pássaro
        self.image = pygame.transform.rotate(self.image, self.vel * -7)

        #entrada do usuário
        if entrada_usuario[pygame.K_SPACE] and not self.voando and self.rect.y > 0:
            self.voando = True
            self.vel = -7

class Bloco(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        self.rect.x -= scroll_vel
        if self.rect.x <= -LARGURA_JANELA:
            self.kill()

class Rodape(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagemRodape
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        self.rect.x -= scroll_vel
        if self.rect.x <= -LARGURA_JANELA:
            self.kill()


def sair_do_jogo():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():

    passaro = pygame.sprite.GroupSingle()
    passaro.add(Passaro())
    
    x_pos_rodape, y_pos_rodape = 0, 520
    rodape = pygame.sprite.Group()
    rodape.add(Rodape(x_pos_rodape, y_pos_rodape))

    bloco_timer = 0
    blocos = pygame.sprite.Group()

    deve_continuar = True

    while deve_continuar:
        sair_do_jogo()

        #reseta o frame
        janela.fill((0, 0, 0))

        #entrada do usuário
        entrada_usuario = pygame.key.get_pressed()

        #desenha o fundo
        janela.blit(imagemFundo, (0, 0))

        #respawna o rodapé
        if len(rodape) <= 2:
            rodape.add(Rodape(LARGURA_JANELA, y_pos_rodape))

        #desenha o rodapé, pássaro e os blocos
        blocos.draw(janela)
        rodape.draw(janela)
        passaro.draw(janela)

        #atualiza o rodapé, pássaro e os blocos
        blocos.update()
        rodape.update()
        passaro.update(entrada_usuario)
        
        #respawnar blocos
        if bloco_timer <= 0:
            x_cima, x_baixo = 550, 550
            y_cima = random.randint(-600, -480)
            y_baixo = y_cima + random.randint(90, 130) + imagemBlocoInferior.get_height()
            blocos.add(Bloco(x_cima, y_cima, imagemBlocoSuperior))
            blocos.add(Bloco(x_baixo, y_baixo, imagemBlocoInferior))
            bloco_timer = random.randint(180, 250)
        bloco_timer -= 1


        relogio.tick(60)
        pygame.display.update()

main()