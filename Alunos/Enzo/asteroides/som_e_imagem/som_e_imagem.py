import pygame, random


imagemOVINI = pygame.image.load("ovini.png")
imagemGUUMYBEAR = pygame.image.load("guumybear.png")
imagemFUNDO = pygame.image.load("fundo.png")

LARGURA_JANELA = imagemFUNDO.get_width()
ALTURA_JANELA = imagemFUNDO.get_height()

LARGURA_OVINI = imagemOVINI.get_width()
ALTURA_OVINI = imagemOVINI.get_height()

LARGURA_GUUMYBEAR = imagemGUUMYBEAR.get_width()
ALTURA_GUUYBEAR = imagemGUUMYBEAR.get_height()
VEL = 6
ITERACOES = 30

def moverjogador(jogador, teclas, dim_janela):
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

pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("imagem e som")

#dicionário
jogador = {
    'objRect': pygame.Rect(300, 100, LARGURA_OVINI, ALTURA_OVINI),
    'imagem': imagemOVINI,
    'vel': VEL
}


print(LARGURA_JANELA)
print(LARGURA_GUUMYBEAR)
print(LARGURA_OVINI)



somCOMER = pygame.mixer.Sound("comendo.mp3")
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(-1, 0,0)
somAtivado = True
teclas = {
    'esquerda': False,
    'direita': False,
    'cima': False,
    'baixo': False,
    }
contador = 0 
guumybear = []
deve_continuar = True

while deve_continuar:
     for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False
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
            if evento.key == pygame.K_m:
                if somAtivado:
                    pygame.mixer.music.stop()
                    somAtivado = False
                else:
                    pygame.mixer.music.play(-1, 0.0)
                    somAtivado = True 
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas['esquerda'] = False
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas['direita'] = False
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas['cima'] = False
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas['baixo'] = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            guumybear.append({
                'objRect': pygame.Rect(evento.pos[0], evento.pos[1], LARGURA_GUUMYBEAR, ALTURA_GUUYBEAR),
                'imagem' : imagemGUUMYBEAR,
                'vel': VEL - 3
            })
     contador += 1
     if contador >= ITERACOES:
        contaador = 0
        posY = random.randint(0, ALTURA_JANELA - ALTURA_GUUYBEAR)
        posX = -LARGURA_GUUMYBEAR
        velRandom = random.randint(VEL - 3, VEL + 3)
        guumybear.append({
            'objRect': pygame.Rect(posX, posY, LARGURA_GUUMYBEAR, ALTURA_GUUYBEAR),
            'imagem': imagemGUUMYBEAR,
            'vel':velRandom
        })
     janela.blit(imagemFUNDO, (0, 0))



     pygame.display.update()
     relogio.tick(40)