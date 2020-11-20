class Arvore ():
    def __init__(self, raiz):
        self.raiz = raiz

    def imprimir(self):
        self.preOrdem(self.raiz)

    def preOrdem(self, no):
        if no is None:
            return
        print(no.chave)
        self.preOrdem(no.esquerda)
        self.preOrdem(no.direita)


class No ():
    def __init__(self, simbolo):
        self.chave = simbolo
        self.esquerda = None
        self.direita = None

    def toJson(self):
        json = {}
        json['name'] = self.chave
        json['size'] = [100, 100]
        return json
