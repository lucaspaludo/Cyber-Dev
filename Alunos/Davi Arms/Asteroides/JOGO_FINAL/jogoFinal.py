import pygame, random 

imagemNave = pygame.image.load('nave.png')
imagemTiro = pygame.image.load('tiro.png')
imagemMeteoro = pygame.image.load('meteoro.png')
imagemFundo = pygame.image.load('fundo.png')
LARGURA_JANELA = 1000
ALTURA_JANELA = 600
COR_TEXTO = (255, 255, 255)
FPS = 40
TAM_MINIMO = 60
TAM_MAXIMO = 90
VEL_MINIMA = 1
VEL_MAXIMO = 10
VEL_JOGADOR = 10
VEL_TIRO = (0, -21)
ITERACOES = 20
LARGURA_NAVE = imagemNave.get_width()
ALTURA_NAVE = imagemNave.get_height()
LARGURA_TIRO = imagemTiro.get_width()
ALTURA_TIRO = imagemTiro.get_height()

def moverjogador(jogador, teclas, dim_janela):
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

def moverelemento(elemento):
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
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption('Isteroidis')
pygame.mouse.set_visible(False) #elimina o cursor do mouse
imagemFundoRedim = pygame.transform.scale(imagemFundo,(LARGURA_JANELA, ALTURA_JANELA))

#configura a fonte
fonte = pygame.font.Font(None, 48)

somFinal = pygame.mixer.Sound('GameOver.mp3')
somRecorde = pygame.mixer.Sound('recorde.mp3')
somTiro = pygame.mixer.Sound('tiro.mp3')
pygame.mixer.music.load('musicafundo.mp3')
colocarTexto('Isteroidis', fonte, janela, LARGURA_JANELA/10, ALTURA_JANELA/5)
colocarTexto('Pressione uma tecla para começar', fonte, janela, LARGURA_JANELA/20, ALTURA_JANELA/3)


pygame.display.update()
aguardarEntrada()

recorde = 0
while True:
    asteroides = []
    raios = []
    pontuação = 0
    deve_continuar = False
    teclas = {
        'esquerda': False,
        'direita': False,
        'cima': False,
        'baixo': False,
    }
    contador = 0
    pygame.mixer.music.play(-1, 0, 0)
    posX = LARGURA_JANELA/2
    posY = ALTURA_JANELA - 50
    jogador = {
        'objRect': pygame.Rect(posX, posY, LARGURA_NAVE, ALTURA_NAVE),
        'imagem': imagemNave,
        'vel': VEL_JOGADOR
    }

    #terceira etapa
    while deve_continuar:
        pontuacao += 1
        if pontuação == recorde:
            somRecorde.play()
        for evento in pygame.event.get(): 
            if evento.type == pygame.QUIT:
                terminar()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    deve_continuar = False
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    teclas['esquerda'] = True 
                if evento.key == pygame.K_RIGHT or evento.key == pygame.k_d:
                    teclas['direita'] = True
                if evento.key == pygame.K_UP or evento.key ==  pygame.k_w:
                    teclas['cima'] = True 
                if evento.key == pygame.K_DOWN or evento.key == pygame.k_s:
                    teclas['baixo'] = True
                if evento.key == pygame.K_SPACE:
                    raio = {
                        'objRect': pygame.Rect(jogador['objRect'].centerx, jogador ['objRect'].top, LARGURA_TIRO, ALTURA_TIRO),
                        'vel': VEL_TIRO,
                        'imagem': imagemTiro,
                        }
                raios.append(raio)
                somTiro.play()
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    teclas['esquerda'] = False
                if evento.key == pygame.K_RIGHT or evento.key == pygame.k_d:
                    teclas['direita'] = False
                if evento.key == pygame.K_UP or evento.key ==  pygame.k_w:
                    teclas['cima'] = False
                if evento.key == pygame.K_DOWN or evento.key == pygame.k_s:
                    teclas['baixo'] = False

                if evento.type == pygame.MOUSEMOTION:
                    centroX_jogador = jogador['objRect'].centerx 
                    centroY_jogador = jogador['objRect'].centery
                    jogador['objRect'].move_ip(evento.pos[0], - centroX_jogador, evento.pos[1] - centroY_jogador)

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    raio = {
                        'objRect': pygame.Rect(jogador['objRect'].centerx, jogador ['objRect'].top, LARGURA_TIRO, ALTURA_TIRO),
                        'imagem': imagemTiro,
                        'vel': VEL_TIRO
                    }
                    raios.append(raio)
                    somTiro.play()

        janela.blit(imagemFundoRedim, (0, 0))
        colocarTexto(f'Pontuação: {str(pontuacao)}', fonte, janela, 2,5, 0)
        colocarTexto(f'Recorde: {str(recorde)}', fonte, janela, 10, 40)
        pygame.display.upadate() #atualizar a janela
        relogio.tick(FPS)
        