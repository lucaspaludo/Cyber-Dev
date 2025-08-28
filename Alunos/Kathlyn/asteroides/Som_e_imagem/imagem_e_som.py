import pygame, random

imagemAbelha = pygame.image.load('abelha.png')
imagemFlor =  pygame.image.load('flor.png')
imagemFundo = pygame.image.load('floresta.png')
LARGURA_JANELA = imagemFundo.get_width()
ALTURA_JANELA = imagemFundo.get_height()
LARGURA_ABELHA = imagemAbelha.get_width()
ALTURA_ABELHA = imagemAbelha.get_height()
LARGURA_FLOR = imagemFlor.get_width()
ALTURA_FLOR = imagemFlor.get_height()
VEL = 6
ITERACOES = 30

pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA))
pygame.display.set_caption('Imagem e Som')
jogador = {
    'objRect': pygame.Rect(300, 100, LARGURA_ABELHA,ALTURA_ABELHA),
    'imagem' : imagemAbelha,
    'vel': VEL
}
print(LARGURA_JANELA)
print(LARGURA_FLOR)
print(LARGURA_ABELHA)
somComer = pygame.mixer.Sound ('moeda.mp3')
pygame.mixer_music.load('musica.mp3')
pygame.mixer.music.play(-1, 0.0)
somAtivado = True
teclas = {
    'esquerda': False,
    ' direita': False,
    'cima': False,
    'baixo': False,
}
contador = 0
flores = []
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
                    pygame.mixer.music.play(-1, 50.0)
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
            flores.append({
                'objRect': pygame.Rect(evento.pos[0], evento.pos[1], LARGURA_FLOR,ALTURA_FLOR),
                'imagem': imagemFlor,
                'vel': VEL -3
            })
          #  print(flores)
    contador += 1
    if contador >= ITERACOES:
        contador = 0
        posY = random.randint(0, ALTURA_JANELA - ALTURA_FLOR)
        posX = -LARGURA_FLOR
        velRandom = random.randint(VEL -3, VEL + 3)
        flores.append({
            'objRect': pygame.Rect(posX, posY, LARGURA_FLOR,ALTURA_FLOR),
            'imagem': imagemFlor,
            'vel': velRandom
        })
    janela.blit(imagemFundo,(0, 0))
    pygame.display.update()
    relogio.tick(40)
