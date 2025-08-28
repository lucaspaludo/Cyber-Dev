import pygame, random 

imagemNave = pygame.image.load('nave.png')
imagemraio = pygame.image.load('raio.png')
imagemaAsteroids = pygame.image.load('Asteroids.png')
imagemFundo = pygame.image.load('fundo.png')
LARGURA_JANELA = 1000
ALTURA_JANELA = 600
COR_TEXTO = (255, 255, 255)
FPS = 40
TAM_MINIMO = 60
TAM_MAXIMO = 90
VEL_MINIMA = 1
VEL_MAXIMA = 8
VEL_JOGADOR = 5
VEL_RAIO = (0, 20)
ITERACOES = 20
LARGURA_NAVE = imagemNave.get_width()
ALTURA_NAVE = imagemNave.get_height()
LARGURA_RAIO = imagemraio.get_width()
ALTURA_RAIO = imagemraio.get_height()

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
            if evento.key == pygame.K_ESCAPE:
                terminar()
            return
        
def colocarTexto(texto, fonte, janela, x, y):
    objTexto = fonte.render(texto, True, COR_TEXTO)
    rectTexto = objTexto.get_rect()
    rectTexto = topleft = (x, y)
    janela.blit(objTexto, rectTexto)


pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption('asteroids')
pygame.mouse.set_visible(False)

imagemFundoRedim = pygame.transform.scale(imagemFundo, (LARGURA_JANELA, ALTURA_JANELA))
fonte = pygame.font.Font(None, 48)

somFinal = pygame.mixer.Sound('final.mp3')
somRecorde = pygame.mixer.Sound('recorde.mp3')
somTiro = pygame.mixer.Sound('tiro.mp3')
pygame.mixer.music.load('musica.mp3')
colocarTexto('Asteroids', fonte, janela, LARGURA_JANELA/5, ALTURA_JANELA/3)

colocarTexto('Pressione uma tecla para comecar', fonte, janela, LARGURA_JANELA/20, ALTURA_JANELA/2)

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
        'baixo': False,
    }

    contador = 0
    pygame.mixer.music.play(-1, 0, 0)
    posX = LARGURA_JANELA/2
    posY = ALTURA_JANELA -50
    jogador = {
        'objRect': pygame.Rect(posX, posY, LARGURA_NAVE, ALTURA_NAVE),
        'imagem': imagemNave,
        'vel':VEL_JOGADOR
        
        }

    while deve_continuar:
        pontuacao += 1
        if pontuacao == recorde:
            somRecorde.play()
        janela.blit(imagemFundoRedim, (0, 0))
        colocarTexto(f'Pontuacao:{str(pontuacao)}', fonte, janela, 10, 0)
        colocarTexto(f'Recorde:{str(recorde)}', fonte, janela, 10, 40)
        pygame.display.update()
        relogio.tick(FPS)
            

