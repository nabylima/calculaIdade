contador = 2023
nome = str(input('Qual seu nome completo?: '))
ano = int(input('Qual o ano do seu nascimento?: '))

while contador == 2023:
  if ano < 1922 or ano > 2022:
    print('Esse ano não está na nossa base de Cáculo')
    ano = int(input('Qual o ano do seu nascimento?: '))
  else: 
    idade = contador - ano
    print('Ano válido! Sua idade é:', idade, 'anos')
    break