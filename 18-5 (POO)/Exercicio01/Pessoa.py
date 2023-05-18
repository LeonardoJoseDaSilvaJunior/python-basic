class Pessoa:
    def __init__(self,nome,peso,idade,comendo =False):
        self.nome    = nome
        self.peso    = peso
        self.idade    = idade
        self.comendo = comendo

    def eat(self,alimento):

        if self.comendo == False:
            self.comendo = True
            print(f"{self.nome} está comendo {alimento}")
        else:
            print(f"{self.nome} Já está comendo!")
    def stopped_eating(self):
        if self.comendo == False:
            print(f"{self.nome} não está comendo ")
        else:
            print(f"{self.nome} parou de comer")
            self.comendo = False

    def to_speak(self):
        self.speak = True
        if self.comendo == True:
            print(f"{self.nome} não pode andar, pois está comendo!")
        elif self.walk == True:
            print(f"{self.nome} Caminha, equanto conversa")
        else:
            print(f"{self.nome} está falando")

    def stopped_talking(self):
        if self.speak == True:
            print(f"{self.nome} parou de conversar! ")
            self.speak = False
        else:
            print(f"{self.nome} não está conversando ")
    def to_walk_(self):
        if self.walk == False:
            print(f"{self.nome} está caminhando! ")
            self.walk = True
        else:
            print(f"{self.nome} já está caminhando! ")
    def stopped_Walking(self):
        if self.walk == False:
            self.walk = True
            print(f"{self.nome} parou de caminhar ")
        else:
            print(f"{self.nome} já parou de caminhar ")


print("PRIMEIRO OBJETO")
p1 = Pessoa("Leonardo",65,20)
print( p1.__dict__)
p2 = Pessoa("Maria",40,20)
print(vars(p2))
p1.eat("maça")

p1.to_speak()
p1.stopped_talking()
p1.stopped_eating()
p1.stopped_talking()
p1.stopped_eating()

