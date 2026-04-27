'''


'''

class Celular:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100
    
    def fazer_chamada(self,custo_bateria):
        print(F"\n---Chamada no {self.modelo}---")
        try:
            self.bateria-=custo_bateria
        except TypeError:
            print("Erro: O custo da bateria deve ser um número!")
        else:
            print(f"Sucesso! Bateria atual: {self.bateria}%")
        finally:
            print("Sistema finalizado.")

meu_celular = Celular("Sansung","S24")
meu_celular.fazer_chamada("muito")#Teste de erro       
