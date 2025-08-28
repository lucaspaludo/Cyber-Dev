import pygame, random

imagemDragao = pygame.image.load("dragao.png")
imagemPresa = pygame.image.load("presa.png")
imagemfundo = pygame.image.load("fundo.jpg")

LARGURA_JANELA = imagemfundo.get_width()
ALTURA_JANELA = imagemfundo.get_height()

LARGURA_DRAGAO = imagemDragao.get_width()
ALTURA_DRAGAO = imagemDragao.get_height()

LARGURA_PRESA = imagemPresa.get_width()
ALTURA_PRESA = imagemPresa.get_height()
VEL = 6
ITERACOES = 30

pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("Imagem e Som")

#dicionario
jogador = {
    'objRect': pygame.Rect(300, 100, LARGURA_DRAGAO, ALTURA_DRAGAO), 
    'imagem' : imagemDragao,
    'vel' : VEL
}

print (LARGURA_JANELA)
print (LARGURA_DRAGAO)
print (LARGURA_PRESA)
somfundo = pygame.mixer.Sound("musica_de_fundo.mp3")
pygame.mixer.music.load("musica_de_fundo.mp3")
pygame.mixer.music.play(-1, 0.0)
somAtivado = True
teclas = {
    'esquerda': False,
    'direita': False,
    'cima': False,
    'baixo':False
}
contador = 0
presa = []
deve_continuar = True

while deve_continuar:   
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                deve_continuar = False
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas["esquerda"] = True
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas["direita"] = True
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas["cima"] = True
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas["baixo"] = True
            if evento.key == pygame.K_m:
                if somAtivado:
                    pygame.mixer.music.stop()
                    somAtivado = False
                else:
                    pygame.mixer.music.play(-1, 0.0)
                    somAtivado = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas["esquerda"] = False
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas["direita"] = False
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas["cima"] = False
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas["baixo"] = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            presa.append({
                'objRect' : pygame.Rect(evento.pos[0], evento.pos[1], ALTURA_PRESA, LARGURA_PRESA),
                'imagem' : imagemPresa,
                'vel' : VEL - 3
            })
    contador += 1
    if contador  >= ITERACOES:
        contador = 0
        posY = random.randint(0, ALTURA_JANELA - ALTURA_PRESA)
        posX = -LARGURA_PRESA
        velRandom = random.randint(VEL - 3, VEL + 3) 
        presa.append({
            'objRect' : pygame.Rect(posX, posY, LARGURA_PRESA, ALTURA_PRESA),
            'imagem' : imagemPresa,
            'vel' : VEL
        })
    janela.blit(imagemfundo, (0, 0))
    pygame.display.update()
    relogio.tick(40)









































































































































































































