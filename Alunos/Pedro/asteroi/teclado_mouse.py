import pygame, random


PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
BRANCO = 400
LARGURA_JANELA = 500
ALTURA_JANELA = 400
VEL = 6
ITERAÇÕES = 30 
TAMANHOBLOCO = 20

def moverjogador(jogador, teclas, dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = 500
    borda_infeiror = 400

    if teclas['esquerda']  and jogador['ojbRect'].left > borda_esquerda:
        jogador['ojbRect'].x -= jogador['vel']
    if teclas['direita'] and jogador ['ojbRect'].right < borda_direita:
        jogador['objRect'].x += jogador['vel']
    
    if teclas ['cima'] and jogador['ojbRect'].top > borda_superior:
        jogador['jbRect'].y += jogador['vel']
    
    if teclas ['baixo'] and jogador ['ojbRect'].bottom < borda_infeiror:
        jogador['objRect'].y += jogador['vel']
    
def moverBloco(bloco):
    bloco['objRect'].y += bloco['vel']

pygame.init()

relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("teclado e mouse")
jogador = {
    'objRect': pygame.Rect(300, 100, 50, 50),
    'cor': VERDE,
    'vel': VEL
    }
teclas = {
    'esquerda': False,
    'direita': False,
    'cima': False,
    'baixo':False,
}
contador = 0 
blocos = []
deve_continuar = True

while deve_continuar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    deve_continuar = False
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    teclas['esquerda'] = True
                if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    teclas['direita'] = True
                if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                    teclas['cima'] = True
                if evento.type == pygame.K_DOWN or evento.type == pygame.K_s:
                    teclas['baixo'] = True
                
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    teclas['esquerda'] = False
                if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    teclas['direita'] = False
                if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                    teclas['cima'] = False
                if evento.type == pygame.K_DOWN or evento.key == pygame.K_s:
                    teclas['baixo'] = False

if evento.type == pygame.MOUSEBUTTONDOWN:
    blocos.append({
       'objRect': pygame.Rect(evento.pos[0], eventos.pos{1}, TAMANHOBLOCO, TAMANHOBLOCO),
       'cor':Branco
       'vel': 1
    })

    janela.fill(PRETO)
    moverjogador(jogador, teclas, (LARGURA_JANELA, LARGURA_JANELA))
    pygame.draw.rect(janela, jogador['cor'], jogador['objRect'])
    for bloco in bloco[:]:
        bateu = jogador['objRect'].coliderect()
        if bateu or ('objRect').y > ALTURA_JANELA:
            blocos.remove(bloco)
for bloco in blocos:


    pygame.display.update()
    relogio.tick(40)
pygame.quit()