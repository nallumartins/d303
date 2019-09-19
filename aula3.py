# criar uma classe de uma receita genérica


class Receita(): # class é a palavra para criar o objeto Receita é o nome do objeto (primeira letra maiuscula)

    def __init__(self, ingredientes, utensilios, preparo, porcao): # def _ _ init _ _ é o inicializador do objeto, self é palavra para criar o método
        self.ingredientes = ingredientes
        self.utensilios = utensilios
        self.preparo = preparo
        self.porcao = porcao

    def get_all(self): # com o get nós retornamos o que colocamos
        print(" Ingredientes: {}\n Utensílios: {}\n Preparo:{}\n Rendimento: {}\n" .format(self.ingredientes, self.utensilios,self.preparo, self.porcao))

# aqui estou instanciando, colocando atributos aos métodos
comida = Receita("1 xícara de farinha, 1 ovo, azeite e sal a gosto", "tigela, garfo, colher, espátulo e frigideira", " mistura tudo e coloca na frigideira" , "6 porções.")
comida.get_all()

class Doce(Receita):

    def __init__(self, ingredientes, utensilios, preparo, porcao):
        self.ingredientes = ingredientes
        self.utensilios = utensilios
        self.preparo = preparo
        self.porcao = porcao

    def brigadeiro(self):
        print (" Ingredientes: {}\n Utensílios: {}\n Preparo: {}\n Porção: {}\n" .format(self.ingredientes, self.utensilios, self. preparo, self.porcao))

docinho = Doce("Leite Condensado e chocolate", "panela e colher", "colocar ingredientes na panela e misturar", "30 brigadeiros")
docinho.brigadeiro()    
    