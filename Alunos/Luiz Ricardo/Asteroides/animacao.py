import pygame, time

PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)

LARGURA_JANELA = 500
ALTURA_JANELA = 500

def mover(figura, dim_janela):    
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]

    if figura['objRect'].top < borda_superior or figura['objRect'].bottom > borda_inferior:
        figura['vel'][1] = -figura['vel'][1]
    if figura['objRect'].left < borda_esquerda or figura['objRect'].right > borda_direita:
        figura['vel'][0] = -figura['vel'][0]

    figura['objRect'].x += figura['vel'][0]
    figura['objRect'].y += figura['vel'][1]

f1 = {
    'objRect': pygame.Rect(300, 80, 40, 80),
    'cor': VERDE,
    'vel': [0, -5],
    'forma': 'ELIPSE'
}

f2 = {
    'objRect': pygame.Rect(200, 200, 20, 20),
    'cor': AZUL,
    'vel': [8, -5],
    'forma': 'ELIPSE'
}

f3 = {
    'objRect': pygame.Rect(100, 150, 60, 60),
    'cor': VERMELHO,
    'vel': [-5, 0],
    'forma': 'RETANGULO'
}

f4 = {
    'objRect': pygame.Rect(200, 150, 80, 80),
    'cor': BRANCO,
    'vel': [-1, 9],
    'forma': 'RETANGULO'
}

f5 = {
    'objRect': pygame.Rect(100, 150, 60, 60),
    'cor': VERDE,
    'vel': [-5, 9],
    'forma': 'RETANGULO'
}

f6 = {
    'objRect': pygame.Rect(100, 50, 40, 60),
    'cor': VERMELHO,
    'vel': [-8, 5],
    'forma': 'RETANGULO'
}

f7 = {
    'objRect': pygame.Rect(200, 190, 80, 80),
    'cor': BRANCO,
    'vel': [-2, 5],
    'forma': 'RETANGULO'
}

f8 = {
    'objRect': pygame.Rect(200, 150, 50, 90),
    'cor': BRANCO,
    'vel': [-5, 6],
    'forma': 'RETANGULO'
}

f9 = {
    'objRect': pygame.Rect(200, 70, 90, 80),
    'cor': VERDE,
    'vel': [2, -5],
    'forma': 'ELIPSE'
}

f10 = {
    'objRect': pygame.Rect(500, 38, 46, 80),
    'cor': AZUL,
    'vel': [0, -4],
    'forma': 'ELIPSE'
}


figuras = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]

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
        elif figura['forma'] == 'RETANGULO':
            pygame.draw.rect(janela, figura['cor'], figura['objRect'])

    pygame.display.update()
    time.sleep(0.09)

pygame.quit()








































































































































































































































































































































































































































































































































































































































































