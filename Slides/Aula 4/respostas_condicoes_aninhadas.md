# ✅ Respostas dos Exercícios – Condições Aninhadas

## 1. Pontos de Vida
```python
vida = 100
inimigo = input("Digite o tipo de inimigo: ")

if inimigo == "zumbi":
    vida -= 10
elif inimigo == "dragão":
    vida -= 50
else:
    vida -= 5

print(f"Pontos de vida restantes: {vida}")
```

## 2. Fase de Desbloqueio
```python
fase = int(input("Fase atual: "))
completou = input("Completou a fase anterior? (s/n): ") == "s"
moedas = int(input("Quantidade de moedas: "))

if completou and moedas >= 50:
    print("Pode jogar a próxima fase.")
else:
    print("Não pode jogar a próxima fase.")
```

## 3. Escolha do Personagem
```python
classe = input("Escolha a classe: ")
arma = input("Escolha a arma: ")

if classe == "guerreiro":
    if arma == "espada":
        print("Escolha válida!")
    else:
        print("Guerreiro só pode usar espada.")
elif classe == "mago":
    if arma == "cajado":
        print("Escolha válida!")
    else:
        print("Mago só pode usar cajado.")
elif classe == "arqueiro":
    if arma == "arco":
        print("Escolha válida!")
    else:
        print("Arqueiro só pode usar arco.")
```

## 4. Sistema de Pontuação
```python
pontos = int(input("Pontos obtidos: "))

if pontos > 50:
    if pontos < 70:
        print("Bom trabalho")
    elif pontos <= 90:
        print("Ótimo trabalho")
    else:
        print("Incrível!")
else:
    print("Continue tentando!")
```

## 5. Batalha Final
```python
espada = input("Tem espada mágica? (s/n): ") == "s"
escudo = input("Tem escudo? (s/n): ") == "s"

if espada and escudo:
    print("Pode lutar com o chefe final!")
elif espada or escudo:
    print("Você precisa de um aliado para lutar.")
else:
    print("Não pode lutar com o chefe final.")
```

## 6. Modo de Jogo
```python
modo = input("Escolha o modo (fácil, médio, difícil): ")
experiente = input("Você é experiente? (s/n): ") == "s"

if modo == "difícil":
    if experiente:
        print("Desafio aceito!")
    else:
        print("Recomenda-se começar no médio.")
else:
    print(f"Você escolheu o modo {modo}. Boa sorte!")
```

## 7. Missão Secreta
```python
nivel = int(input("Nível do jogador: "))
chave = input("Tem a chave dourada? (s/n): ") == "s"

if nivel >= 10:
    if chave:
        print("Acesso liberado à missão secreta!")
    else:
        print("Procure a chave.")
else:
    if chave:
        print("Você ainda não está pronto.")
    else:
        print("Suba de nível e encontre a chave.")
```
