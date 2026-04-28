'''
Eercicio pático: simule um carregamento de um smartfone, quando estiver a 5%, quando estiver 
85% avise que esta carregado

'''

class celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
        self.bateria = 100
    
    def ligar(self):
        self.ligado = True
        print(f'{self.modelo} está ligado.')

    def carregar(self):
        self.bateria = 100
        print(f'{self.modelo} está carregado.') 

meu_celular = celular('Apple', 'Iphone 16')
meu_celular.ligar()
meu_celular.bateria = 5
print(f'{meu_celular.modelo} está com {meu_celular.bateria}% de bateria.')

