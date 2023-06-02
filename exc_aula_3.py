erro = False
fluxo_caracteres = input('Digite uma expressão: ')  

def lexa(fluxo_caracteres):
    fluxo_tokens = ''
    posicao = 1
    tamanho = len(fluxo_caracteres)
    qtd_operadores = 0
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
            qtd_operadores += 1
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


# Verificar se a expressão possui duas variáveis antes do "="
if fluxo_caracteres.count('=') == 1:
    left_side, right_side = fluxo_caracteres.split('=')
    left_side_variables = sum([c.isalpha() for c in left_side])
    right_side_variables = right_side.split()

    right_side = right_side.strip()
    operands = ["+", "-", "*", "/"]
    count_operands = 0
    count_operators = 0
    error = False
    for i in range(len(right_side_variables) - 1):
        if right_side_variables[i].isalpha() and right_side_variables[i+1].isalpha():
            print("Erro: Foram encontradas duas variáveis seguidas e separadas por espaço em branco:", right_side_variables[i],"e", right_side_variables[i + 1])
            error = True
            break
        if right_side_variables[i] in operands and right_side_variables[i + 1] in operands:
            print("Erro: Foram encontrados dois operadores seguidos, separados por espaço em branco.", right_side_variables[i],"e", right_side_variables[i + 1] )
            error = True
            break

    for char in right_side:
        if char in operands:
            count_operators += 1
        elif char.isalpha() or char.isdigit():
            count_operands += 1
        if count_operands >= 3 and count_operators >= 2:
            print("Erro: Foram encontrados mais de três operandos e mais de dois operadores na expressão de três endereços.")
            error = True
            break

    for i in range(len(right_side) - 1):
        if right_side[i] in operands and right_side[i + 1] in operands:
            print("Erro: Foram encontrados dois operadores seguidos, separados por espaço em branco.")
            error = True
            break

   
    if left_side_variables == 2:
        print("Erro: Foram encontradas duas variáveis antes do sinal de igual.")
        error = True
    if error:
        exit
    else:
        print("Expressão válida.")
        lexa(fluxo_caracteres)

else:
    print("Erro: A expressão deve conter um sinal de igual.")




