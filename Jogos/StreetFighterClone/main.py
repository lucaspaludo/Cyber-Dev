from pathlib import Path
import sys
import pygame
from pygame import mixer
from lutador import Lutador

mixer.init()
pygame.init()

#criando janela
LARGURA_JANELA = 1000
ALTURA_JANELA = 600

janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("Street Fighter Clone")

#definindo fps
relogio = pygame.time.Clock()
FPS = 60

#definindo cores
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

#definindo variáveis do jogo
intro_count = 3
last_count_update = pygame.time.get_ticks()
pontuacao = [0, 0] #pontuação dos jogadores
fim_de_jogo = False
FIM_DE_JOGO_COOLDOWN = 2000


#definindo variáveis dos lutadores
TAMANHO_GUERREIRO = 162
ESCALA_GUERREIRO = 4
OFFSET_GUERREIRO = [72, 56]
DADOS_GUERREIRO = [TAMANHO_GUERREIRO, ESCALA_GUERREIRO, OFFSET_GUERREIRO]
TAMANHO_MAGO = 250
ESCALA_MAGO = 3
OFFSET_MAGO = [112, 107]
DADOS_MAGO = [TAMANHO_MAGO, ESCALA_MAGO, OFFSET_MAGO]

def resource_path(*parts: str) -> str:
    """Funciona no Python normal e no exe do PyInstaller."""
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).parent))
    return str(base.joinpath(*parts))

pygame.mixer.music.load(resource_path("assets", "audio", "music.mp3"))
espada_som = pygame.mixer.Sound(resource_path("assets", "audio", "sword.wav"))
magia_som  = pygame.mixer.Sound(resource_path("assets", "audio", "magic.wav"))

# imagens
imagemFundo   = pygame.image.load(resource_path("assets", "images", "background", "background.jpg")).convert_alpha()
guerreiroSheet= pygame.image.load(resource_path("assets", "images", "warrior", "Sprites", "warrior.png")).convert_alpha()
magoSheet     = pygame.image.load(resource_path("assets", "images", "wizard", "Sprites", "wizard.png")).convert_alpha()
imagemVitoria = pygame.image.load(resource_path("assets", "images", "icons", "victory.png")).convert_alpha()

# fontes
count_font = pygame.font.Font(resource_path("assets", "fonts", "turok.ttf"), 80)
score_font = pygame.font.Font(resource_path("assets", "fonts", "turok.ttf"), 30)

#carregando música de fundo e efeitos sonoros
#pygame.mixer.music.load("assets/audio/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000) #loop infinito

#espada_som = pygame.mixer.Sound("assets/audio/sword.wav")
espada_som.set_volume(0.5)

#magia_som = pygame.mixer.Sound("assets/audio/magic.wav")
magia_som.set_volume(0.75)


#carregando imagem background
#imagemFundo = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

#carregando spritesheets
#guerreiroSheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
#magoSheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()

#carregando imagem de vitória
#imagemVitoria = pygame.image.load("assets/images/icons/victory.png").convert_alpha()

#desenhando imagem de fundo
def desenha_fundo():
    imagemFundoRedim = pygame.transform.scale(imagemFundo, (LARGURA_JANELA, ALTURA_JANELA))
    janela.blit(imagemFundoRedim, (0, 0))

#definindo número de etapas em cada animação
ETAPAS_ANIMCACAO_GUERREIRO = [10, 8, 1, 7, 7, 3, 7]
ETAPAS_ANIMACAO_MAGO = [8, 8, 1, 8, 8, 3, 7]

#definindo fonte
#count_font = pygame.font.Font('assets/fonts/turok.ttf', 80)
#score_font = pygame.font.Font('assets/fonts/turok.ttf', 30)

#desenhando texto
def desenha_texto(texto, fonte, cor, x, y):
    img = fonte.render(texto, True, cor)
    janela.blit(img, (x, y))

#desenhando vida dos lutadores
def desenha_barra_vida(vida, x, y):
    proporcao_vida = vida / 100
    pygame.draw.rect(janela, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(janela, RED, (x, y, 400, 30))
    pygame.draw.rect(janela, YELLOW, (x, y, 400 * proporcao_vida, 30))

#criando instâncias dos dois lutadores
lutador_1 = Lutador(1, 200, 310, False, DADOS_GUERREIRO, guerreiroSheet, ETAPAS_ANIMCACAO_GUERREIRO, espada_som)
lutador_2 = Lutador(2, 700, 310, True, DADOS_MAGO, magoSheet, ETAPAS_ANIMACAO_MAGO, magia_som)

#game loop
deve_continuar = True
while deve_continuar:

    relogio.tick(FPS)

    #desenhando fundo
    desenha_fundo()

    #desenhando estatísticas dos lutadores
    desenha_barra_vida(lutador_1.vida, 20, 20)
    desenha_barra_vida(lutador_2.vida, 580, 20)
    desenha_texto(f"P1: {str(pontuacao[0])}", score_font, RED, 20, 60)
    desenha_texto(f"P2: {str(pontuacao[1])}", score_font, RED, 580, 60)

    #atualizando contagem inicial
    if intro_count <= 0:
        #movendo lutadores
        lutador_1.mover(LARGURA_JANELA, ALTURA_JANELA, janela, lutador_2, fim_de_jogo)
        lutador_2.mover(LARGURA_JANELA, ALTURA_JANELA, janela, lutador_1, fim_de_jogo)
    else:
        #desenhando contagem
        desenha_texto(str(intro_count), count_font, RED, LARGURA_JANELA//2, ALTURA_JANELA//3)
        #atualizando contagem
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()
        
    #atualizando ações dos lutadores
    lutador_1.update()
    lutador_2.update()

    #desenhando lutadores
    lutador_1.desenhar(janela)
    lutador_2.desenhar(janela)

    #checando se o jogador foi derrotado
    if fim_de_jogo == False:
        if lutador_1.vivo == False:
            pontuacao[1] += 1
            fim_de_jogo = True
            fim_de_jogo_tempo = pygame.time.get_ticks()
        elif lutador_2.vivo == False:
            pontuacao[0] += 1
            fim_de_jogo = True
            fim_de_jogo_tempo = pygame.time.get_ticks()
    else:
        #desenhando imagem de vitória
        janela.blit(imagemVitoria, (360, 150))
        if pygame.time.get_ticks() - fim_de_jogo_tempo > FIM_DE_JOGO_COOLDOWN:
            fim_de_jogo = False
            intro_count = 4
            lutador_1 = Lutador(1, 200, 310, False, DADOS_GUERREIRO, guerreiroSheet, ETAPAS_ANIMCACAO_GUERREIRO, espada_som)
            lutador_2 = Lutador(2, 700, 310, True, DADOS_MAGO, magoSheet, ETAPAS_ANIMACAO_MAGO, magia_som)


    #checagem de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False


    #atualizando a tela
    pygame.display.update()

#fechando pygame
pygame.quit()



