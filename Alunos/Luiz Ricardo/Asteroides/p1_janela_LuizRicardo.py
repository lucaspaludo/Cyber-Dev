import pygame

#definir cores
#tuplas - ficam entre parênteses 
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
MARROM = (255, 90, 50)
LARANJA = (255, 120, 50)
AMARELO = (255, 255, 0)

#definindo constante tipo int 
PI = 3.1416

#inicializando modulos de pygame
pygame.init()

#criando uma janela com o titulo 'olá, mundo'
janela = pygame.display.set_mode((500,500))
pygame.display.set_caption('preenchendo figuras e textos')

janela.fill(BRANCO)
fonte = pygame.font.Font(None,48)
texto = fonte.render('primeiro jogo cyber dev', True, BRANCO, AZUL)
#define a posicao do texto 
janela.blit(texto, (30, 150))
#desenvolvimento de figuras
pygame.draw.line(janela, AZUL, (60, 260,), (420, 260), 39)
pygame.draw.polygon(janela, VERDE, ((191, 206), (236, 277), (156, 277)), 0)
pygame.draw.circle(janela, LARANJA, (300, 50), 20, 0)
pygame.draw.ellipse(janela, AMARELO, (400, 250, 40, 80), 5)
pygame.draw.rect(janela, VERMELHO, (20, 20, 60, 40,), 0)
pygame.draw.arc(janela, AZUL, [250, 75, 150, 125], PI/2,3*PI/2,2)
pygame.draw.arc(janela, VERMELHO, [250, 75, 150, 125], -PI/2,PI/2,2)


pygame.display.update()



deve_continuar = True 

#criando um loop infinito
while deve_continuar:
    for event in pygame .event.get():
        if event .type == pygame.QUIT:
            deve_continuar = False
pygame.quit()