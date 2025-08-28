import pygame

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

PI = 3.1416

    #inicializando os modulos do pygame
pygame.init()

janela = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Olá, mundo!')

deve_continuar = True

while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
               deve_continuar = False

pygame.quit()