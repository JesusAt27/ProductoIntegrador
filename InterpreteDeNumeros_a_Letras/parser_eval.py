from traductor import numero_a_letras
from nodos import NodoNumero, NodoOpBinaria, NodoOpUnaria

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.token_actual = self.tokens[self.pos]

    def avanzar(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.token_actual = self.tokens[self.pos]

    def consumir(self, tipo_esperado):
        if self.token_actual[0] == tipo_esperado:
            self.avanzar()
        else:
            raise SyntaxError(f"Se esperaba {tipo_esperado} pero se encontró {self.token_actual[0]}")

    def factor(self):
        token = self.token_actual
        
        if token[0] == 'LPAREN':
            self.consumir('LPAREN')
            nodo = self.expresion()
            self.consumir('RPAREN')
            return nodo
            
        elif token[0] == 'RESTA':
            self.consumir('RESTA')
            nodo = self.factor()
            return NodoOpUnaria('RESTA', nodo)
        elif token[0] == 'SUMA':
            self.consumir('SUMA')
            return self.factor()
        elif token[0] == 'NUM':
            val = float(token[1])
            texto = numero_a_letras(val)
            self.consumir('NUM')
            return NodoNumero(val, texto)
        raise SyntaxError(f"Sintaxis inválida. Se esperaba un número o '(' pero se halló: {token[0]}")

    def termino(self):
        nodo_izq = self.factor()
        while self.token_actual[0] in ('MULT', 'DIV'):
            op = self.token_actual[0]
            self.avanzar()
            nodo_der = self.factor()
            nodo_izq = NodoOpBinaria(nodo_izq, op, nodo_der)
        return nodo_izq

    def expresion(self):
        nodo_izq = self.termino()
        while self.token_actual[0] in ('SUMA', 'RESTA'):
            op = self.token_actual[0]
            self.avanzar()
            nodo_der = self.termino()
            nodo_izq = NodoOpBinaria(nodo_izq, op, nodo_der)
        return nodo_izq