#funções para as operações basicas 
def soma(a, b):
    som = a + b 
    return som

def subtracao(a, b):
    sub = a - b 
    return sub

def multiplicacao(a, b):
    mult = a * b 
    return mult 

def divisao(a, b):
    div = a / b 
    return div 


#funcao da calculadora 
def calculadora(a, b, c):
    if c == "+":
        return soma(a, b)
    
    elif c == "-" : 
        return subtracao(a, b) 

    elif c == "*":
        return multiplicacao(a, b)

    elif c == "/":
        return divisao(a, b) 
  
while True: 
    print("=====CALCULADORA=====")

    num1 = int(input('insira o primeiro numero: '))
    operacao = input("escolha a operação(+, -, *, /): ")
    num2 = int(input('insira o segundo numero: '))


    valor = calculadora(num1, num2, operacao)
    print(valor)

    sair = input("deseja continuar (sim/nao): ")
    if sair == "nao":
        break
