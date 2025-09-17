import pygame,random

imagemNave = pygame.image.load('image.png')
imagemRaio = pygame.image.load('enzo_copiei.png')
imagemAsteroide =pygame.image.load('asteroide1.png')
imagemFundo = pygame.image.load('fundo.png')

LARGURA_JANELA = 1000
ALTURA_JANELA = 600
COR_TEXTO = (255, 255, 255)
FPS = 40
TAM_MINIMO = 60
TAM_MAXIMA = 90
VEL_MINIMA = 1
VEL_MAXIMA = 8
VEL_JOGADOR = 5
VEL_RAIO = (0, 20)
ITERACOES = 20

LARGURA_NAVE = imagemNave.get_width()
ALTURA_NAVE = imagemNave.get_height()

LARGURA_RAIO = imagemRaio.get_height()
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
     elemento['objRect'].y += elemento['vel'][0]


def terminar():
    pygame.quit()
    exit()

def aguardandoEntrada():
    while True:
     for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
                terminar()
        if evento.type == pygame.KEYDOWN:
            if evento.type == pygame.K_ESCAPE:
                terminar()
            return

def colocarTexto(texto, fonte, janela, x, y):
    objTexto = fonte.render(texto, True, COR_TEXTO)
    rectTexto = objTexto.get_rect()
    rectTexto.topleft = (x, y )

    janela.blit(objTexto, rectTexto)
pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption('Asteroides')
pygame.mouse.set_visible(False) #elimina o cursor do mouse 7

imagemFundoRedim = pygame.transform.scale(imagemFundo, (LARGURA_JANELA, ALTURA_JANELA))

fonte = pygame.font.Font(None, 48)

somFinal = pygame.mixer.Sound('game.over.mp3')
somRecorde = pygame.mixer.Sound('recorde.mp3')
somTiro = pygame.mixer.Sound('tiro.mp3')
pygame.mixer.music.load('musicadefundo.mp3')
colocarTexto('Asteroides', fonte, janela, LARGURA_JANELA/5, ALTURA_JANELA/3)
colocarTexto('Pressione uma tecla para começar', fonte, janela, LARGURA_JANELA/20, ALTURA_JANELA/2)


pygame.display.update()
aguardandoEntrada()

recorde = 0
while True:
    asteroides = [] 
    raios = []
    pontuacao = 0
    deve_continuar = True 
    teclas = {
        'esquerda':False,
        'direita':False,
        'cima':False,
        'baixo':False, 
    }
    contador = 0
    pygame.mixer.music.play(-1, 0, 0 )
    posX= LARGURA_JANELA/2
    posY = ALTURA_JANELA - 50
    jogador = {
        'objRect': pygame.Rect(posX, posY, LARGURA_NAVE, ALTURA_JANELA),
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
                if evento.key == -pygame.K_ESCAPE:
                    deve_continuar = False
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    teclas['esquerda'] = True
                if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    teclas['direita'] = True
                if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                    teclas['cima'] = True
                if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                    teclas['baixo'] = True
                if evento.key == pygame.K_SPACE:
                    raio = {
                        'objRect': pygame.Rect(jogador['objRect'].centerx, jogador['objRect'].top, LARGURA_RAIO, ALTURA_RAIO),
                        'vel':VEL_RAIO,
                        'imagem': imagemRaio

                    }
                    raios.append(raio)
                    somTiro.play()
                if evento.type == pygame.KEYUP:
                      if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                          teclas['esquerda'] = True
                if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    teclas['direita'] = True
                if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                    teclas['cima'] = True
                if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                    teclas['baixo'] = False

            if evento.type ==pygame.MOUSEBUTTONDOWN:
                    centroX_jogador = jogador['objRect'].centerx
                    centroY_jogador = jogador['objRect'].centery
                    jogador['objRect'].move_ip(evento.pos(0)-centroX_jogador, evento.pos(1)- centroY_jogador)

            if evento.type == pygame.MOUSEBUTTONDOWN:
                    raio = {
                        'objRect': pygame.Rect(jogador['objRect'].centerx, jogador['objRect'].top, LARGURA_RAIO, ALTURA_RAIO),
                        'vel': VEL_RAIO,
                        'imagem': imagemRaio
                     }



        janela.blit(imagemFundoRedim, (0, 0))
        colocarTexto(f'Pontuacao: {str(pontuacao)}', fonte, janela, 10, 0)
        colocarTexto(f'recorde:{str(recorde)}', fonte, janela, 10, 40)
        contador+=1

        if contador == ITERACOES:
            contador = 0
            tamAsteroide = random.randint(TAM_MINIMO, TAM_MAXIMA)
            posX = random.randint(0, LARGURA_JANELA - tamAsteroide)
            posY = - tamAsteroide
            velX = random.randint(-1, 1)
            velY = random.randint(VEL_MINIMA, VEL_MAXIMA)
            imagem_redimensiodada = pygame.transform.scale(imagemAsteroide, (tamAsteroide, tamAsteroide))
            asteroides_rect = pygame.Rect(posX, posY, tamAsteroide, tamAsteroide )

            asteroide = {
                'objRect': asteroides_rect,
                'imagem' : imagem_redimensiodada,
                'vel' :(velX, velY)
            }
            asteroides.append(asteroide)
            for asteroide in asteroides:
                moverElemento(asteroide)
                janela.blit(asteroide['imagem'], asteroide['objRect'])

            for asteroide in asteroides[:]:
                 topo_asteroide = asteroide['objRect'].top
                 if topo_asteroide > ALTURA_JANELA:
                      asteroides.remove(asteroide)

            for raio in raios:
                 moverElemento(raio)
                 janela.blit(raio('imagem'), raio('objRect'))  

            for raio in raios[:]:
                 base_raio = raio['objRect'].bottom
                 if base_raio < 0:
                      raios.remove(raio)

            moverJogador(jogador, teclas, (LARGURA_JANELA, ALTURA_JANELA))

            #exibe o jogador na tela
            janela.blit(jogador['imagem'],jogador['objRect'])

            for asteroide in asteroides[:]:
                 jogadorColidiu = jogador['objRect'].colliderect(asteroide['objRect'])
                 if jogadorColidiu:
                  if pontuacao > recorde:
                      recorde = pontuacao
                 deve_continuar = False
            for raio in raios[:]:
                 raioColidiu = raio['objRect'].colliderect(asteroide['objRect'])
                 if raioColidiu:
                      if raio in raios:
                           raios.remove(raio)
                      if asteroide in asteroides:
                           asteroides.remove(asteroide)
                           break              
            
        pygame.display.update()#atualizar a janela
        relogio.tick(FPS)
    pygame.mixer.music.stop()
    somFinal.play()
    colocarTexto("GAME OVER", fonte, janela, (LARGURA_JANELA/10), (ALTURA_JANELA/2))
    colocarTexto("Pressione um tecla para jogar novamente", fonte, janela, (LARGURA_JANELA/10), (ALTURA_JANELA/2))
    pygame.display.update()
    aguardandoEntrada()
    somFinal.stop()