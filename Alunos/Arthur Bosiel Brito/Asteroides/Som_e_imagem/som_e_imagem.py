import pygame, random
imagemPassaro  = pygame.image.load('personagem.png')
imagemMosquito = pygame.image.load('alvo.png')
imagemFundo = pygame.image.load('fundo.png')
LARGURA_JANELA = imagemFundo.get_width()
ALTURA_JANELA  = imagemFundo.get_height()
LARGURA_PASSARO = imagemPassaro.get_width()
ALTURA_PASSARO = imagemPassaro.get_height()
LARGURA_MOSQUITO = imagemMosquito.get_width()
ALTURA_MOSQUITO = imagemMosquito.get_height()
VEL = 6
ITERACOES = 30

pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption('Imagem e som')
# dicionário
joador = {
    'objRect': pygame.Rect(300, 100, LARGURA_PASSARO, ALTURA_PASSARO),
    'imagem': imagemPassaro,
    'vel': VEL
}
# configurando o som
somComer = pygame.mixer.Sound('comer.mp3')
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play(-1, 0.0)
somAtivado = True
teclas = {
    'esquerda' = False,
    'direita' = False,
    'cima' = False,
    'baixo' = False
 }
contador = 0
mosquitos = []
deve_continuar = True

while deve_continuar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False
        if  evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                deve_continuar = False
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas['esquerda'] = True
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas['direita'] = True
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas['cima'] = True
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas['baixo'] =True