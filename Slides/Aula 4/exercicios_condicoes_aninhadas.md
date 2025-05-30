# 🎮 Lista de Exercícios – Condições Aninhadas em Python (Temática de Jogos)

## 1. Pontos de Vida
Um jogador começa com 100 pontos de vida. Se for atingido por um inimigo:
- Se o inimigo for um "zumbi", ele perde 10 pontos.
- Se for um "dragão", ele perde 50 pontos.
- Caso contrário, perde 5 pontos.

**Entrada:** tipo do inimigo  
**Saída:** pontos de vida restantes

---

## 2. Fase de Desbloqueio
Um jogo possui 3 fases. O jogador só pode jogar a próxima fase se tiver completado a anterior e tiver pelo menos 50 moedas.

**Entrada:** fase atual (1, 2 ou 3), fases completadas (True/False), moedas  
**Saída:** pode ou não jogar a próxima fase

---

## 3. Escolha do Personagem
O jogador escolhe uma classe ("guerreiro", "mago" ou "arqueiro") e uma arma.  
- Se for guerreiro, só pode usar espada.
- Se for mago, só pode usar cajado.
- Se for arqueiro, só pode usar arco.

**Entrada:** classe e arma escolhida  
**Saída:** mensagem indicando se a escolha é válida

---

## 4. Sistema de Pontuação
Um jogador ganhou 80 pontos em uma missão.  
- Se tiver mais de 50 pontos:
  - Se tiver menos de 70: "Bom trabalho"
  - Se tiver de 70 a 90: "Ótimo trabalho"
  - Se mais de 90: "Incrível!"

**Entrada:** pontos da missão  
**Saída:** avaliação do desempenho

---

## 5. Batalha Final
Se o jogador tem uma "espada mágica" e "escudo", ele pode lutar com o "chefe final".
- Caso tenha apenas um dos dois, ele precisa de um aliado.
- Se não tiver nenhum dos dois, não pode lutar.

**Entrada:** possui espada (True/False), possui escudo (True/False)  
**Saída:** mensagem indicando se pode lutar ou não

---

## 6. Modo de Jogo
No menu, o jogador pode escolher entre "fácil", "médio" ou "difícil".
- Se escolher difícil:
  - E se for experiente: "Desafio aceito!"
  - Caso contrário: "Recomenda-se começar no médio."

**Entrada:** nível escolhido, é experiente (True/False)  
**Saída:** mensagem de recomendação

---

## 7. Missão Secreta
Para acessar a missão secreta:
- O jogador precisa ter nível 10 ou mais.
- E também precisa ter a "chave dourada".
- Se tiver o nível, mas não a chave: "Procure a chave".
- Se tiver a chave, mas não o nível: "Você ainda não está pronto."

**Entrada:** nível do jogador, possui chave dourada (True/False)  
**Saída:** mensagem de acesso
