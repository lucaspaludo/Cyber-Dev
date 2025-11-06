import pygame
from sys import exit

LARGURA_JANELA = 551
ALTURA_JANELA = 720

imagem_fundo = pygame.image.load('assets/background.png')


pygame.init()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA)) 
pygame.display.set_caption("Flappy Bird")
relogio = pygame.time.Clock()

def sair_do_jogo():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():

    deve_continuar = True
    while deve_continuar:
        sair_do_jogo()
        janela.fill((0, 0, 0))
        #desenha fundo
        janela.blit(imagem_fundo, (0, 0))


        relogio.tick(60)
        pygame.display.update()

main()


    