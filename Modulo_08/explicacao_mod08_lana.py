'''


'''

class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
    
    def buzinar (self):
        print(f'O{self.marca} da cor {self.cor} fez Bip Bip!')

meu_carro = Carro('Toyota', 'cinza')

carro_do_cliente = Carro('Honda', 'preto')

meu_carro.buzinar()

carro_do_cliente.buzinar()

# Exercício 2

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria
    
    def exibir_info(self):
        info_base = super().exibir_info()
        return f'{info_base}, Autonomia da bateria: {self.autonomia_bateria} km'
    
