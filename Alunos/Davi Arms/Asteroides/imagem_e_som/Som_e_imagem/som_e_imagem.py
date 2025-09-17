import pygame, random

imagemMegalodom = pygame.image.load('personagem.png')
imagemPeixe = pygame.image.load('alvo.png')
imagemFundo = pygame.image.load('fundo.png')
LARGURAJANELA = imagemFundo.get_width()
ALTURAJANELA = imagemFundo.get_height()
LARGURAMEGALODOM = imagemMegalodom.get_width()
ALTURAMEGALODOM = imagemMegalodom.get_height()
LARGURAPEIXE = imagemPeixe.get_width()
ALTURAPEIXE = imagemPeixe.get_width()
VEL = 5
ITERACOES = 30

pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption('Imagem e Som')

#dicionario
jogador = {
    'ObjRect': pygame.Rect(300, 100, LARGURAMEGALODOM, ALTURAMEGALODOM),
    'imagem': imagemMegalodom,
    'vel': VEL
}
print(LARGURAJANELA)
print(LARGURAPEIXE)
print(LARGURAMEGALODOM)
#configurando som 
somComer = pygame.mixer.Sound('comer.mp3')
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play(-1, 0.0)
somAtivado = True
teclas = {
    'esquerda': False,
    'direita': False,
    'cima': False,
    'baixo': False,
}
contador = 0
peixes =  []
deve_continuar = True
