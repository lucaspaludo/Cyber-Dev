import pygame, random

imagemNave = pygame.image.load('nave.png')
imagemlaser = pygame.image.load('laser.jpg')
imagemAste = pygame.image.load('aste.png')
imagemFundo = pygame.image.load('space.jpg')
LJ = 1000
AJ = 600
COR_TXT = (255, 255, 255)
FPS = 40
TAM_MINIMO = 90
TAM_MAX = 125
VEL_MINI = 1
VEL_MAX = 9
VEL_PY = 5
VEL_LASER = (0, -20)
INTERACOES = 20
LN = imagemNave.get_width()
AN = imagemNave.get_height()
LR = imagemlaser.get_width()
AR = imagemlaser.get_height()

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

def moverElemento(elementos):
    elementos['objRect'].x += elementos['vel'][0]
    elementos['objRect'].y += elementos['vel'][1]

def terminar():
    pygame.quit()
    exit()

def agurdarEntrada():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    terminar()
                return

def colocarTexto(texto, fonte, janela, x, y):
    objTexto = fonte.render(texto, True, COR_TXT)
    rectTexto = objTexto.get_rect()
    rectTexto.topleft = (x, y)
    janela.blit(objTexto, rectTexto)
    

pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LJ, AJ))
pygame.display.set_caption('Asteroides')
pygame.mouse.set_visible(False)

imagemFundoRedim = pygame.transform.scale(imagemFundo, (LJ, AJ))

fonte = pygame.font.Font(None, 48)

somFinal = pygame.mixer.Sound('final.mp3')
somRecord = pygame.mixer.Sound('record.mp3')
somlaser = pygame.mixer.Sound('laser.mp3')
pygame.mixer.music.load('musica.mp3')
colocarTexto('asteroids', fonte, janela, LJ/5, AJ/3)

colocarTexto('pressione uma tecla para começar', fonte, janela, LJ/20, AJ/2)

pygame.display.update()
agurdarEntrada()


recorde = 0
while True:
    asteroides = []
    lasers = []
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
    posX = LJ/2
    posY = AJ - 50
    jogador = {
        'objRect': pygame.Rect(posX, posY, LN, AN),
        'imagem':imagemNave,
        'VEL':VEL_PY
    }

    while deve_continuar:
        pontuacao += 1
        if pontuacao == recorde:
            somRecord.play()
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
                    lasers = {
                        'objRect': pygame.Rect(jogador['objRect'].centerx, jogador['objRect'].top, LJ, AJ),
                        'vel': VEL_LASER,
                        'imagem': imagemlaser
                    }
                    lasers.append(lasers)
                    somlaser.play()
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
            centerX_jogador = jogador['objRect'].centerx
            centery_jogador = jogador['objRect'].centery
            jogador['objRect'].move_ip(evento.pos[0] - centerX_jogador, evento.pos - centery_jogador)

        if evento.type == pygame.MOUSEBUTTONDOWN:
            lasers = {
                'objRect': pygame.Rect(jogador['objRect'].centerx, jogador['objRect'].top, LJ, AJ),
                'vel': VEL_LASER,
                'imagem': imagemlaser
            }
            lasers.append(lasers)
            somlaser.play()
        janela.blit(imagemFundoRedim, (0, 0))
        colocarTexto(f"pontuação: {str(pontuacao)}", fonte, janela, 10, 0 )
        colocarTexto(f"recorde: {str(recorde)}", fonte, janela,10, 40)
        pygame.display.update()
        relogio.tick(FPS)

