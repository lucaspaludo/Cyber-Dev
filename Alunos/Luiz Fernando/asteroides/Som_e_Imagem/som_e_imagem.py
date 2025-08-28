import pygame, random
imagemTubarao = pygame.image.load("tubarao.png")
imagemPeixe = pygame.image.load("peixe.png")
imagemFundo = pygame.image.load("fundo.png")
LARGURA_JANELA = imagemFundo.get_width()
ALTURA_JANELA = imagemFundo.get_height()
LARGURA_TUBARAO = imagemTubarao.get_width()
ALTURA_TUBARAO = imagemTubarao.get_height()
LARGURA_PEIXE = imagemPeixe.get_width()
ALTURA_PEIXE = imagemPeixe.get_height()
VEL = 6
ITERACOES = 30

pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("Imagem e Som")
#dicionário
jogador = {
    'objRect': pygame.Rect(300, 100, LARGURA_TUBARAO, ALTURA_TUBARAO),
    'imagem': imagemTubarao,
    'vel': VEL
}
print(LARGURA_JANELA)
print(LARGURA_PEIXE)
print(LARGURA_TUBARAO)
#configurando som
somComer = pygame.mixer.Sound("comer.mp3")
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(-1, 0.0)
somAtivado = True
teclas = {
    'esquerda': False,
    'direita': False,
    'cima': False,
    'baixo': False
    }
contador = 0
peixes = []
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
            if evento.key == pygame. K_m:
                if somAtivado:
                    pygame.mixer.music.stop()
                    somAtivado = False
                else:
                    pygame.mixer.music.play(-1, 3,0)
                    somAtivado = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas['esquerda'] = True
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas['direita'] = True
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas['cima'] = True
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas['baixo'] = True
        if evento.type == pygame.MOUSEBUTTONDOWN:
            peixes.append({
                'objRect': pygame.Rect(evento.pos(1), LARGURA_PEIXE, ALTURA_PEIXE),
                'imagem': imagemPeixe,
                'vel': VEL - 3
            })

    contador += 1
    if contador > ITERACOES:
        contador = 0
        posY = random.randint(0, ALTURA_JANELA - ALTURA_PEIXE)
        posX = -LARGURA_PEIXE 
        posX = -LARGURA_PEIXE
        velRandom = random .randint (VEL - 3, VEL + 3)
        peixes.append({
            'objRect': pygame.Rect(posX, posY, LARGURA_PEIXE,ALTURA_PEIXE),
            'imagem': imagemPeixe,
            'vel': velRandom
        })

    janela.blit(imagemFundo, (0, 0))
    pygame.display.update()
    relogio.tick(40)
