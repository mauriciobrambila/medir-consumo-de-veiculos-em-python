print
listaCarro = []
listaConsumo = []

while len(listaCarro) < 3:
    listaCarro.append(input(f"\nDigite marca/modelo de veiculo:" ))
    listaConsumo.append(float(input('Digite o consumo do carro (km/L):')))
  
results = ''
valor_gas = 4.90
total_km = 500
for j, c in enumerate(listaCarro):
    print('Veiculo {}'.format(j+1))
    print('Nome: {}'.format(c))
    print('Km por litro: {}\n'.format(listaConsumo[j]))

    consumo_l = round(total_km/listaConsumo[j], 2)
    results += 'O carro {} consume {}L e custará $R{} quando fizer {}km\n'.format(c, consumo_l, round(consumo_l*valor_gas, 2), total_km)

print('O carro mais económico é o {}'.format(listaCarro[listaConsumo.index(max(listaConsumo))])) 
print(results)