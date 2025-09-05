import pygame, random   
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)
LARGURA_JANELA = 600
ALTURA_JANELA = 600
VEL = 6
ITERACOES = 30
TAMANHOBLOCO = 20

def moverjogador(jogador, teclas, dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]
    if teclas['esquerda'] and jogador['ObjRect'].left > borda_esquerda:
        jogador['ObjRect'].x -= jogador['vel']
    if teclas['direita'] and jogador['ObjRect'].right < borda_direita:
        jogador['ObjRect'].x += jogador['vel']
    if teclas['cima'] and jogador['ObjRect'].top > borda_superior:
        jogador['ObjRect'].y -= jogador['vel']
    if teclas['baixo'] and jogador['ObjRect'].bottom < borda_inferior:
        jogador['ObjRect'].y += jogador['vel']

def moverBloco(bloco):
    bloco['ObjRect'].y += bloco['vel']

pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption('Teclado e mouse')

jogador = {
    'ObjRect': pygame.Rect(300, 100, 50, 50),
    'cor': VERDE,
    'vel': VEL 
}
teclas = {
    'esquerda': False,
    'direita': False,
    'cima': False,
    'baixo': False
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
            if evento.key == pygame.K_DOWN or evento.type == pygame.K_s:
                teclas['baixo'] = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas['esquerda'] = False
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas['direita'] = False
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas['cima'] = False
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas['baixo'] = False          
        if evento.type == pygame.MOUSEBUTTONDOWN:
            blocos.append({
                'ObjRect': pygame.Rect(evento.pos[0], evento.pos[1], TAMANHOBLOCO, TAMANHOBLOCO),
                'cor': BRANCO,
                'vel': 1
            })


    contador += 1
    if contador >= ITERACOES:
        contador = 0
        posX = random.randint(1, LARGURA_JANELA - TAMANHOBLOCO)
        posY = -TAMANHOBLOCO
        velRandom = random.randint(1, VEL-3)
        blocos.append({
            'ObjRect': pygame.Rect(posX, posY, TAMANHOBLOCO, TAMANHOBLOCO),
            'cor': BRANCO,
            'vel': velRandom


        }) 

    janela.fill(PRETO)
    moverjogador(jogador, teclas, (LARGURA_JANELA, ALTURA_JANELA))

    pygame.draw.rect(janela, jogador['cor'], jogador['ObjRect'])
    for bloco in blocos[:]:
        bateu = jogador['ObjRect'].colliderect(bloco['ObjRect'])
        if bateu or bloco['ObjRect'].y > ALTURA_JANELA:
            blocos.remove(bloco)
    for bloco in blocos:
        moverBloco(bloco)
        pygame.draw.rect(janela, bloco['cor'], bloco['ObjRect'])

    pygame.display.update()
    relogio.tick(100000000000000000000000000000000000000000000000000000000000000000000000)

pygame.quit()
