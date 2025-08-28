#cd Imagem e som
import pygame, random

ImagemFundo = pygame.image.load('fundo.jpg')
Imagemplayer = pygame.image.load('ImagemNinja.png')
ImagemPlayer = pygame.image.load('ImagemNinja(1).png')
ImagemSword = pygame.image.load('sword.png')


PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)
LARGURAJANELA = 1000
ALTURAJANELA = 700
VEL = 6
ITERACOES = 10
AlturaBlock= 50
LarguraBlock = 80
LP = Imagemplayer.get_width()
AP = Imagemplayer.get_height()
LS = ImagemSword.get_width()
AS = ImagemSword.get_height()
ImagemPlayer = pygame.transform.scale(Imagemplayer and ImagemPlayer, (70, 70))
ImagemSword = pygame.transform.scale(ImagemSword, (LarguraBlock, AlturaBlock))
ImagemFundo = pygame.transform.scale(ImagemFundo, (LARGURAJANELA, ALTURAJANELA))


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



pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Imagem e Som")

jogador = {
    'objRect' : pygame.Rect(500 , 554, 60, 60),
    'cor' : VERDE,
    'vel' : VEL,
    'imagemF' : ImagemPlayer,
    'imagemT' : ImagemPlayer
}
pygame.mixer.init()
SomMusic = pygame.mixer.Sound('morrer.mp3')
pygame.mixer.music.load("music_fundo.mp3")
pygame.mixer.music.play(-1, 0, 0)
somAtivado = True

teclas = {
    'esquerda' : False,
    'direita' : False,
    'cima' : False,
    'baixo' : False,
}
contador = 0
Sword = []
deve_continuar = True

while deve_continuar :
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False
        if evento.type == pygame.KEYDOWN :
            if evento.key == pygame.K_ESCAPE:
               deve_continuar = False
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
               teclas['esquerda'] = True
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
               teclas['direita'] = True
            # if evento.key == pygame.K_UP or evento.key == pygame.K_w:
            #    teclas['cima'] = True
            # if evento.key == pygame.K_DOWN or evento.type == pygame.K_s:
            #    teclas['baixo'] = True
        if evento.type == pygame.KEYUP:
           if evento.key ==  pygame.K_LEFT or evento.key == pygame.K_a:
              teclas['esquerda'] = False
           if evento.key  == pygame.K_RIGHT or evento.key == pygame.K_d:
              teclas['direita'] = False  
           if evento.key == pygame.K_UP or evento.key == pygame.K_w:
              teclas['cima'] = False
           if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
              teclas['baixo'] = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
           Sword.append({
              'objRect': pygame.Rect(evento.pos[0], evento.pos[1], 80, 50),
              'vel': 1 
                                
           })
   
    contador += 1
    if contador >= ITERACOES:
       contador = 0
       posX = random.randint(1, LARGURAJANELA - LarguraBlock) 
       posY = -AlturaBlock
       velRandom = random.randint(1, VEL+3)
       Sword.append({
           'objRect': pygame.Rect(posX, posY, LarguraBlock, AlturaBlock),
           'cor': BRANCO,
           'vel': velRandom,
           'imagem' : ImagemSword
       })
    
    janela.blit(ImagemFundo, (0, 0))
    moverJogador(jogador, teclas, (LARGURAJANELA, ALTURAJANELA))
    janela.blit(jogador['imagemF'], jogador["objRect"]) 
   
    for bloco in Sword[:]:
       bateu = jogador['objRect'].colliderect(bloco['objRect'])
       if bateu or bloco['objRect'].y > LARGURAJANELA:
           Sword.remove(bloco)
    for bloco in Sword:
      moverBloco(bloco)
      janela.blit(ImagemSword, bloco["objRect"])
   

    pygame.display.update()
    relogio.tick(40)

pygame.quit()              
