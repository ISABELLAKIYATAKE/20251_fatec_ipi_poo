import calculadora

# Definindo as Boas-Vindas
def bem_vindo():
    print('''
!!!Bem-Vindos a Calculadora!!!
    ''')

# Função para validar a entrada de números
def obter_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

# Função para validar a entrada da operação
def obter_operacao():
    while True:
        operacao = input('''
Por gentileza, digite a operação matemática desejada:
+ para somar
- para subtrair
* para multiplicar
/ para dividir
Operação: ''')

        if operacao in ['+', '-', '*', '/']:
            return operacao
        else:
            print('Opção inválida. Tente novamente.')

# Definindo a função calcular()
def calcular():
    # Chamar a função de boas-vindas
    bem_vindo()

    # Solicitar os números ao usuário
    numero_1 = obter_numero('Digite o primeiro número: ')
    numero_2 = obter_numero('Digite o segundo número: ')

    # Solicitar a operação ao usuário
    operacao = obter_operacao()

    # Realizar a operação selecionada
    if operacao == '+':
        print('{} + {} = {}'.format(numero_1, numero_2, numero_1 + numero_2))
    elif operacao == '-':
        print('{} - {} = {}'.format(numero_1, numero_2, numero_1 - numero_2))
    elif operacao == '*':
        print('{} * {} = {}'.format(numero_1, numero_2, numero_1 * numero_2))
    elif operacao == '/':
        if numero_2 == 0:
            print("Erro: Divisão por zero!")
        else:
            print('{} / {} = {}'.format(numero_1, numero_2, numero_1 / numero_2))

    # Perguntar se o usuário quer calcular de novo
    de_novo()

# Definindo a função de_novo() para perguntar se o usuário quer usar a calculadora outra vez
def de_novo():
    # Dar input para o usuário
    calc_de_novo = input('''
    Você quer calcular de novo?
    Digite S para SIM ou N para NÃO
    Resposta: ''')

    # Se o usuário digitar S, a função calcular() irá rodar outra vez
    # Aceita 's' ou 'S' adicionando a string.upper()
    if calc_de_novo.upper() == 'S':
        calcular()
    # Se o usuário digitar N, a função dirá "Tchau Tchau!!!" para o usuário e encerrará o programa
    # Aceita 'n' ou 'N' adicionando a string.upper()
    elif calc_de_novo.upper() == 'N':
        print('Tchau Tchau!!!')
    # Se o usuário digitar outra coisa, irá rodar a função de novo
    else:
        print('Opção inválida. Tente novamente.')
        de_novo()

# Chamar a função calcular() para iniciar o programa
calcular()
