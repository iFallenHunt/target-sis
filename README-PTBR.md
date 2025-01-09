[🇺🇸](https://github.com/iFallenHunt/target-sis/blob/main/README.md)

# Visão Geral do Projeto

Este projeto contém vários scripts em Python que realizam diferentes tarefas relacionadas a cálculos de receita e geração da sequência de Fibonacci.

## Descrições dos Arquivos

### 1. Valor da variável SOMA no final do processamento

Aqui, SOMA é inicializada como 0. O laço incrementa K até 13 e acumula o valor de K em SOMA. A soma será o total de 1 + 2 + 3 ... + 13.

### 2. Verificar se um número pertence à sequência de Fibonacci

`fib/fibonacci.py`

Este script gera a sequência de Fibonacci até um número especificado de termos. Ele também inclui uma função para verificar se um determinado número faz parte da sequência de Fibonacci gerada.

### 3. Faturamento diário de uma distribuidora

`fat/faturamento.py`

Este script processa dados de receita de arquivos JSON e XML. Ele combina os dados, filtra os dias com receita zero e calcula métricas como a menor e a maior receita diária, bem como os dias com receita acima da média mensal.

### 4. Porcentagem de faturamento por estado

`dis/estado_final.py`

Este script calcula a porcentagem da receita mensal por estado. Ele define um dicionário com dados de receita, calcula a receita total e, em seguida, calcula a contribuição percentual de cada estado para a receita total.

### 5. Inverter caracteres de uma string

`inv/inversao.py`
Este script inverte a ordem dos caracteres de uma string. Ele define uma função que recebe uma string como entrada e retorna a string com os caracteres invertidos.
