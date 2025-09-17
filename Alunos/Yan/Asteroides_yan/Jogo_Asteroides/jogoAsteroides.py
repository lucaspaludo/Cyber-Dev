import pygame, random

imagemNave = pygame.image.load('nave.png')
imagemlaser = pygame.image.load('laser_img.png')
imagemAste = pygame.image.load('asteroide_img.png')
imagemFundo = pygame.image.load('fundo.jpg')

LJ, AJ = 1000, 600
COR_TXT = (255, 255, 255)
FPS = 40
TAM_MINIMO = 90
TAM_MAX = 125
VEL_MINI = 1
VEL_MAX = 9
VEL_PY = 5
VEL_LASER = (0, -20)
INTERACOES = 20
LN, AN = 90, 150
LR, AR = imagemlaser.get_width(), imagemlaser.get_height()

pygame.joystick.init()
joy = None
if pygame.joystick.get_count() > 0:
    joy = pygame.joystick.Joystick(0)
    joy.init()


def moverJogador(jogador, teclas, dim_janela):
    if teclas['esquerda'] and jogador['objRect'].left > 0:
        jogador['objRect'].x -= jogador['vel']
    if teclas['direita'] and jogador['objRect'].right < dim_janela[0]:
        jogador['objRect'].x += jogador['vel']
    if teclas['cima'] and jogador['objRect'].top > 0:
        jogador['objRect'].y -= jogador['vel']
    if teclas['baixo'] and jogador['objRect'].bottom < dim_janela[1]:
        jogador['objRect'].y += jogador['vel']

def moverElemento(elemento):
    elemento['objRect'].x += elemento['vel'][0]
    elemento['objRect'].y += elemento['vel'][1]

def terminar():
    pygame.quit()
    exit()

def agurdarEntrada():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar()
            if evento.type == pygame.KEYDOWN:
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

imagemNave = pygame.transform.scale(imagemNave, (LN, AN))
imagemFundoRedim = pygame.transform.scale(imagemFundo, (LJ, AJ))
fonte = pygame.font.Font(None, 48)

somFinal = pygame.mixer.Sound('final.mp3')
somRecord = pygame.mixer.Sound('somRecord.mp3')
somlaser = pygame.mixer.Sound('tiro_nave.mp3')
pygame.mixer.music.load('somFundo.mp3')

colocarTexto('ASTEROIDES', fonte, janela, LJ/5, AJ/3)
colocarTexto('PRESSIONE UMA TECLA PARA COMEÇAR', fonte, janela, LJ/20, AJ/2)
pygame.display.update()
agurdarEntrada()

recorde = 0

while True:
    asteroides = []
    raios = []
    pontuacao = 0
    continuar = True
    teclas = {'esquerda': False, 'direita': False, 'cima': False, 'baixo': False}
    contador = 0
    pygame.mixer.music.play(-1, 0, 0)
    jogador = {'objRect': pygame.Rect(LJ//2, AJ-AN-10, LN, AN), 'imagem': imagemNave, 'vel': VEL_PY}

    while continuar:
        if joy:
            ax_x = joy.get_axis(0)
            ax_y = joy.get_axis(1)
        if abs(ax_x) < 0.2: ax_x = 0
        if abs(ax_y) < 0.2: ax_y = 0
        jogador['objRect'].x += int(ax_x * jogador['vel'])
        jogador['objRect'].y += int(ax_y * jogador['vel'])
        if joy.get_button(0):
            raios.append({
                'objRect': pygame.Rect(jogador['objRect'].centerx, jogador['objRect'].top, 20, 50),
                'imagem': imagemlaser,
                'vel': VEL_LASER
            })
            
        pontuacao += 1
        if pontuacao > recorde:
            somRecord.play()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    terminar()
                if evento.key in [pygame.K_LEFT, pygame.K_a]:
                    teclas['esquerda'] = True
                if evento.key in [pygame.K_RIGHT, pygame.K_d]:
                    teclas['direita'] = True
                if evento.key in [pygame.K_DOWN, pygame.K_s]:
                    teclas['baixo'] = True
                if evento.key in [pygame.K_UP, pygame.K_w]:
                    teclas['cima'] = True
                if evento.key == pygame.K_SPACE:
                    raios.append({'objRect': pygame.Rect(jogador['objRect'].centerx -10, jogador['objRect'].top, LR, AR),
                                   'vel': VEL_LASER, 'imagem': imagemlaser})
                    somlaser.play()
            if evento.type == pygame.KEYUP:
                if evento.key in [pygame.K_LEFT, pygame.K_a]:
                    teclas['esquerda'] = False
                if evento.key in [pygame.K_RIGHT, pygame.K_d]:
                    teclas['direita'] = False
                if evento.key in [pygame.K_DOWN, pygame.K_s]:
                    teclas['baixo'] = False
                if evento.key in [pygame.K_UP, pygame.K_w]:
                    teclas['cima'] = False

        dt = relogio.tick(FPS)
        janela.blit(imagemFundoRedim, (0,0))
        colocarTexto(f'Pontuação: {pontuacao}', fonte, janela, 10, 0)
        colocarTexto(f'Recorde: {recorde}', fonte, janela, 10, 40)
        contador += 1
        if contador >= INTERACOES:
            contador = 0
            tamAst = random.randint(TAM_MINIMO, TAM_MAX)
            posx = random.randint(0, LJ - tamAst)
            posy = -tamAst
            velX, velY = random.randint(-1,1), random.randint(VEL_MINI, VEL_MAX)
            imagem_resiz = pygame.transform.scale(imagemAste, (tamAst, tamAst))
            asteroides.append({'objRect': pygame.Rect(posx,posy,tamAst,tamAst),'imagem':imagem_resiz,'vel':(velX,velY)})

        for ast in asteroides:
            moverElemento(ast)
            janela.blit(ast['imagem'], ast['objRect'])
        for ast in asteroides[:]:
            if ast['objRect'].top > AJ:
                asteroides.remove(ast)

        for raio in raios:
            moverElemento(raio)
            janela.blit(raio['imagem'], raio['objRect'])
        for raio in raios[:]:
            if raio['objRect'].bottom < 0:
                raios.remove(raio)

        moverJogador(jogador, teclas, (LJ, AJ))
        janela.blit(jogador['imagem'], jogador['objRect'])

        for ast in asteroides[:]:
            if jogador['objRect'].colliderect(ast['objRect']):
                continuar = False
                if pontuacao>recorde:
                    recorde=pontuacao
            for raio in raios[:]:
                if raio['objRect'].colliderect(ast['objRect']):
                    if raio in raios:
                        raios.remove(raio)
                    if ast in asteroides:
                        asteroides.remove(ast)
                    break
        # pygame.draw.rect(janela, (255, 255, 255), jogador['objRect'])
        pygame.display.update()
    pygame.mixer.music.stop()
    somFinal.play()
    janela.blit(imagemFundoRedim,(0,0))
    colocarTexto('GAME OVER', fonte, janela, LJ/10, AJ/2)
    colocarTexto('PRESSIONE UMA TECLA PARA JOGAR NOVAMENTE', fonte, janela, LJ/10, AJ/2 + 60)
    pygame.display.update()
    agurdarEntrada()
    
