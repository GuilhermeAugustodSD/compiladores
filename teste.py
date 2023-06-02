fluxo_tokens = ''
posicao = 1
fluxo_caracteres = input('Digite uma expressão: ')
tamanho = len(fluxo_caracteres)
op_count = 0  # contador de operadores
op_limit = 2  # limite de operadores
op_mult_count = 0  # contador de operadores de multiplicação
op_mult_limit = 1  # limite de operadores de multiplicação
var_count = 0  # contador de variáveis

i = 0
while i < tamanho:
    c = fluxo_caracteres[i]

    if c.isalpha():
        # Verifica se há uma variável seguida por espaço em branco
        if i < tamanho - 1 and fluxo_caracteres[i + 1].isspace():
            print(f"Erro: Foram encontradas duas variáveis seguidas e separadas por espaço em branco: {c} {fluxo_caracteres[i + 1]}")
            break

        fluxo_tokens += "<id," + str(posicao) + ">"
        print(f"Identificador {posicao}: {c}")
        posicao += 1
        var_count += 1

    elif c.isdigit():
        fluxo_tokens += "<{}>".format(c)
        print(f"Número: {c}")

    elif c == '=':
        fluxo_tokens += "<{}>".format(c)
        print("Operador de atribuição")

    elif c == '+':
        if i < tamanho - 1 and fluxo_caracteres[i + 1] == '*':
            print(f"Erro: Foram encontrados dois operadores seguidos: {c} {fluxo_caracteres[i + 1]}")
            break
        print("Operador aritmético ADD")
        op_count += 1

    elif c == '*':
        if op_mult_count >= op_mult_limit:
            print(f"Erro: Foram encontrados mais de {op_mult_limit} operadores de multiplicação na expressão de três endereços")
            break
        print("Operador aritmético MULT")
        op_mult_count += 1
        op_count += 1

    elif c == '/':
        if op_count >= op_limit:
            print(f"Erro: Foram encontrados mais de {op_limit} operadores na expressão de três endereços")
            break
        print("Operador aritmético DIV")
        op_count += 1

    elif c == ';':
        print("Delimitador")

    elif c.isspace():
        pass

    else:
        print("Erro: Caractere desconhecido")
        break

    i += 1
return 0

# Verifica se a expressão está correta
if var_count > 1 and op_count > 1:
    if op_count > op_limit:
        print(f"Erro: Foram encontrados mais de {op_limit} operadores na expressão de três endereços")
    if op_mult_count > op_mult_limit:
        print(f"Erro: Foram encontrados mais de {op_mult_limit} operadores de multiplicação na expressão de três endereços")
    print("Erro: Foram encontrados mais de um operando e operador antes do enunciado de atribuição.")

print(f"Saída\nFluxo de tokens:\n{fluxo_tokens}")
