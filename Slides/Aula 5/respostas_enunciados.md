# Respostas dos Exercícios

## 1. Pontuação do Jogador
```python
total = 0
for i in range(5):
    pontos = int(input(f"Digite a pontuação da partida {i+1}: "))
    total += pontos
print("Pontuação total:", total)
```

## 2. Contador de Vidas
```python
vidas_perdidas = 0
for i in range(10):
    resposta = input(f"Perdeu uma vida no turno {i+1}? (sim/não): ")
    if resposta.lower() == 'sim':
        vidas_perdidas += 1
print("Total de vidas perdidas:", vidas_perdidas)
```

## 3. Multiplicador de Pontos
```python
total = 0
for i in range(5):
    pontos = int(input(f"Pontos coletados no nível {i+1}: "))
    total += pontos * 2
print("Total com bônus:", total)
```

## 4. Fases Completas
```python
total_fases = 0
for dia in range(7):
    fases = int(input(f"Fases completas no dia {dia+1}: "))
    total_fases += fases
print("Total de fases na semana:", total_fases)
```

## 5. Lista de Inimigos
```python
for i in range(5):
    inimigo = input(f"Nome do inimigo {i+1}: ")
    print(inimigo, "- Derrotado")
```

