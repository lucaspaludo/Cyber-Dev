import pygame, random

imagemF1 = pygame.image.load("f1-car.png")
imagemGAS = pygame.image.load('Galão.png')
imagemFUNDO = pygame.image.load('Estrada.jpg')

LARGURA_JANELA = imagemFUNDO.get_width()
ALTURA_JANELA = imagemFUNDO.get_height()
LARGURA_CARRO = imagemF1.get_width()
ALTURA_CARRO = imagemF1.get_height()
LARGURA_GAS = imagemGAS.get_width()
ALTURA_GAS =  imagemGAS.get_height()
VEL = 6 
ITERACOES = 30 

pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA))
pygame.display.set_caption('imagens e som')
#dicionario
jogador = {
    'objRect': pygame.Rect(300, 100, LARGURA_CARRO,ALTURA_CARRO),
    'imagem': imagemF1,
    'vel': VEL
}

somAPASDECER = pygame.mixer.Sound('Efeito_som.mp3')
pygame.mixer.music.load('musica.mp3')

pygame.mixer.music.play(-1, 0.0)
somaAtivado = True
teclas = {
    'esquerda': False,
    'direita': False,
    'cima': False,
    'baixo': False
    }
contador = 0
GAS = []
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