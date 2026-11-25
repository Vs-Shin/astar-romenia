from mapa import mapa_romenia, heuristica_bucareste

print('Quantidade de cidades no mapa:', len(mapa_romenia))
print('Quantidade de valores de h(n):', len(heuristica_bucareste))

vizinhos_arad = mapa_romenia['Arad']
print()
print('Vizinhos de Arad:', vizinhos_arad)
print('Tipo do valor:', type(vizinhos_arad))

primeira = vizinhos_arad[0]
print()
print('Primeira estrada que sai de Arad:', primeira)
print('  posição [0] -> cidade vizinha:', primeira[0])
print('  posição [1] -> custo em km   :', primeira[1])

print()
print('Estradas que saem de Arad:')
for vizinho, custo in mapa_romenia['Arad']:
    print('  Arad ->', vizinho, '=', custo, 'km\n')

for cidade in mapa_romenia:
    quantidade = len(mapa_romenia[cidade])
    print(f' {cidade:<15} {quantidade} estrada(s)')

print()
print('h(Arad) =', heuristica_bucareste['Arad'], 'km em linha reta até Bucareste')
print('Para cada vizinho de Arad: custo da estrada e h(vizinho)')
for vizinho, custo in mapa_romenia['Arad']:
    h = heuristica_bucareste[vizinho]
    print(f' {vizinho:<10} estrada = {custo:>3} km h = {h:>3} km')

