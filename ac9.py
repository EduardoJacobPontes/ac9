# 1

distancia = int(input())


velocidade_x = 60  # em Km/h
velocidade_y = 90  # em Km/h

diferenca_velocidade = velocidade_y - velocidade_x

tempo_necessario = distancia / diferenca_velocidade

tempo_necessario_minutos = tempo_necessario * 60

# Imprime o resultado
print(f'{int(tempo_necessario_minutos)} minutos')


# 2

N = int(input())


fatorial = 1

for i in range(1, N + 1):
    fatorial *= i

print(fatorial)


# 3
def calcular_custo(lista_compras, precos):
    custo_total = 0
    for produto, quantidade in lista_compras.items():
        custo_total += quantidade * precos[produto]
    return custo_total

num_casos = int(input())

for _ in range(num_casos):
    
    num_produtos = int(input())
    precos = {}
    for _ in range(num_produtos):
        produto, preco = input().split()
        precos[produto] = float(preco)
    
    num_compras = int(input())
    lista_compras = {}
    for _ in range(num_compras):
        produto, quantidade = input().split()
        lista_compras[produto] = int(quantidade)

    custo_total = calcular_custo(lista_compras, precos)
    print(f'R$ {custo_total:.2f}')



# 4

tipo_real = int(input())
respostas = list(map(int, input().split()))

corretas = respostas.count(tipo_real)




print(corretas)


#5

competidores, folhas_compradas, folhas_por_competidor = map(int, input().split())

folhas_necessarias = competidores * folhas_por_competidor

if folhas_compradas >= folhas_necessarias:
    print('S')
else:
    print('N')


#6

N = int(input())

distancia_total = 0

for _ in range(N):

    tempo, velocidade_media = map(int, input().split())

    distancia_intervalo = velocidade_media * tempo
    
    distancia_total += distancia_intervalo

print(distancia_total)


#7

t = int(input())

m = 4 * t

print(m)



#8

N = int(input())

sequencia = [int(input()) for _ in range(N)]

marcados = 1 if N > 0 else 0
for i in range(1, N):
    if sequencia[i] != sequencia[i - 1]:
        marcados += 1

print(marcados)
