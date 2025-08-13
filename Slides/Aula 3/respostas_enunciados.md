# 🧠 Respostas dos Exercícios com Temática de Jogos

---

## 🎯 Exercício 1 — Adivinhe o Número
```python
import random

numero_secreto = random.randint(1, 10)
chute = int(input("Tente adivinhar o número de 1 a 10: "))

if chute == numero_secreto:
    print("🎉 Parabéns! Você acertou.")
else:
    print(f"❌ Errou! O número era {numero_secreto}.")
```

---

## ⌛ Exercício 2 — Jogo da Reação Rápida
```python
import time
import random

print("Prepare-se...")
time.sleep(random.randint(2, 5))
print("AGORA! Pressione Enter!")

inicio = time.time()
input()
fim = time.time()

tempo_reacao = fim - inicio
print(f"⏱️ Seu tempo de reação foi {tempo_reacao:.2f} segundos.")

if tempo_reacao < 0.5:
    print("⚡ Rápido como um raio!")
else:
    print("🐢 Você pode treinar mais sua velocidade.")
```

---

## 🎲 Exercício 3 — Jogo de Dados
```python
import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
soma = dado1 + dado2

print(f"Você rolou {dado1} e {dado2}. Soma = {soma}")

if soma == 7 or soma == 11:
    print("🎉 Você venceu!")
else:
    print("😕 Tente novamente.")
```

---

## 🪙 Exercício 4 — Cara ou Coroa
```python
import random

escolha = input("Escolha cara ou coroa: ").lower()
resultado = random.choice(["cara", "coroa"])

print(f"O resultado foi: {resultado}")

if escolha == resultado:
    print("✅ Acertou!")
else:
    print("❌ Errou!")
```

---

## 👾 Exercício 5 — Vida do Jogador
```python
vida = int(input("Digite seus pontos de vida (0 a 100): "))

if vida == 100:
    print("💪 Você está no máximo!")
elif vida >= 50:
    print("🛡️ Você ainda está bem.")
elif vida > 0:
    print("⚠️ Cuidado! Vida baixa.")
else:
    print("💀 Game Over.")
```

---
