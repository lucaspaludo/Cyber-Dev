import pygame, random
imagemPersonagem = pygame.image.load("personagem.png")
imagemSushi = pygame.image.load("comida.png")
imagemFundo = pygame.image.load("fundo.png")
LARGURA_JANELA = imagemFundo.get_width()
ALTURA_JANELA = imagemFundo.get_height()
LARGURA_PERSONAGEM = imagemPersonagem.get_width()
ALTURA_PERSONAGEM = imagemPersonagem.get_height()
LARGURA_SUSHI = imagemSushi.get_width()
ALTURA_SUSHI = imagemSushi.get_height()
VEL = 6
ITERACOES = 30

pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("Imagem e Som")
#dicionário
jogador = {
    'objRect': pygame.Rect(300, 100,LARGURA_PERSONAGEM, ALTURA_PERSONAGEM),
    'imagem': imagemPersonagem,
    'vel': VEL
}
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
print(LARGURA_JANELA)
print(LARGURA_PERSONAGEM)
print(LARGURA_SUSHI)

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
                    pygame.mixer.music.play(-1,0.0)
                    somAtivado = True
                    


    