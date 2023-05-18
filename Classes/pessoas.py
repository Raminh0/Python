
#Classes
class Pessoas:
    #Metodos:
    def __init__ (self,nome,peso,idade,comendo = False,falando = False,andando = False):

        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.andando = andando
    def comer(self, comida):

        if self.comendo == False:
            self.comendo = True
            self.comida= comida

            print(f'\n{self.nome} está comendo {self.comida}\n')
        else:
            print(f'***Não pode, {self.nome} já está comendo {self.comida}!\n')

    def pararDeComer(self):

        if self.comendo == True:
            self.comendo = False
            print(f'-{self.nome} parou de  comer')

    def falar(self,palavra):
        if self.falando == False:
            self.falando = True
            self.palavra = palavra

            print(f'\n{self.nome} está falando {self.palavra}\n')
        else:
            print(f'***Não pode, {self.nome} já está falando {self.palavra}!\n')

    def pararDeFalar(self):

        if self.falando == True:
            self.falando = False
            print(f' -{self.nome} parou de falar')

    def andar(self,passo):
        if self.andando == False:
            self.andando = True
            self.passo = passo

            print(f'\n{self.nome} está andando, ele deu {self.passo} passos\n')
        else:
            print(f'***Não pode, {self.nome} já está andando {self.passo} passos!\n')

    def pararAndar(self):

        if self.andando == True:
            self.andando = False
            print(f' -{self.nome} parou de andar')
#Objetos:
p1= Pessoas("Inajá",68.54,23)
p2= Pessoas("Raminnho",70,30)

p1.comer("feijão")
p2.comer("arroz")
p1.comer("sorvete")
p2.comer("sorvete")
p1.pararDeComer()
p1.falar("Abracadabra")
p2.falar("zinsalabrim")
p1.falar("Abracadabra")
p2.falar("zinsalabrim")
p1.pararDeFalar()
p2.pararDeFalar()
p1.andar(3)
p2.andar(5)
p1.andar(3)
p2.andar(5)
p1.pararAndar()
p2.pararAndar()