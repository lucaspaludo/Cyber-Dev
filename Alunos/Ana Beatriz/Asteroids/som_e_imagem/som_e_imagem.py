import pygame, random

imagemAlegria = pygame.image.load("alegria.png")
imagemBola = pygame.image.load("bola.png")
imagemFundo = pygame.image.load("fundo.png")
LARGURA_JANELA = imagemFundo.get_width()
ALTURA_JANELA = imagemFundo.get_height()
LARGURA_ALEGRIA = imagemAlegria.get_width()
ALTURA_ALEGRIA = imagemAlegria.get_height()
LARGURA_BOLA = imagemBola.get_width()
ALTURA_BOLA = imagemBola.get_height()
VEL = 6
ITERACOES = 20

def moverjogador(jogador, teclas, dim_janela):
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
    if teclas['baixo']and jogador['objRect'].bottom < borda_inferior:
        jogador['objRect'].y += jogador['vel']
    
def moverBola(Bola):
    Bola['objRect'].x += Bola['vel']

pygame.init()
relogio = pygame.time.Clock()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("Imagem e Som")

jogador = {
    'objRect': pygame.Rect(300, 100, LARGURA_ALEGRIA, ALTURA_ALEGRIA),
    'imagem': imagemAlegria,
    'vel': VEL
}
print(LARGURA_JANELA)
print(LARGURA_BOLA)
print(LARGURA_ALEGRIA)

somPegar = pygame.mixer.Sound("pegar.mp3")
pygame.mixer.music.load("musicaFundo.mp3")
pygame.mixer.music.play(-1, 0.0)
somAtivado = True
teclas = {
    'esquerda': False,
    'direita': False,
    'cima': False,
    'baixo': False
}
contador = 0
Bolas = []
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
            Bolas.append({
                'objRect': pygame.Rect(evento.pos[0], evento.pos[1], LARGURA_BOLA, LARGURA_BOLA),
                'imagem': imagemBola,
                'vel': VEL - 3
            })
    contador += 1
    if contador > ITERACOES:
        contador = 0
        posY = random.randint(0, LARGURA_JANELA - LARGURA_BOLA)
        posX = -LARGURA_BOLA
        velRandom = random.randint(VEL - 3, VEL + 3)
        Bolas.append({
            'objRect': pygame.Rect(posX, posY, LARGURA_BOLA, ALTURA_BOLA),
            'imagem': imagemBola,
            'vel': velRandom
        })
    janela.blit(imagemFundo, (0, 0))
    moverjogador(jogador, teclas, (LARGURA_JANELA, ALTURA_JANELA))
    janela.blit(jogador['imagem'], jogador['objRect'])

    for Bola in Bolas[:]:
        comeu = jogador['objRect'].colliderect(Bola['objRect'])
        if comeu and somAtivado:
            somPegar.play()
        if comeu or Bola['objRect'].x > LARGURA_JANELA:
            Bolas.remove(Bola)
    
    for Bola in Bolas:
        moverBola(Bola)
        janela.blit(Bola['imagem'], Bola['objRect'])

    pygame.display.update()
    relogio.tick(40)
pygame.quit()

    