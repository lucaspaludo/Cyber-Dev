import pygame, random

imagemNAVE = pygame.image.load('nave.png')
imagemRAIO = pygame.image.load('raio.png')
imagemASTEROIDES = pygame.image.load('asteroides.png')
imagemFUNDO = pygame.image.load('fundo.png')

LARGURA_JANELA = 1000
ALTURA_JANELA = 600
COR_TEXTO = (255, 255, 255)
FPS = 40 
TAM_MINIMO = 60
TAM_MAXIM0 = 90
VEL_MINIMA = 1
VEL_MAXIMA = 8
VEL_JOGADOR = 5
VEL_RAIO = (0, -20)
ITERACOES = 20

LARGURA_NAVE = imagemNAVE.get_width()
ALTURA_NAVE = imagemNAVE.get_height()
LARGURA_RAIO = imagemRAIO.get_width()
ALTURA_RAIO = imagemRAIO.get_height()

def moverJogador(jogador, teclas, dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior =  dim_janela[1]
    
    if teclas['esquerda'] and jogador['objRect'].left > borda_esquerda:
        jogador['objRect'].x -= jogador['vel']
    if teclas ['direita'] and jogador ['objRect'].right< borda_direita:
        jogador['objRect'].x += jogador['vel']
    if teclas['cima'] and jogador ['objRect'].bottom < borda_superior:
        jogador['objRect'].y -= jogador['vel']
    if teclas['baixo'] and jogador ['objRect'].bottom < borda_inferior:
        jogador['objRect'].y += jogador['vel']

def moverElementos(elemento):
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
                if evento.Key == pygame.K_ESCAPE:
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
pygame.display.set_caption('Asteroides')
pygame.mouse.set_visible(False) #elimina o cursor do mouse

imagemFUNDORedim = pygame.transform.scale(imagemFUNDO, (LARGURA_JANELA, ALTURA_JANELA))
#configura a fonte
fonte = pygame.font.Font(None, 48)
somFinal = pygame.mixer.Sound('final.mp3')
somRecorde = pygame.mixer.Sound('recorde.mp3')
somTiro = pygame.mixer.Sound('tiro.mp3')
pygame.mixer.music.load('musica.mp3')
colocarTexto('asteroides', fonte, janela, LARGURA_JANELA/5, ALTURA_JANELA/3)
colocarTexto('Pressione uma tecla para começar', fonte, janela, LARGURA_JANELA/20, ALTURA_JANELA/2 )

pygame.display.update()
aguardarEntrada()

recorde = 0
while True:
    asteroides = []
    raios = []
    pontuacao = 0
    deve_continuar = False
    teclas = {
        'esquerda': False,
        'direita': False,
        'cima': False,
        'baixo': False
    }
    contador = 0
    pygame.mixer.music.play(-1, 0, 0)
    posX = LARGURA_JANELA/2
    posY = ALTURA_JANELA - 50
    jogador = {
        'objRect': pygame.Rect(posX, posY, LARGURA_NAVE, ALTURA_NAVE),
        'imagem': imagemNAVE,
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
                        'imagem': imagemRAIO
                    }
                    raios.append(raio)
                    somTiro.play()
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    teclas['esquerda'] = False
                if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    teclas['direita'] = False
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
                    'vel':VEL_RAIO,
                    'imagem': imagemRAIO
                }
                raios.append(raio)
                somTiro.play()

        janela.blit(imagemFUNDORedim, (0, 0,))
        colocarTexto(f"pontuacao: {str(pontuacao)}", fonte, janela, 10, 0)
        colocarTexto(f"Recorde: {str(recorde)}",fonte, janela, 10, 40)
        pygame.display.update() #atualizar a janela
        relogio.tick(FPS)
        