import pygame, random

imagemNave = pygame.image.load('nave.png')
imagemlaser = pygame.image.load('laser_img.png')
imagemAste = pygame.image.load('asteroide_img.png')
imagemFundo = pygame.image.load('fundo.jpg')
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

def moverJogador():
    pass

def moverElemento():
    pass

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
somRecord = pygame.mixer.Sound('somRecord.mp3')
somlaser = pygame.mixer.Sound('tiro_nave.mp3')
pygame.mixer.music.load('somFundo.mp3')
colocarTexto('asteroides', fonte, janela, LJ/5, AJ/3)

colocarTexto('pressione uma tecla para começar', fonte, janela, LJ/20, AJ/2)

pygame.display.update()
agurdarEntrada()
recorde = 0
while True:
    asteroides = []
    raio = []
    pontuação = 0
    continuar = False
    teclas = {
        'esquerda': False,
        'direita':False,
        'cima': False,
        'baixo': False
    }
    contador=0
    pygame.mixer.music.play(-1, 0, 0)
    posx=LJ
    posy= AJ-50
    jogador={
        'objRect':pygame.Rect(posx, posy, LN, AN),
        'imagem': imagemNave,
        'vel':VEL_PY
    }
    while continuar:
        pontuação+=1
        if pontuação==recorde:
            somRecord.play()
        janela.blit(imagemFundoRedim, (0, 0))
        colocarTexto(f'Pontuação:, {str[pontuação]}', fonte, janela,10, 0)
        colocarTexto(f'Recorde: {str[recorde]}', fonte, janela, 10, 40)
        pygame.display.update()
        relogio.tick(FPS)