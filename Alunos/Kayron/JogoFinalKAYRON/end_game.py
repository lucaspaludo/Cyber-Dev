import pygame
import random

pygame.init()


LJ = 1000
AJ = 600
FPS = 40
COR_TXT = (255, 255, 255)


TAM_MINIMO = 100
TAM_MAX = 135
VEL_MINI = 1
VEL_MAX = 9
VEL_PY = 5
VEL_LASER = (0, -35)
INTERACOES = 20


imagemNave = pygame.image.load('nave.png')
imagemLaser = pygame.image.load('laser.jpg')
imagemAste = pygame.image.load('aste.png')
imagemFundo = pygame.transform.scale(pygame.image.load('space.jpg'), (LJ, AJ))

LN = imagemNave.get_width()
AN = imagemNave.get_height()
LR = imagemLaser.get_width()
AR = imagemLaser.get_height()

somFinal = pygame.mixer.Sound('final.mp3')
somRecord = pygame.mixer.Sound('record.mp3')
somLaser = pygame.mixer.Sound('laser.mp3')
pygame.mixer.music.load('musica.mp3')

fonte = pygame.font.Font(None, 48)

janela = pygame.display.set_mode((LJ, AJ))
pygame.display.set_caption('Asteroides')
pygame.mouse.set_visible(False)
relogio = pygame.time.Clock()

def colocarTexto(texto, fonte, janela, x, y):
    objTexto = fonte.render(texto, True, COR_TXT)
    rectTexto = objTexto.get_rect()
    rectTexto.topleft = (x, y)
    janela.blit(objTexto, rectTexto)

def moverJogador(jogador, teclas):
    if teclas['esquerda'] and jogador['objRect'].left > 0:
        jogador['objRect'].x -= jogador['vel']
    if teclas['direita'] and jogador['objRect'].right < LJ:
        jogador['objRect'].x += jogador['vel']
    if teclas['cima'] and jogador['objRect'].top > 0:
        jogador['objRect'].y -= jogador['vel']
    if teclas['baixo'] and jogador['objRect'].bottom < AJ:
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

janela.blit(imagemFundo, (0, 0))
colocarTexto("ASTEROIDS", fonte, janela, LJ // 3, AJ // 3)
colocarTexto("Pressione uma tecla para começar", fonte, janela, LJ // 5, AJ // 2)
pygame.display.update()
aguardarEntrada()

recorde = 0

while True:
    asteroides = []
    lasers = []
    pontuacao = 0
    deve_continuar = True
    teclas = {'esquerda': False, 'direita': False, 'cima': False, 'baixo': False}
    contador = 0

    pygame.mixer.music.play(-1)

    jogador = {
        'objRect': pygame.Rect(LJ // 2, AJ - AN - 20, LN, AN),
        'imagem': imagemNave,
        'vel': VEL_PY
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
                elif evento.key in (pygame.K_LEFT, pygame.K_a):
                    teclas['esquerda'] = True
                elif evento.key in (pygame.K_RIGHT, pygame.K_d):
                    teclas['direita'] = True
                elif evento.key in (pygame.K_UP, pygame.K_w):
                    teclas['cima'] = True
                elif evento.key in (pygame.K_DOWN, pygame.K_s):
                    teclas['baixo'] = True
                elif evento.key == pygame.K_SPACE:
                    novo_laser = {
                        'objRect': pygame.Rect(jogador['objRect'].centerx - LR//2, jogador['objRect'].top - AR, LR, AR),
                        'vel': VEL_LASER,
                        'imagem': imagemLaser
                    }
                    lasers.append(novo_laser)
                    somLaser.play()

            if evento.type == pygame.KEYUP:
                if evento.key in (pygame.K_LEFT, pygame.K_a):
                    teclas['esquerda'] = False
                elif evento.key in (pygame.K_RIGHT, pygame.K_d):
                    teclas['direita'] = False
                elif evento.key in (pygame.K_UP, pygame.K_w):
                    teclas['cima'] = False
                elif evento.key in (pygame.K_DOWN, pygame.K_s):
                    teclas['baixo'] = False

            if evento.type == pygame.MOUSEMOTION:
                jogador['objRect'].center = evento.pos

            if evento.type == pygame.MOUSEBUTTONDOWN:
                novo_laser = {
                    'objRect': pygame.Rect(jogador['objRect'].centerx - LR//2, jogador['objRect'].top - AR, LR, AR),
                    'vel': VEL_LASER,
                    'imagem': imagemLaser
                }
                lasers.append(novo_laser)
                somLaser.play()

        janela.blit(imagemFundo, (0, 0))
        colocarTexto(f"Pontuação: {pontuacao}", fonte, janela, 10, 10)
        colocarTexto(f"Recorde: {recorde}", fonte, janela, 10, 50)

        contador += 1
        if contador >= INTERACOES:
            contador = 0
            tam = random.randint(TAM_MINIMO, TAM_MAX)
            x = random.randint(0, LJ - tam)
            y = -tam
            velX = random.randint(-1, 1)
            velY = random.randint(VEL_MINI, VEL_MAX)
            img = pygame.transform.scale(imagemAste, (tam, tam))
            asteroides.append({
                'objRect': pygame.Rect(x, y, tam, tam),
                'vel': (velX, velY),
                'imagem': img
            })

        for ast in asteroides[:]:
            moverElemento(ast)
            janela.blit(ast['imagem'], ast['objRect'])
            if ast['objRect'].top > AJ:
                asteroides.remove(ast)

        for laser in lasers[:]:
            moverElemento(laser)
            janela.blit(laser['imagem'], laser['objRect'])
            if laser['objRect'].bottom < 0:
                lasers.remove(laser)

        moverJogador(jogador, teclas)
        janela.blit(jogador['imagem'], jogador['objRect'])

        for ast in asteroides[:]:
            if jogador['objRect'].colliderect(ast['objRect']):
                if pontuacao > recorde:
                    recorde = pontuacao
                deve_continuar = False
                break
            for laser in lasers[:]:
                if laser['objRect'].colliderect(ast['objRect']):
                    lasers.remove(laser)
                    asteroides.remove(ast)
                    break

        pygame.display.update()
        relogio.tick(FPS)

    pygame.mixer.music.stop()
    somFinal.play()
    janela.blit(imagemFundo, (0, 0))
    colocarTexto("GAME OVER", fonte, janela, LJ // 3, AJ // 3)
    colocarTexto("Pressione uma tecla para jogar novamente", fonte, janela, LJ // 6, AJ // 2)
    pygame.display.update()
    aguardarEntrada()
    somFinal.stop()
