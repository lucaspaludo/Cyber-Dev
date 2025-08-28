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

def moverJogador():
    pass

def moverElemento():
    pass

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
while True:
    asteroides = []
    raio = []
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

        janela.blit(imagemFundoRedim, (0, 0))
        colocarTexto(f'Pontuação: {str(pontuacao)}', fonte, janela, 10, 2)
        colocarTexto(f'Recorde: {str(recorde)}', fonte, janela, 10, 40)
        pygame.display.update() #atualizar a janela
        relogio.tick(FPS)