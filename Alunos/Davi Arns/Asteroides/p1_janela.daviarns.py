import pygame

#definindo cores - CONSTANTES
#tuplas - ficam entre parênteses
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#definindo constante tipo int
PI = 3.1416 

#Inicializando os módulos do pygame
pygame.init() 

#Criando uma janela
janela = pygame.display.set_mode((700, 400))
pygame.display.set_caption('Preenchendo figuras e textos')

janela.fill(BRANCO)
#define o tamanho do texto
fonte = pygame.font.Font(None, 48)

texto = fonte.render('Primeiro jogo cyber dev', True, BRANCO, VERMELHO)
janela.blit(texto, [120, 75])

#desenvolvimento as figuras
pygame.draw.line(janela, PRETO, (50, 100), (420, 260), 4)
pygame.draw.polygon(janela, PRETO, ((191, 206), (236, 277), (156, 277)), 0)
pygame.draw.circle(janela, VERDE, (130, 300), 30, 0)
pygame.draw.ellipse(janela, AZUL, (400, 250, 40, 80), 0)
pygame.draw.rect(janela, AZUL, (20, 20, 60, 40,), 0)
pygame.draw.arc(janela, PRETO, [250, 75, 150, 125], PI/2, 3*PI/2, 2)
pygame.draw.arc(janela, PRETO, [250, 75, 150, 125], -PI/2, PI/2, 2)

#atualiza a exibição
pygame.display.update()

deve_continuar = True

#Loop do jogo
while deve_continuar:
    #Checando eventos
    for event in pygame.event.get():
        #Se for um evento QUIT 
        if event.type == pygame.QUIT:
            deve_continuar = False 

#Encerrando módulos de pygame 
pygame.quit()