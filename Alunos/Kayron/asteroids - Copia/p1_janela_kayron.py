import pygame

Preto = (0, 0, 0)
Branco = (255, 255, 255)
Vermelho = (255, 0, 0)
Verde = (0, 255, 0)
Azul = (0, 0, 255)

PI = 3.1416
pygame.init()
janela = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Figuras e texto")
janela.fill(Branco)

fonte = pygame.font.Font(None, 48)
texto = fonte.render("Ola mundo", True,Branco,Azul)
janela.blit(texto, [50,150])

pygame.draw.line(janela, Verde, (60, 260), (420, 260), 4)
pygame.draw.polygon(janela, Preto, ((191, 206), (236, 277), (156, 277)),0)
pygame.draw.circle(janela, Azul, (300, 50), 20, 0)
pygame.draw.ellipse(janela, Vermelho, (400, 250, 40, 80), 0)
pygame.draw.rect(janela, Verde, (20, 20, 60, 40), 0)
pygame.draw.arc(janela, Vermelho, [250, 75, 150, 125], PI/2.3*PI/2,2)
pygame.draw.arc(janela, Preto, [250, 75, 150, 125], PI/2, PI/2,2)

pygame.display.update()
continuar = True
while continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuar = False

pygame.quit()


