from auxiliares import *
import json

if __name__ == "__main__":
    formula = "(~(pvq)-r)"
    #formula = "((pvq)-r)"
    #formula = "(r-(pvq))"
    #formula = "((p^q)-(rvh))"
    arv = criarArvore(formula)
    arv.imprimir()
    arvJson = montarJson(arv.raiz)
   # print(json.dumps(arvJson, indent=1))
