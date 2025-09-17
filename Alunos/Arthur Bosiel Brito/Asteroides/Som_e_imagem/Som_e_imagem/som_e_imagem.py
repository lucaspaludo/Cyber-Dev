import pygame, random
imagemPassaro = pygame.image.load('personagem.png')
imagemMosquito = pygame.image.load('alvo.png')
imagemFundo = pygame.image.load('fundo.png')
LARGURA_JANELA = imagemFundo.get_width()
ALTURA_JANELA  = imagemFundo.get_height()
LARGURA_PASSARO = imagemPassaro.get_width()
ALTURA_PASSARO = imagemPassaro.get_height()
LARGURA_MOSQUITO = imagemMosquito.get_width()
ALTURA_MOSQUITO = imagemMosquito.get_height()

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

def moverMosquito(mosquito):
    mosquito['objRect'].x += mosquito['vel']

pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption('Imagem e som')
# dicionário
jogador = {
    'objRect': pygame.Rect(300, 100, LARGURA_PASSARO, ALTURA_PASSARO),
    'imagem': imagemPassaro,
    'vel': VEL
}

# configurando o som
somComer = pygame.mixer.Sound('comer.mp3')
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play(-1, 0.0)
somAtivado = True
teclas = {
    'esquerda': False,
    'direita': False,
    'cima':False,
    'baixo': False
}
contador = 0
mosquitos = []
deve_continuar = True

while deve_continuar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False
        if  evento.type == pygame.KEYDOWN:
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
                    somAtivado = True
        
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
            mosquitos.append({
                'objRect': pygame.Rect(evento.pos[0], evento.top[1], LARGURA_MOSQUITO, ALTURA_MOSQUITO),
                'imagem': imagemMosquito,
                'vel': VEL - 3
            })

    contador += 1
    if contador >= ITERACOES:
        contador = 0
        posY = random.randint(0, ALTURA_JANELA - ALTURA_MOSQUITO)
        posX = -LARGURA_MOSQUITO
        velRandom = random.randint(VEL - 3, VEL + 3)
        mosquitos.append({
            'objRect': pygame.Rect(posX, posY, LARGURA_MOSQUITO, ALTURA_MOSQUITO),
            'imagem': imagemMosquito,
            'vel': velRandom
        })

    janela.blit(imagemFundo, (0,0))
    moverJogador(jogador, teclas, (LARGURA_JANELA, ALTURA_JANELA))
    janela.blit(jogador['imagem'], jogador['objRect'])

    for mosquito in mosquitos[:]:
        comeu = jogador['objRect'].colliderect(mosquito['objRect'])
        if comeu and somAtivado:
            somComer.play()
        if comeu or mosquito['objRect'].x > LARGURA_JANELA:
            mosquitos.remove(mosquito)

    for mosquito in mosquitos:
        moverMosquito(mosquito)
        janela.blit(mosquito['imagem'], mosquito['objRect'])



    pygame.display.update()
    relogio.tick(40)
pygame.quit
