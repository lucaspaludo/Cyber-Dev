import pygame

class Lutador():
    def __init__(self, jogador, x, y, flip, dados, spritesheet, etapas_animacao, som_ataque):
        self.jogador = jogador
        self.tamanho = dados[0]
        self.image_scale = dados[1]
        self.offset = dados[2]
        self.flip = flip
        self.lista_animacao = self.carregar_sprites(spritesheet, etapas_animacao)
        self.acao = 0 #0: idle, 1: run, 2: jump, 3: attack1, 4: attack2, 5: hit, 6: death
        self.frame_index = 0
        self.image = self.lista_animacao[self.acao][self.frame_index]
        self.update_time = pygame.time.get_ticks() 
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.correndo = False
        self.pulando = False
        self.atacando = False
        self.tipo_ataque = 0
        self.golpe = False
        self.ataque_cooldown = 0
        self.som_ataque = som_ataque
        self.vida = 100
        self.vivo = True
    
    def carregar_sprites(self, spritesheet, etapas_animacao):
        #extrarindo sprites de uma spritesheet
        lista_animacao = []
        for y, animacao in enumerate(etapas_animacao):
            temp_img_list  = []
            for x in range(animacao):
                temp_img = spritesheet.subsurface(x * self.tamanho, y * self.tamanho, self.tamanho, self.tamanho)
                
                temp_img_list.append(pygame.transform.scale(temp_img, (self.tamanho * self.image_scale, self.tamanho * self.image_scale)))
            lista_animacao.append(temp_img_list)

        return lista_animacao

    def mover(self, largura_janela, altura_janela, janela, alvo, fim_de_jogo):
        VEL = 10
        GRAVIDADE = 2
        dx = 0
        dy = 0
        self.correndo = False
        self.tipo_ataque = 0

        #capturando teclas pressionadas
        tecla = pygame.key.get_pressed()

        #apenas um ataque por vez
        if self.atacando == False and self.vivo == True and fim_de_jogo == False:
            #checando teclas para jogador 1
            if self.jogador == 1:
                #movimento
                if tecla[pygame.K_a]:
                    dx = -VEL
                    self.correndo = True
                    
                if tecla[pygame.K_d]:
                    dx = VEL
                    self.correndo = True

                #pulo
                if tecla[pygame.K_w] and self.pulando == False:
                    self.vel_y = -30
                    self.pulando = True 
                
                #ataques
                if tecla[pygame.K_r] or tecla[pygame.K_t]:

                    self.ataque(alvo)
                    #determinando o tipo de ataque
                    if tecla[pygame.K_r]:
                        self.tipo_ataque = 1
                    if tecla[pygame.K_t]:
                        self.tipo_ataque = 2

            #checando teclas para jogador 2
            if self.jogador == 2:
                #movimento
                if tecla[pygame.K_LEFT]:
                    dx = -VEL
                    self.correndo = True
                    
                if tecla[pygame.K_RIGHT]:
                    dx = VEL
                    self.correndo = True

                #pulo
                if tecla[pygame.K_UP] and self.pulando == False:
                    self.vel_y = -30
                    self.pulando = True 
                
                #ataques
                if tecla[pygame.K_KP1] or tecla[pygame.K_KP2]:

                    self.ataque(alvo)
                    #determinando o tipo de ataque
                    if tecla[pygame.K_KP1]:
                        self.tipo_ataque = 1
                    if tecla[pygame.K_KP2]:
                        self.tipo_ataque = 2

        #gravidade
        self.vel_y += GRAVIDADE
        dy += self.vel_y
        
        #verificando se o jogador está dentro da janela
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > largura_janela:
            dx = largura_janela - self.rect.right
        if self.rect.bottom + dy > altura_janela - 110:
            self.vel_y = 0
            self.pulando = False
            dy = altura_janela - 110 - self.rect.bottom
        
        #verificando para que os lutadores se virem um para o outro
        if alvo.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True
        
        #atualizando cooldown do ataque
        if self.ataque_cooldown > 0:
            self.ataque_cooldown -= 2

        #atualizando posição do retângulo
        self.rect.x += dx
        self.rect.y += dy

    #atualizando animação
    def update(self):
        #checando qual ação o lutador está realizando
        if self.vida <= 0:
            self.vida = 0
            self.vivo = False
            self.atualizar_acao(6) #morte
        elif self.golpe == True:
            self.atualizar_acao(5) #levando golpe
        elif self.atacando == True:
            if self.tipo_ataque == 1:
                self.atualizar_acao(3) #ataque 1
            elif self.tipo_ataque == 2:
                self.atualizar_acao(4) #ataque 2
        elif self.pulando == True:
            self.atualizar_acao(2) #pulo
        elif self.correndo == True:
            self.atualizar_acao(1) #correndo
        else:
            self.atualizar_acao(0) #idle
        animation_cooldown = 50
        #atualiza imagem
        self.image = self.lista_animacao[self.acao][self.frame_index]
        #checando se tempo suficiente passou desde a última atualização
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        #checando se a animação terminou
        if self.frame_index >= len(self.lista_animacao[self.acao]):
            #checando se o lutador morreu e finalizando a animação
            if self.vivo == False:
                self.frame_index = len(self.lista_animacao[self.acao]) - 1
            else:
                self.frame_index = 0
                #checanado se o ataque terminou
                if self.acao == 3 or self.acao == 4:
                    self.atacando = False
                    self.ataque_cooldown = 20
                #checando se elevou um golpe
                if self.acao == 5:
                    self.golpe = False
                    #se o lutador estiver no meio de um ataque, interrompe o ataque
                    self.atacando = False
                    self.ataque_cooldown = 20

    def ataque(self, alvo):
        if self.ataque_cooldown == 0:
            #executa ataque
            self.atacando = True
            self.som_ataque.play()
            ataque_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
            if ataque_rect.colliderect(alvo.rect):
                alvo.vida -= 10
                alvo.golpe = True
          
    def atualizar_acao(self, nova_acao):
        #checando se a nova ação é diferente da anterior
        if nova_acao != self.acao:
            self.acao = nova_acao
            #atualizando o frame index
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def desenhar(self, janela):
        img = pygame.transform.flip(self.image, self.flip, False)
        janela.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))

        