
input_user = input('Digite uma expressão: ')

texto_sem_espacos = input_user.replace(" ", "")
tamanho_sem_espacos = len(texto_sem_espacos)
quantidade_de_espacos = input_user.count(" ")
total = tamanho_sem_espacos + quantidade_de_espacos

print("1 - ", tamanho_sem_espacos)
print("2 - ", quantidade_de_espacos)
print("3 - ", total)
print("4 - ",texto_sem_espacos)
