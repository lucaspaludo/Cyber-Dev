import pygame
import random

pygame.init()

tam_min = 15
tam_max = 40
VEL = 6
ITERACOES = 30
LARGURA = 600
ALTURA = 700

pygame.joystick.init()
joy = None
if pygame.joystick.get_count() > 0:
    joy = pygame.joystick.Joystick(0)
    joy.init()

pygame.display.set_caption("Asteroides Troianos")

texto_pont = 0
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

asteroide_img = pygame.image.load("asteroide_img.png")
laser_img = pygame.image.load("laser_img.png")
nave_img = pygame.image.load("nave.png")
fundo_img = pygame.image.load("fundo.jpg")

nave_img = pygame.transform.scale(nave_img, (75, 150))
laser_img = pygame.transform.scale(laser_img, (20, 50))

fonte = pygame.font.SysFont(None, 36)

pygame.mixer.init()
Somtiro = pygame.mixer.Sound('tiro_nave.mp3')
SomRecord = pygame.mixer.Sound('somRecord.mp3')
SomFinal = pygame.mixer.Sound('final.mp3')
pygame.mixer.music.load("somFundo.mp3")
pygame.mixer.music.play(-1, 0, 0)

pontuacao = 0
recorde = 0
clock = pygame.time.Clock()

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

def moverBloco(bloco):
    bloco['objRect'].y += bloco['vel']

def moverLaser(laser):
    laser['objRect'].y -= laser['vel']

janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.mouse.set_visible(False)

jogador = {
    'objRect': pygame.Rect(250, 570, 50, 90),
    'imagem': nave_img,
    'vel': VEL
}

teclas = {
    'esquerda': False,
    'direita': False,
    'cima': False,
    'baixo': False,
}

contador = 0
blocos = []
lasers = []
deve_continuar = True

while deve_continuar:
    clock.tick(40)
    pontuacao += 1
    janela.blit(fundo_img, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                deve_continuar = False
            if evento.key == pygame.K_SPACE:
                lasers.append({
                    'objRect': pygame.Rect(jogador['objRect'].centerx, jogador['objRect'].top, 20, 50),
                    'imagem': laser_img,
                    'vel': VEL
                })
                Somtiro.play()
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas['esquerda'] = True
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas['direita'] = True
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas['cima'] = True
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas['baixo'] = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas['esquerda'] = False
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas['direita'] = False
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas['cima'] = False
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas['baixo'] = False

    if joy:
        ax_x = joy.get_axis(0)
        ax_y = joy.get_axis(1)
        if abs(ax_x) < 0.2: ax_x = 0
        if abs(ax_y) < 0.2: ax_y = 0
        jogador['objRect'].x += int(ax_x * jogador['vel'])
        jogador['objRect'].y += int(ax_y * jogador['vel'])
        if joy.get_button(0):
            lasers.append({
                'objRect': pygame.Rect(jogador['objRect'].centerx, jogador['objRect'].top, 20, 50),
                'imagem': laser_img,
                'vel': VEL
            })
            Somtiro.play()

    moverJogador(jogador, teclas, (LARGURA, ALTURA))

    contador += 1
    if contador >= ITERACOES:
        contador = 0
        TAMANHOBLOCO = random.randint(tam_min, tam_max)
        posX = random.randint(1, LARGURA - TAMANHOBLOCO)
        posY = -TAMANHOBLOCO
        velRandom = random.randint(1, VEL + 3)
        blocos.append({
            'objRect': pygame.Rect(posX, posY, TAMANHOBLOCO, TAMANHOBLOCO),
            'imagem': asteroide_img,
            'vel': velRandom
        })

    for Laser in lasers:
        moverLaser(Laser)
        janela.blit(Laser['imagem'], Laser['objRect'])

    for bloco in blocos:
        moverBloco(bloco)
        pygame.draw.rect(janela, BRANCO, bloco['objRect'])

    janela.blit(jogador['imagem'], jogador['objRect'])

    for bloco in blocos:
        bateu = jogador['objRect'].colliderect(bloco['objRect'])
        if pontuacao > recorde:
            recorde = pontuacao
            SomRecord.play()

    for Laser in lasers[:]:
        if Laser['objRect'].bottom < 0:
            lasers.remove(Laser)

    texto_pont = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)
    texto_rec = fonte.render(f"Recorde: {recorde}", True, BRANCO)
    janela.blit(texto_pont, (10, 10))
    janela.blit(texto_rec, (10, 40))

    pygame.display.flip()

pygame.quit()
