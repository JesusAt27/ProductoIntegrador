class NodoNumero:
    def __init__(self, valor, texto):
        self.valor = valor
        self.texto = texto

    def evaluar(self):
        return self.valor, self.texto

    def mostrar_arbol(self, prefijo="", es_ultimo=True):
        print(prefijo + ("└── " if es_ultimo else "├── ") + f"NUM ({self.valor}) -> {self.texto}")


class NodoOpBinaria:
    def __init__(self, izq, op, der):
        self.izq = izq
        self.op = op
        self.der = der

    def evaluar(self):
        izq_val, izq_txt = self.izq.evaluar()
        der_val, der_txt = self.der.evaluar()
        
        if self.op == 'SUMA':
            return izq_val + der_val, f"{izq_txt} más {der_txt}"
        elif self.op == 'RESTA':
            return izq_val - der_val, f"{izq_txt} menos {der_txt}"
        elif self.op == 'MULT':
            return izq_val * der_val, f"{izq_txt} multiplicado por {der_txt}"
        elif self.op == 'DIV':
            if der_val == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            return izq_val / der_val, f"{izq_txt} dividido por {der_txt}"

    def mostrar_arbol(self, prefijo="", es_ultimo=True):
        print(prefijo + ("└── " if es_ultimo else "├── ") + f"OP_BINARIA ({self.op})")
        nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")
        self.izq.mostrar_arbol(nuevo_prefijo, False)
        self.der.mostrar_arbol(nuevo_prefijo, True)


class NodoOpUnaria:
    def __init__(self, op, nodo):
        self.op = op
        self.nodo = nodo

    def evaluar(self):
        val, txt = self.nodo.evaluar()
        if self.op == 'RESTA':
            return -val, f"menos {txt}"
        return val, txt

    def mostrar_arbol(self, prefijo="", es_ultimo=True):
        print(prefijo + ("└── " if es_ultimo else "├── ") + f"OP_UNARIA ({self.op})")
        nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")
        self.nodo.mostrar_arbol(nuevo_prefijo, True)