
fluxo_tokens = ''
posicao = 1
fluxo_caracteres = input('Digite uma expressão: ')  
tamanho = len(fluxo_caracteres)
for i in range(0, tamanho):
    c = fluxo_caracteres[i]
    if c.isalpha():
        fluxo_tokens += "<id,"+str(posicao)+">"  

        print(fluxo_caracteres[i] ,f"Identificador {posicao}")
        posicao += 1

    elif c.isdigit():
        fluxo_tokens += "<{}>".format(c)
        print(fluxo_caracteres[i], "Número")
        
    elif c == '=':
        fluxo_tokens += "<{}>".format(c)        
        print(fluxo_caracteres[i], "Operador de atribuição")
    elif c == '*':
        print(fluxo_caracteres[i], "Operador aritmético MULT")
    # elif c == ' ': 
    elif c == '+':
        print(fluxo_caracteres[i], "Operador aritmético ADD")                        
    elif c == ';':
        print(fluxo_caracteres[i], "delimitador")
    elif c.isspace():                           
        pass                                    
    else:
        fluxo_tokens += '<erro>'                
# print(f'Entrada:\n{fluxo_caracteres}')
# print(f"Saída\nFluxo de tokens:\n{fluxo_tokens}")

