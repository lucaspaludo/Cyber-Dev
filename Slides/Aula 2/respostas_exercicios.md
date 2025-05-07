
# 💻 Respostas dos Exercícios

## 1. Calculadora do Guerreiro
```python
forca = int(input("Digite os pontos de FORÇA ganhos: "))
agilidade = int(input("Digite os pontos de AGILIDADE ganhos: "))
inteligencia = int(input("Digite os pontos de INTELIGÊNCIA ganhos: "))

total = forca + agilidade + inteligencia

print(f"Total de pontos distribuídos: {total}")
```

---

## 2. Batalha de Dano Crítico
```python
dano_base = float(input("Digite o dano base do ataque: "))
multiplicador = float(input("Digite o multiplicador de dano: "))

dano_total = dano_base * multiplicador

print(f"O dano total causado foi: {dano_total:.2f}")
```

---

## 3. Cálculo de Vida Perdida
```python
vida_inicial = int(input("Digite a vida inicial do jogador: "))
ataque1 = int(input("Dano do primeiro ataque: "))
ataque2 = int(input("Dano do segundo ataque: "))
ataque3 = int(input("Dano do terceiro ataque: "))

vida_restante = vida_inicial - (ataque1 + ataque2 + ataque3)

print(f"Vida restante após os ataques: {vida_restante}")
```
---

## 4. Poção de Experiência
```python
experiencia_inicial = int(input("Digite a experiência inicial do personagem: "))

experiencia_final = experiencia_inicial * (2 ** 4)

print(f"Experiência após 4 poções: {experiencia_final}")
```
---

## 5. Divisão de Ouro
```python
ouro_total = int(input("Quantas moedas de ouro vocês encontraram? "))
membros = int(input("Quantos membros há no grupo? "))

por_membro = ouro_total // membros
sobra = ouro_total % membros

print(f"Cada membro recebe: {por_membro} moedas")
print(f"Sobraram {sobra} moedas para o cofre da guilda")
```

## 6. Raiz do Enigma
```python
numero = int(input("Digite o núemro do enigma: "))
raiz = numero**(1/2)

print(f"A raíz quadrada de {numero} é {raiz:.2f}")
```
