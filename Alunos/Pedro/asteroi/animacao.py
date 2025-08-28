import pygame, time
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
LARGURA_JANELA = 500
ALTURA_JANELA = 400
def mover():
    pass

f1 = {
    'object' : pygame.Rect(300, 80, 40, 80),
    'cor' : VERDE,
    'vel' : [0, -5],
    'forma' : 'ELIPSE'
}

figuras = [f1]

pygame.init()
janela = pygame.display.set_caption('Animação')
deve_continuar = True
while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            deve_continuar = False
janela.fill(PRETO)
for figura in figuras:
    mover(janela, (LARGURA_JANELA, ALTURA_JANELA))
    
if figura['forma'] == 'ELIPSE':
    pygame.draw.ellipse(janela,figura('cor'), figura('objRect'))

pygame.display.update()
 
pygame.quit()