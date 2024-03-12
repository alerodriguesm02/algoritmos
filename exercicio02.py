salario = float(input('Digite o salário em Reais(R$): '))
aumento = float(input('Digite o percentual de aumento do salário: '))/100

novo_sal = salario + (salario * aumento)

print(f'O valor do aumento é de: R${salario*aumento:8.2f}')
print(f'O novo salário é de: R${novo_sal:8.2f}')
