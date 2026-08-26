#6) Faça um algoritmo que leia um número positivo e exiba se seu quadrado é ímpa
try:
 n = int(input('digite um número positivo: '))
 if 0 < n:
 q = n**2
 qi = q % 2 != 0
 qm = q % 11 == 0
 if qi and qm:
 print(f'o quadrado de {n} ({q}) é impar e múltiplo de 11!')
 else:
 print(f'o quadrado de {n} ({q}) não atende às duas condições')
 else:
 print('tem algo de errado com o seu número ou o número é menor/igual a 0')
except ValueError:
 print('tu errou algo chefe, digite apenas números inteiros')


#7) Escrever um algoritmo em Python que leia o Preço de uma mercadoria e exiba o
try:
 preco = float(input('digite o preço da mercadoria: '))
 opcao = input('digite "acréscimo" ou "desconto": ').strip().lower()
 e_acrescimo = opcao == 'acréscimo' or opcao == 'acrescimo'
 e_desconto = opcao == 'desconto'
 if e_acrescimo:
 novo_preco = preco + (preco * 0.03)
 print(f'preço com acréscimo de 3%: {novo_preco}')
 elif e_desconto:
 novo_preco = preco - (preco * 0.03)
 print(f'preço com desconto de 3%: {novo_preco}')
 else:
 print('opção inválida! digite acréscimo ou desconto')
except ValueError:
 print('tu errou algo chefe, digite apenas números no preço')


#9) Escrever um algoritmo em Python que determine a conversão entre as moedas: R
try:
 valor = float(input('digite a quantidade de dinheiro: '))
 print('1 - Real (R$) | 2 - Dólar (US$) | 3 - Libra (£)')
 origem = input('digite o número da moeda de origem: ')
 destino = input('digite o número da moeda de destino: ')
 if origem == '1':
 em_reais = valor
 elif origem == '2':
 em_reais = valor * 5.60
 elif origem == '3':
 em_reais = valor * 7.20
 else:
 em_reais = -1
 if em_reais == -1:
 print('opção de origem inválida!')
 elif destino == '1':
 print(f'resultado: R$ {em_reais:.2f}')
 elif destino == '2':
 resultado = em_reais / 5.60
 print(f'resultado: US$ {resultado:.2f}')
 elif destino == '3':
 resultado = em_reais / 7.20
 print(f'resultado: £ {resultado:.2f}')
 else:
 print('opção de destino inválida!')
except ValueError:
 print('tu errou algo chefe, digite apenas números no valor')


#11) Escrever um algoritmo que leia de apenas um (1) veículo de um estacionament
#➢ Hora de Saída: formato HH:MM
#➢ Valor pago a cada 30 Minutos: R$__?__ / 30 Minutos;
#E, exiba na tela o Total a Pagar (R$), levando em consideração:
#➢ Tolerância: Carência gratuita de 30 Minutos.
#➢ Considerar que o veículo não permutará no shopping. (Tempo de permanência ≤
try:
 h_in = int(input("digite a hora de entrada: "))
 m_in = int(input("digite os minutos de entrada: "))
 h_out = int(input("digite a hora de saída: "))
 m_out = int(input("digite os minutos de saída: "))
 valor_30min = float(input("digite o valor a cada 30 minutos: "))
 min_entrada = (h_in * 60) + m_in
 min_saida = (h_out * 60) + m_out
 if min_saida < min_entrada:
 min_saida = min_saida + 1440
 tempo_total = min_saida - min_entrada
 if tempo_total <= 30:
 total = 0.0
 else:
 sobra = tempo_total % 30
 if sobra > 0:
 blocos = (tempo_total // 30) + 1
 else:
 blocos = tempo_total // 30
 total = blocos * valor_30min
 print(f"total a pagar: R$ {total}")
except ValueError:
 print("tu errou algo chefe, digite apenas números")


 #12) Escrever um algoritmo em Python que leia a Massa (Quilos) e a Altura (Metro
try:
 massa = float(input('digite a massa (em kg): '))
 altura = float(input('digite a altura (em metros): '))
 if massa > 0 and altura > 0:
 imc = massa / (altura ** 2)
 if imc < 18.5:
 classificacao = 'Magreza'
 elif imc < 25:
 classificacao = 'Saudável'
 elif imc < 30:
 classificacao = 'Sobrepeso'
 elif imc < 35:
 classificacao = 'Obesidade Grau I'
 elif imc < 40:
 classificacao = 'Obesidade Grau II (Severa)'
 else:
 classificacao = 'Obesidade Grau III (Mórbida)'
 print(f'IMC: {imc:.2f}')
 print(f'Classificação: {classificacao}')
 else:
 print('massa e altura precisam ser maiores que zero!')
except ValueError:
 print('tu errou algo chefe, digite apenas números')







