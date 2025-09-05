import pygame
import sys

# Inicialização
pygame.init()
pygame.joystick.init()

# Criar uma janela mínima (necessário para eventos funcionarem corretamente em algumas plataformas)
pygame.display.set_mode((300, 200))
pygame.display.set_caption("Teste de Joystick")

# Verificar joystick
if pygame.joystick.get_count() == 0:
    print("Nenhum controle detectado.")
    pygame.quit()
    sys.exit()

# Inicializar primeiro controle
joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Controle detectado: {joystick.get_name()}")
print(f"Número de eixos: {joystick.get_numaxes()}")
print(f"Número de botões: {joystick.get_numbuttons()}")

# Loop de leitura dos eixos
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Leitura dos eixos
    for i in range(joystick.get_numaxes()):
        valor = joystick.get_axis(i)
        if abs(valor) > 0.1:
            print(f"Eixo {i}: {valor:.2f}")

    # Leitura dos botões
    for i in range(joystick.get_numbuttons()):
        if joystick.get_button(i):
            print(f"Botão {i} pressionado")

    clock.tick(30)  # Limita a 30 fps

pygame.quit()
