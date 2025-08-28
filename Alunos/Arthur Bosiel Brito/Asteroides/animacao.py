import pygame, time

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

LARGURA_JANELA = 500
ALTURA_JANELA = 400

def mover(figura, dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]

    if figura['objRect'].top < 0 or figura['objRect'].bottom > borda_inferior:
        figura['vel'][1] = -figura['vel'][1]
    if figura['objRect'].left < borda_esquerda or figura['objRect'].right > borda_direita:
        figura['vel'][0] = -figura['vel'][0] 

    figura['objRect'].x += figura['vel'][0]
    figura['objRect'].y += figura['vel'][1]

f1 = {
    'objRect': pygame.Rect(300, 80, 40, 80),
    'cor': VERDE,
    'vel': [0, -5],
    'forma': 'ELIPSE', 
}

f2 = {
    'objRect': pygame.Rect(200, 200, 20, 20),
    'cor': AMARELO,
    'vel': [-5, 0],
    'forma': 'RETANGULO',
}

f3 = {
    'objRect': pygame.Rect(200, 50, 90, 50),
    'cor': AZUL,
    'vel': [5, -9],
    'forma': 'ELIPSE'

}

f4 = {
    'objRect': pygame.Rect(255, 60, 90, 10),
    'cor': VERMELHO,
    'vel': [9, 3],
    'forma': 'RETANGULO'
}

figuras = [f1, f2, f3, f4]

pygame.init

janela = pygame.display.set_mode((LARGURA_JANELA,
ALTURA_JANELA))

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
        elif figura['forma'] == 'RETANGULO':
            pygame.draw.rect(janela, figura['cor'], figura['objRect'])

    pygame.display.update()
    time.sleep(0.02)

pygame.quit