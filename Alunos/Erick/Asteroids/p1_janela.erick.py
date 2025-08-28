import pygame

BRANCO = (255,255,255)
PRETO = (0,0,0) 
VERMELHO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

PI = 3.1416

pygame.init()

janela = pygame.display.set_mode((500,400))
pygame.display.set_caption("Preenchimeto figuras de texto")

janela.fill(BRANCO)

fonte = pygame.font.Font(None,48)

texto = fonte.render("Primeiro jogo Cyber dev,", BRANCO, PRETO)
janela.blit(texto, [0, 0])

pygame.draw.line(janela,PRETO, (50, 100), (420, 260), 4)
pygame.display.update()

deve_continuar = True



while deve_continuar:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            deve_continuar = False
pygame.quit() 

pygame.