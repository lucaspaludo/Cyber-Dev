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

#inicializando os módulos do pygame
pygame.init()

#criando uma janela com o título "Olá, mundo!"
janela = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Figuras e textos')

#define o fundo da janela
janela.fill(BRANCO)

#define o tamanho da fonte
fonte = pygame.font.Font(None, 48)

#define o texto que será exibido, sua cor e a cor de fundo
texto = fonte.render('Primeiro jogo cyber dev', True, PRETO, BRANCO)

#define a posição do texto
janela.blit(texto, [0, 0])

#desenvolvendo as figuras
pygame.draw.line(janela, PRETO, (50, 100), (420, 260), 4)
pygame.draw.polygon(janela, PRETO, ((191, 206), (236, 277), (156, 277)), 0)
pygame.draw.circle(janela, PRETO, (300, 50), 20, 0)
pygame.draw.ellipse(janela, PRETO, (400, 250, 40, 80), 0)
pygame.draw.rect(janela, PRETO, (20, 20, 60, 40), 0)
pygame.draw.arc(janela, PRETO, [250, 75, 150, 125], PI/2, 3*PI/2, 2)
pygame.draw.arc(janela, PRETO, [250, 75, 150, 125], -PI/2, PI/2, 2)

#atualiza a exibição
pygame.display.update()

deve_continuar = True


#criando um loop infinito
while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False
pygame.quit() 




