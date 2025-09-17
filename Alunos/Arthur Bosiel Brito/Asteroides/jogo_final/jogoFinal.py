import pygame, random

imagemNave = pygame.image.load('nave.png')
imagemRaio = pygame.image.load('tiro.png')
imagemAsteroide = pygame.image.load('asteroides.png')
imagemFundo = pygame.image.load('fundo.png')
LARGURAJANELA = 1000
ALTURAJANELA = 600
COR_TEXTO = (255,255,255)
FPS = 40
TAM_MINIMO = 60
TAM_MAXIMO = 90
VEL_MINIMA = 1
VEL_MAXIMA = 8
VEL_JOGADOR = 5
VEL_RAIO = (0, -20)
ITERACOES = 20
LARGUARA_NAVE = imagemNave.get_width()
ALTURA_NAVE = imagemNave.get_width()
LARGURA_RAIO = imagemRaio.get_width()
ALTURA_RAIO = imagemRaio.get_height()

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

def moverElemento(elemento):
    elemento['objRect'].x += elemento['vel'][0]
    elemento['objRect'].y += elemento['vel'][1]

def terminar():
    pygame.quit()
    exit()

def aguardarEntrada():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    terminar()
                return
            
def colocarTexto(texto, fonte, janela, x, y):
    objTexto = fonte.render(texto, True, COR_TEXTO)
    rectTexto = objTexto.get_rect()
    rectTexto.topleft = (x, y)
    janela.blit(objTexto, rectTexto)

pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption('Asteroides')
pygame.mouse.set_visible(False) #elimina o cursor do mouse

imagemFundoRedim = pygame.transform.scale(imagemFundo, (LARGURAJANELA, ALTURAJANELA))

#configura a fonte
fonte = pygame.font.Font(None, 48)

somFinal = pygame.mixer.Sound('somgameover.mp3')
somRecorde = pygame.mixer.Sound('somrecord.mp3')
somTiro = pygame.mixer.Sound('somtiro.mp3')
pygame.mixer.music.load('somfundo.mp3')
colocarTexto('Asteroides', fonte, janela, LARGURAJANELA/5, ALTURAJANELA/3)

colocarTexto('Pressione uma tecla para começar', fonte, janela, LARGURAJANELA/20, ALTURAJANELA/2)

pygame.display.update()
aguardarEntrada()
recorde = 0

#segunda etapa
while True:
    asteroides = []
    raios = []
    pontuacao = 0
    deve_continuar = True
    teclas = {
        'esquerda': False,
        'direita': False,
        'cima': False,
        'baixo': False
    }
    contador = 0
    pygame.mixer.music.play(-1, 0, 0)
    posX = LARGURAJANELA/2
    posY = ALTURAJANELA - 50
    jogador = {
        'objRect': pygame.Rect(posX, posY, LARGUARA_NAVE, ALTURA_NAVE),
        'imagem': imagemNave, 
        'vel': VEL_JOGADOR
    }

    #terceira etapa
    while deve_continuar:
        pontuacao += 1
        if pontuacao == recorde:
            somRecorde.play()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    deve_continuar == False
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    teclas['esquerda'] = True
                if evento.key == pygame.K_RIGHT or evento.type == pygame.K_d:
                    teclas['esquerda'] = True
                if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                    teclas['cima'] = True
                if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                    teclas['baixo'] = True
                if evento.key == pygame.K_ESCAPE:
                    raio = {
                        'objRect': pygame.Rect(jogador['objRect'].centerx, jogador['objRect'].top, LARGURA_RAIO, ALTURA_RAIO),
                        'imagem': imagemRaio,
                        'vel': VEL_RAIO
                    }
                    raios.append(raio)
                    somTiro.play()
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    teclas['esquerda'] = False
                if evento.key == pygame.K_RIGHT or evento.type == pygame.K_d:
                    teclas['esquerda'] = False
                if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                    teclas['cima'] = False
                if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                    teclas['baixo'] = False
            if evento.type == pygame.MOUSEMOTION:
                centroX_jogador = jogador['objRect'].centerx
                centroY_jogador = jogador['objRect'].centery
                jogador['objRect'].move_ip(evento.pos[0] - centroX_jogador, evento.pos[1] - centroY_jogador)
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                raio = {
                    'objRect': pygame.Rect(jogador['objRect'].centerx, jogador['objRect'].top, LARGURA_RAIO, ALTURA_RAIO),
                    'imagem': imagemRaio,
                    'vel': VEL_RAIO
                }
                raios.append(raio)
                somTiro.play()

        janela.blit(imagemFundoRedim, (0, 0))
        colocarTexto(f'Pontuação: {str(pontuacao)}', fonte, janela, 10, 2)
        colocarTexto(f'Recorde: {str(recorde)}', fonte, janela, 10, 40)
        contador+=1

        if contador == ITERACOES:
            contador = 0
            tamAsteroide = random.randint(TAM_MINIMO, TAM_MAXIMO)
            posX = random.randint(0, LARGURAJANELA - tamAsteroide)
            posY = -tamAsteroide
            velX = random.randint(-1, 1)
            velY = random.randint(VEL_MINIMA, VEL_MAXIMA)
            imagem_redimensioada = pygame.transform.scale(imagemAsteroide, (tamAsteroide, tamAsteroide))
            asteroide_rect = pygame.Rect(posX, posY, tamAsteroide, tamAsteroide)
            
            asteroide = {
                'objRect': asteroide_rect,
                'imagem': imagem_redimensioada,
                'vel': (velX, velY)
            }
            asteroides.append(asteroide)

        for asteroide in asteroides:
            moverElemento(asteroide)
            janela.blit(asteroide['imagem'], asteroide['objRect'])

        for asteroide in asteroides[:]:
            topo_asteroide = asteroide['objRect'].top 
            if topo_asteroide > ALTURAJANELA:
                asteroides.remove(asteroide)
            
        for raio in raios:
            moverElemento(raio)
            janela.blit(raio['imagem'], raio['objRect'])
        
        for raio in raios[:]:
            base_raio = raio['objRect'].bottom
            if base_raio < 0:
                raios.remove(raio)

        #processa a moimentação do jogador
        moverJogador(jogador, teclas, (LARGURAJANELA, ALTURAJANELA))

        #exibe o jogador na tela
        janela.blit(jogador['imagem'], jogador['objRect'])

        for asteroide in asteroides[:]:
            jogadorColidiu = jogador['objRect'].colliderect(asteroide['objRect'])
            if jogadorColidiu:
                if pontuacao > recorde:
                    recorde = pontuacao
                deve_continuar = False
            for raio in raios [:]:
                raioColidiu = raio['objRect'].colliderect(asteroide['objRect'])
                if raioColidiu:
                    if raio in raios:
                        raios.remove(raio)
                    if asteroide in asteroides:
                        asteroides.remove(asteroide)
                    break

        pygame.display.update() #atualizar a janela
        relogio.tick(FPS)

    pygame.mixer.music.stop()
    somFinal.play()
    colocarTexto('GAME OVER', fonte, janela, (LARGURAJANELA/3), (ALTURAJANELA/2))
    colocarTexto('Pressione uma tecla para jogar novamente', fonte, janela, (LARGURAJANELA/10), (ALTURAJANELA/2))
    pygame.display.update()
    aguardarEntrada()
    somFinal.stop()