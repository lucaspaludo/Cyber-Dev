import pygame, time

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
LARGURA_JANELA = 500
ALTURA_JANELA = 400

def mover(figura, dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior =dim_janela[1]

    if figura['objRect'].top < 0 or figura['objRect'].bottom > borda_inferior:
        figura['vel'][1] = -figura['vel'][1]
    if figura['objRect'].left < borda_esquerda or figura['objRect'].right > borda_direita:
        figura['vel'][0] = - figura['vel'][0]

    figura['objRect'].x += figura['vel'][0]
    figura['objRect'].y += figura['vel'][1]


f1 = {
    'objRect': pygame.Rect(300, 80, 60, 60),
    'cor': VERDE,
    'vel':[0, -5],
    'forma': 'ELIPSE',
}

f2 = {
    'objRect': pygame.Rect(125, 20, 60, 60),
    'cor': BRANCO,
    'vel':[5, -5],
    'forma': 'ELIPSE',
}

f3 = {
    'objRect': pygame.Rect(100, 150, 60, 60),
    'cor': AZUL,
    'vel':[-5, -5],
    'forma': 'ELIPSE',
}

f4 = {
    'objRect': pygame.Rect(100, 150, 60, 60),
    'cor': VERMELHO,
    'vel':[5, -5],
    'forma': 'ELIPSE',
}

f5 = {
    'objRect': pygame.Rect(200, 130, 60, 60),
    'cor': VERDE,
    'vel':[0, -5],
    'forma': 'ELIPSE',
}

f6 = {
    'objRect': pygame.Rect(240, 240, 60, 60),
    'cor': BRANCO,
    'vel':[5, -5],
    'forma': 'ELIPSE',
}

f7 = {
    'objRect': pygame.Rect(400, 180, 60, 60),
    'cor': AZUL,
    'vel':[-5, -5],
    'forma': 'ELIPSE',
}

f8 = {
    'objRect': pygame.Rect(350, 160, 60, 60),
    'cor': VERMELHO,
    'vel':[5, -5],
    'forma': 'ELIPSE',
}

figuras = [f1, f2, f3, f4, f5, f6, f7, f8]



pygame.init()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption('Animação')
deve_continuar = True
while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False
    janela.fill(PRETO)
    for figura in figuras:
        mover(figura, (LARGURA_JANELA, ALTURA_JANELA))
        if figura['forma'] == 'ELIPSE':
          pygame.draw.ellipse(janela, figura['cor'], figura['objRect'])
          pygame.draw.ellipse(janela, figura['cor'], figura['objRect'])
          pygame.draw.ellipse(janela, figura['cor'], figura['objRect'])
          pygame.draw.rect(janela, figura['cor'], figura['objRect'])
          pygame.draw.ellipse(janela, figura['cor'], figura['objRect'])
          pygame.draw.ellipse(janela, figura['cor'], figura['objRect'])
          pygame.draw.ellipse(janela, figura['cor'], figura['objRect'])
          pygame.draw.rect(janela, figura['cor'], figura['objRect'])

    pygame.display.update()
    time.sleep(0.02) 

pygame>quit()
