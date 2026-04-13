'''


'''

print('\n Calculadora simples - Python Vocação\n')

numb_hum = input('Digite o primeiro número:') 
numb_dois = input('Digite o segundo número:') 
print('')
# result = numb_hum + numb_dois
# result = int(numb_hum) + int(numb_dois)
operar_numb = input('Escolha a operação: 1-> +, 2->  -, 3-> *,4-> /') 

if operar_numb == '1':
  result = int(numb_hum) + int(numb_dois)
  print(f'O resultado é: {result}')
  
elif operar_numb == '2':
  result = int(numb_hum) - int(numb_dois)
  print (f'O resultado é: {result}')

elif operar_numb == '3':
  result = int(numb_hum) * int(numb_dois) 
  print (f'O resultado é: {result}')

elif operar_numb == '4':
  result = int(numb_hum) / int(numb_dois)   
  print (f'O resultado é: {result}')

else:
  print('Número não válido, tente novamente!')
