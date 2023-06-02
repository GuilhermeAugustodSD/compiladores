import re

# Expressão regular para cada tipo de token
token_patterns = [
    (r'\d+\.\d+', 'número real'), 
    (r'\d+', 'número natural'),       
    (r'\+', 'operador de soma'),           
    (r'\-', 'operador de subtração'),           
    (r'\*', 'operador de multiplicação'),          
    (r'\/', 'operador de divisão'), 
    (r'\(', 'abre parênteses'),       
    (r'\)', 'fecha parênteses'),        
]

# Função para analisar a expressão
def analisar(expressao):
    tokens = []
    pos = 0
    while pos < len(expressao):
        match = None
        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(expressao, pos)
            if match:
                valor = match.group(0)
                tokens.append((valor, token_type))
                pos = match.end()
                break
        if not match:
            print(f"Caractere inválido: '{expressao[pos]}'")
            pos += 1
    return tokens

# Testando a função
expressao = input("Digite uma expressão: ")
tokens_analisados = analisar(expressao)
for valor, token_type in tokens_analisados:
    print(valor, '=>', token_type)