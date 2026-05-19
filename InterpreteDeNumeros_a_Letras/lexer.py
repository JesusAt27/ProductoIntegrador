import re

def lexer(codigo):
    patrones = [
        ('NUM',    r'\d+\.\d+|\d+'),
        ('SUMA',   r'\+'),
        ('RESTA',  r'-'),
        ('MULT',   r'\*'),
        ('DIV',    r'/'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('SKIP',   r'[ \t]+'), 
    ]
    
    tokens = []
    pos = 0
    while pos < len(codigo):
        match = None
        for tipo, patron in patrones:
            regex = re.compile(patron)
            match = regex.match(codigo, pos)
            if match:
                texto = match.group(0)
                if tipo != 'SKIP':
                    tokens.append((tipo, texto))
                pos = match.end()
                break
        if not match:
            raise SyntaxError(f"Carácter ilegal detectado en la posición {pos}: {codigo[pos]}")
    
    tokens.append(('EOF', '')) 
    return tokens