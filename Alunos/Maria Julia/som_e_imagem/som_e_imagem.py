import pygame, random

imagemBorboleta = pygame.image.load('borboleta.png')
imagemFlor = pygame.image.load('flor.png')
imagemFundo = pygame.image.load('florestaPNGcyberdev.png')

LARGURA_JANELA = imagemFundo.get_width()
ALTURA_JANELA = imagemFundo.get_height()
LARGURA_BORBOLETA = imagemBorboleta.get_width()
ALTURA_BORBOLETA = imagemBorboleta.get_height()
LARGURA_FLOR = imagemFlor.get_width()
ALTURA_FLOR = imagemFlor.get_height()
VEL = 6
ITERACOES = 30

def moverJogador(jogador, teclas, dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]
    if teclas['esquerda'] and jogador['objRect'].left > borda_esquerda:
        jogador['objRect'].x -= jogador['vel']
    if teclas['direita'] and jogador['objRect'].right < borda_direita:
        jogador['objRect'].x += jogador['vel']
    if teclas['cima'] and jogador['objRect'].top > borda_superior:
        jogador['objRect'].y -= jogador['vel']
    if teclas['baixo'] and jogador['objRect'].bottom < borda_inferior:
        jogador['objRect'].y += jogador['vel']

def moverFlor(flor):
    flor['objRect'].x += flor['vel']

pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption('Imagem e Som')
jogador = {
    'objRect': pygame.Rect(300, 100, LARGURA_BORBOLETA, ALTURA_BORBOLETA),
    'imagem': imagemBorboleta,
    'vel': VEL
}
# print(LARGURA_JANELA)
# print(LARGURA_FLOR)
# print(LARGURA_BORBOLETA)
somComer = pygame.mixer.Sound('comer.mp3')
pygame.mixer.music.load('fundo.mp3')
pygame.mixer.music.play(-1, 0.0)
somAtivado = True
teclas = {
    'esquerda': False,
    'direita': False,
    'cima': False,
    'baixo': False
}
contador = 0
flores = []
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
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas['baixo'] = True
            if evento.key == pygame.K_m:
                if somAtivado:
                    pygame.mixer.music.stop()
                    somAtivado = False
                else:
                    pygame.mixer.music.play(-1, 0.0)
                    somAtivado= True
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
            flores.append({
                'objRect': pygame.Rect(evento.pos[0], evento.pos[1], LARGURA_FLOR, ALTURA_FLOR),
                'imagem': imagemFlor,
                'vel': VEL -3
            })
            #print(flores)
    contador += 1
    if contador >= ITERACOES:
        contador = 0
        posY = random.randint(0, ALTURA_JANELA - ALTURA_FLOR)
        posX = -LARGURA_FLOR
        velRandom = random.randint(VEL -3, VEL+3)
        flores.append({
            'objRect': pygame.Rect(posX, posY, LARGURA_FLOR, ALTURA_FLOR),
            'imagem': imagemFlor,
            'vel': velRandom
        })
        #print(flores)
    janela.blit(imagemFundo, (0,0))
    moverJogador(jogador, teclas, (LARGURA_JANELA, ALTURA_JANELA))
    janela.blit(jogador['imagem'], jogador['objRect'])
    for flor in flores[:]:
        comeu = jogador['objRect'].colliderect(flor['objRect'])
        if comeu and somAtivado:
            somComer.play()
        if comeu or flor['objRect'].x > LARGURA_JANELA:
            flores.remove(flor)

    for flor in flores:
        moverFlor(flor)
        janela.blit(flor['imagem'], flor['objRect'])
    
    pygame.display.update()
    relogio.tick(40)

pygame.quit()