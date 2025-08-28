import pygame

#definindo cores
PRETO = (0,0,0)
BRANCO= (255,255,255)
VERMELHO= (255,0,0)
VERDE=(0,255,0)
AZUL= (0,0,255)
AMARELO = (255, 255, 0)
ROXO = (255, 0, 255)

#definindo constante tipo int
PI= 3.1416

#inicializando os módulos do pygame
pygame.init()

janela=pygame.display.set_mode((500,400))
pygame.display.set_caption('Figuras e texto!')




janela.fill(BRANCO)
#define a fonte
fonte= pygame.font.Font(None, 48)
texto = fonte.render('Primeiro jogo cyber dev ', True, BRANCO, AZUL)

#define a posição
janela.blit(texto,[0, 0])
pygame.draw.line(janela, VERDE, (60, 260), (420, 260), 4)
pygame.draw.polygon(janela,PRETO,((191, 206), (236, 277), (156,277)),0)
pygame. draw.circle(janela,AZUL,(300, 50), 20,0)
pygame.draw.ellipse(janela,VERMELHO,(400, 250, 40, 80), 1)
pygame.draw.rect(janela,ROXO,(20, 20, 60, 40), 0)
pygame.draw.arc(janela,VERMELHO, [250, 75, 150, 125], PI/2,3*PI/2,2)
pygame.draw.arc(janela,AMARELO, [250, 75, 150, 125], -PI/2, PI/2,2)
pygame.display.update()

deve_continuar=True

# criando um loop infinito
while deve_continuar:
    #checando eventos
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            deve_continuar= False
pygame.quit()