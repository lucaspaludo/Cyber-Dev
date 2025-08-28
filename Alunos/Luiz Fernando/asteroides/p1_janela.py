import pygame

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

PI = 3.1416

#inicializando os módulos do pygame
pygame.init()

janela = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Figuras e textos')

janela.fill(BRANCO)
fonte = pygame.font.Font(None, 56)
texto = fonte.render('primeiro jogo cyber dev', True, PRETO, VERMELHO)
janela.blit(texto, [0, 0])

pygame.draw.line(janela, PRETO, (50,100), (420,260), 4)
pygame.draw.polygon(janela, PRETO, ((191, 206), (236,277), (156, 277)), 8)
pygame.draw.circle(janela, PRETO, (300, 50), 20, 0)
pygame.draw.ellipse(janela, PRETO, (400, 250, 40, 80),0)
pygame.draw.rect(janela, PRETO, (20, 20, 60, 40), 0)
pygame.draw.arc(janela, PRETO, [250,75, 150, 125], PI/2, 3*PI/2,2)
pygame.draw.arc(janela, PRETO, [250,75, 150, 125], -PI/2, PI/2,2)
pygame.display.update()

deve_continuar = True

#criando um loop infinito
while deve_continuar:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        deve_continuar = False
pygame.quit()