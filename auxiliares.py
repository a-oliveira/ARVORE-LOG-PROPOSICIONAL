from arvore import *


def isConectivo(conect):
    if conect == "~" or conect == "-" or conect == "=" or conect == "^" or conect == "v":
        return True
    else:
        return False


def montarJson(raiz):
    if raiz is None:
        return
    json = raiz.toJson()
    if raiz.esquerda or raiz.direita:
        json['children'] = []
        if raiz.esquerda:
            json['children'].append(montarJson(raiz.esquerda))
        if raiz.direita:
            json['children'].append(montarJson(raiz.direita))

    return json


def criarArvore(formula):
    pilha = []
    arv = Arvore(None)
    subArv = None

    for simb in formula:
        if simb != ')':
            if simb == '(' and len(pilha) > 0 and pilha[len(pilha)-1] != '(':
                aux = pilha.pop()
                if isConectivo(aux):
                    novaRaiz = No(aux)
                    if subArv is not None:
                        novaRaiz.esquerda = subArv.raiz
                        arv.raiz = novaRaiz
                        subArv = arv
                    else:
                        arv.raiz = novaRaiz
                        subArv = arv
                    arv = Arvore(None)
                else:
                    pilha.append(aux)
            pilha.append(simb)

        elif simb == ')':
            tamPilha = len(pilha)
            while tamPilha > 0:
                if arv.raiz is None:
                    novaRaiz = No(pilha.pop())
                    arv.raiz = novaRaiz

                else:
                    simb = pilha.pop()
                    if simb == '(':
                        break
                    if isConectivo(simb):
                        if isConectivo(arv.raiz.chave):
                            if simb == '~':
                                novaRaiz = No(simb)
                                novaRaiz.esquerda = arv.raiz
                                arv.raiz = novaRaiz
                        else:
                            novaRaiz = No(simb)
                            filhoEsq = arv.raiz.esquerda
                            arv.raiz.esquerda = None
                            novaRaiz.esquerda = filhoEsq
                            novaRaiz.direita = arv.raiz
                            arv.raiz = novaRaiz

                    else:
                        if isConectivo(arv.raiz.chave):
                            if arv.raiz.esquerda is None:
                                filhoEsq = No(simb)
                                arv.raiz.esquerda = filhoEsq
                            else:
                                novaRaiz = No(simb)
                                novaRaiz.esquerda = arv.raiz
                                arv.raiz = novaRaiz

                tamPilha = tamPilha-1
                if subArv is None:
                    subArv = arv

            if subArv.raiz.chave == '~' and isConectivo(arv.raiz.chave):
                if subArv.raiz.esquerda is None:
                    subArv.raiz.esquerda = arv.raiz
                else:
                    arv.raiz.esquerda = subArv.raiz
                    subArv = arv
                arv = Arvore(None)

            if len(pilha) == 0 and subArv.raiz.direita is None:
                subArv.raiz.direita = arv.raiz
    return subArv
