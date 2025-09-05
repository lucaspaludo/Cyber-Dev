import pygame, time

PRETO = (0, 0, 0,)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
LARGURA_JANELA = 500
ALTURA_JANELA = 400
def mover(figura,dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]
  
  if figura['objRect'].top < borda_superior or figura

f1 = {
    'objRect' : pygame.Rect(300, 80, 40, 80),
    'cor': VERDE,
    'vel': [0,-5],
    'forma': 'ELIPSE'
}

figuras = [f1]

pygame.init()
janela = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA))

pygame.display.set_caption('Animação')
deve_continuar = True
while deve_continuar:
    for luiz in pygame.event.get():
        if luiz.type ==pygame.QUIT:
            deve_continuar = False
    janela.fill(PRETO)
    for figura in figuras:
        if figura['forma'] == 'ELIPSE':
            pygame.draw.ellipse(janela, figura['cor'],figura['objRect'])

    pygame.display.update()

pygame.quit()   