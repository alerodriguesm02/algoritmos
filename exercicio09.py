altura_degrau = float(input('Digite a altura do degrau: '))
objetivo = float(input('Digite o seu objetivo em metros: '))

objetivo = objetivo*100

qtd_degraus = objetivo//altura_degrau

print(f'Quantidade de degraus é: {qtd_degraus}')
