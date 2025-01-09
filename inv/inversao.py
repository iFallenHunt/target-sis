# Passo 1: Entrada da string
entrada = input("Digite uma string: ")

# Passo 2: Inversão da string
string_invertida = ""
for char in entrada:
    string_invertida = char + string_invertida

# Passo 3: Saída
print("String invertida:", string_invertida)
