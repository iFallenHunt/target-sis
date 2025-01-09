def gerar_fibonacci(n):
    """
    Gera a sequência de Fibonacci até o enésimo termo.
    :param n: Número de termos da sequência a serem gerados
    :return: Lista contendo a sequência de Fibonacci
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    sequencia = [0, 1]
    for i in range(2, n):
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


def esta_na_fibonacci(numero, sequencia):
    """
    Verifica se um número está na sequência de Fibonacci gerada.
    :param numero: Número a ser verificado
    :param sequencia: Lista com a sequência de Fibonacci
    :return: True se o número está na sequência, False caso contrário
    """
    return numero in sequencia


# Exemplo de uso
n_termos = int(input(
    "Quantos termos da sequência de Fibonacci você quer gerar? "))
numero_para_verificar = int(input("Informe o número que deseja verificar: "))

sequencia_fibonacci = gerar_fibonacci(n_termos)
print("Sequência gerada:", sequencia_fibonacci)

if esta_na_fibonacci(numero_para_verificar, sequencia_fibonacci):
    print(f"O número {numero_para_verificar} está na sequência de "
          "Fibonacci gerada.")
else:
    print(
        f"O número {numero_para_verificar} não está na sequência de "
        "Fibonacci gerada."
    )
