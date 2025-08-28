import pygame
import random

pygame.init()
ImagemPlayer = pygame.image.load('a.png')  
ImagemPortal = pygame.image.load('por.png')
ImagemFundo = pygame.image.load('f.jpg')
ImagemFundo2 = pygame.image.load('boss.png')
ImagemVidaPlayer = pygame.image.load('vida_player.png')
ImagemBoss = pygame.image.load('bossP.png')

pos_l = 282
pos_a = 287

PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)

LARGURAJANELA = 1000
ALTURAJANELA = 700
VEL = 6

pygame.mixer.init()
pygame.mixer.music.load("fundo.mp3")
pygame.mixer.music.play(-1, 0, 0)

largura_frame = 65
altura_frame = 70
num_frames = 4

largura_portal = 50
altura_portal = 110
num_frames_portal = 4
frame_portal = 0
tempo_animacao_portal = 4
contador_portal = 0


ImagemFundo = pygame.transform.scale(ImagemFundo, (1008, 703))
ImagemFundo2 = pygame.transform.scale(ImagemFundo2, (1008, 703))
ImagemPortal = pygame.transform.scale(ImagemPortal, (200, 100))
ImagemVidaPlayer = pygame.transform.scale(ImagemVidaPlayer, (150, 100))
boss = pygame.transform.scale(ImagemBoss, (100, 130))

janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Imagem e Som")
relogio = pygame.time.Clock()

jogador = {
    'objRect': pygame.Rect(pos_l, pos_a, largura_frame, altura_frame),
    'vel': VEL,
    'imagemF': ImagemPlayer,
    'imagemT': ImagemPlayer
}

portal = {
    'objRect': pygame.Rect(10, 360, 35, 80),
    'imagem': ImagemPortal,
    'ativo': True
}

teclas = {
    'esquerda': False,
    'direita': False,
    'cima': False,
    'baixo': False,
}
bossVisivel = False
fundo_atual = ImagemFundo
#Texto da vida do player
Txt_ativado = False
borda_s = 0
borda_i = ALTURAJANELA
fonte = pygame.font.Font(None, 48)
texto = fonte.render('', Txt_ativado, PRETO)

#Sprites player
x_sprite = 0
y_sprite = 0  
frame_atual = 0  
tempo_animacao = 5

#Sprite vida Player
atual_vidaPlayer = 0
ALtura_vidaPlayer = 80
Largura_vidaPlayer = 30
conf_vidaPlayer = pygame.Rect(20, 30, 150, 100)
VidaVisivel = False


deve_continuar = True
while deve_continuar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
            deve_continuar = False
        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_LEFT, pygame.K_a):
                teclas['esquerda'] = True
            if evento.key in (pygame.K_RIGHT, pygame.K_d):
                teclas['direita'] = True
            if evento.key in (pygame.K_UP, pygame.K_w):
                teclas['cima'] = True
            if evento.key in (pygame.K_DOWN, pygame.K_s):
                teclas['baixo'] = True
        if evento.type == pygame.KEYUP:
            if evento.key in (pygame.K_LEFT, pygame.K_a):
                teclas['esquerda'] = False
            if evento.key in (pygame.K_RIGHT, pygame.K_d):
                teclas['direita'] = False
            if evento.key in (pygame.K_UP, pygame.K_w):
                teclas['cima'] = False
            if evento.key in (pygame.K_DOWN, pygame.K_s):
                teclas['baixo'] = False

    def moverJogador(jogador, teclas, dim_janela):
        if teclas['esquerda'] and jogador['objRect'].left > 0:
            jogador['objRect'].x -= jogador['vel']
        if teclas['direita'] and jogador['objRect'].right < dim_janela[0]:
            jogador['objRect'].x += jogador['vel']
        if teclas['cima'] and jogador['objRect'].top > borda_s:
            jogador['objRect'].y -= jogador['vel']
        if teclas['baixo'] and jogador['objRect'].bottom < borda_i:
            jogador['objRect'].y += jogador['vel']

    moverJogador(jogador, teclas, (LARGURAJANELA, ALTURAJANELA))

    frame_atual += 1
    if frame_atual >= tempo_animacao:
        x_sprite = (x_sprite + 1) % num_frames
        frame_atual = 0
    
    if teclas['direita']:
        y_sprite = 2
    elif teclas['esquerda']:
        y_sprite = 1
    elif teclas['cima']:
        y_sprite = 3
    elif teclas['baixo']:
        y_sprite = 0
    else:
        x_sprite = 0

    if portal['ativo']:
        contador_portal += 1
        if contador_portal >= tempo_animacao_portal:
            frame_portal = (frame_portal + 1) % num_frames_portal
            contador_portal = 0

    if portal['ativo'] and jogador['objRect'].colliderect(portal['objRect']):
        fundo_atual = ImagemFundo2
        portal['ativo'] = False
        pygame.mixer.music.stop()
        borda_s = 87
        borda_i = ALTURAJANELA - 115
        texto = fonte.render('Player', Txt_ativado, BRANCO)
        VidaVisivel = True
        bossVisivel = True
    
    janela.blit(fundo_atual, (-5, -3))
    if bossVisivel == True:
        janela.blit(boss, (900, 280))
    if portal['ativo']:
        janela.blit(
            portal['imagem'],
            portal['objRect'],
            (frame_portal * largura_portal, 0, largura_portal, altura_portal)
        )
    if VidaVisivel == True:
        janela.blit(ImagemVidaPlayer, conf_vidaPlayer)

    janela.blit(texto, [50, 0])
    janela.blit(
        jogador['imagemT'],
        jogador['objRect'],
        (x_sprite * largura_frame, y_sprite * altura_frame, largura_frame, altura_frame)
    )

    pygame.display.flip()
    pygame.display.update()
    relogio.tick(17)

pygame.quit()
