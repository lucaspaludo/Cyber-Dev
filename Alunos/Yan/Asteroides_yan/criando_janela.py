import pygame

#inicializa os módulos do pygame
pygame.init()

#criando uma janela com o título 'Olá, mundo!'
janela = pygame.display.set_mode((900, 500))
pygame.display.set_caption('Olá, mundo!')

deve_continuar = True

#loop do jogo
while deve_continuar:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            deve_continuar = False

#Encerrando os módulos do Pygame
pygame.quit()



