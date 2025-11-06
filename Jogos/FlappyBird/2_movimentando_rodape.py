import pygame
from sys import exit

LARGURA_JANELA = 551
ALTURA_JANELA = 720


imagem_fundo = pygame.image.load('assets/background.png')
imagem_rodape = pygame.image.load('assets/ground.png')
scroll_vel = 1

pygame.init()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA)) 
pygame.display.set_caption("Flappy Bird")
relogio = pygame.time.Clock()

class Rodape(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem_rodape
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

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
    x_pos_rodape, y_pos_rodape = 0, 520
    rodape = pygame.sprite.Group()
    rodape.add(Rodape(x_pos_rodape, y_pos_rodape))
    deve_continuar = True
    while deve_continuar:
        sair_do_jogo()
        janela.fill((0, 0, 0))
        #desenha fundo
        janela.blit(imagem_fundo, (0, 0))

        #respawna o rodapé
        if len(rodape) <= 2:
            rodape.add(Rodape(LARGURA_JANELA, y_pos_rodape)) 

        #desenha rodaapé
        rodape.draw(janela)
        #atualiza o rodapé
        rodape.update()
        relogio.tick(60)
        pygame.display.update()

main()


    