# criar uma classe de uma receita genérica


class Receita(): # class é a palavra para criar o objeto Receita é o nome do objeto (primeira letra maiuscula)

    def __init__(self, ingredientes, utensilios, preparo, porcao): # def _ _ init _ _ é o inicializador do objeto, self é palavra para criar o método
        self.ingredientes = ingredientes
        self.utensilios = utensilios
        self.preparo = preparo
        self.porcao = porcao

    def get_all(self): # com o get nós retornamos o que colocamos
        print("Para fazer está receita, é preciso de {}. Os utensílios necessários são {}. Para fazer a receita {}. Essa receita rende {}" .format(self.ingredientes, self.utensilios,self.preparo, self.porcao))

# aqui estou atribuindo os métodos da minha receita
comida = Receita("1 xícara de farinha, 1 ovo, azeite e sal a gosto", "tigela, garfo, colher, espátulo e frigideira", "coloque o ovo e leite na tigela, acrescente a farinha aos poucos para não empelotar. Coloco a frigideira no fogo, unte com azeite, coloque 2 colheres de sopa da massa e vire quando a massa estiver com as bordas douradas, deixe mais 2 minutos e retire" , "6 porções.")
comida.get_all()