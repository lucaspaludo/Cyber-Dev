import pygame

#definit cores
#tuplas - ficam entre parenteses
PRETO =  (0, 0 ,0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#definindo uma variavel tipo int
PI = 3.1416

#inicializando os módulos do pygame
pygame.init()

#criando uma janela com o título 'Olá mundo!'
janela = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Preendo figuras e textos')

#define a cor de fundo da janela
janela.fill(BRANCO)

#define o tamanho do texto
fonte = pygame.font.Font(None, 48)

#define o texto que vai ser exibido e a cor da fonte e a cor de fundo
texto = fonte.render('Primeiro jogo Cyber-Dev', True, BRANCO, AZUL)

#define onde o texto vai ser exibido
janela.blit(texto, [0, 0])

#desenvolvendo as figuras
pygame.draw.line(janela, PRETO, (50,100), (420,260), 4)
pygame.draw.polygon(janela, VERMELHO, ((191, 206), (236, 277), (156, 277)), 0)
pygame.draw.circle(janela, VERMELHO, (300,70), 20, 0)
pygame.draw.ellipse(janela, VERDE, (400, 250, 40, 80), 2)
pygame.draw.rect(janela, VERDE, (20, 20, 60, 40), 0)
pygame.draw.arc(janela, PRETO, [250, 75, 150, 125], PI/2, 3*PI/2, 2)
pygame.draw.arc(janela, PRETO, [250, 75, 150, 125], -PI/2, PI/2)

pygame.display.update()

deve_continuar = True

#criando um loop infinito
while deve_continuar:
    for event in  pygame.event.get():
        if  event.type == pygame.QUIT:
            deve_continuar = False
pygame.quit()