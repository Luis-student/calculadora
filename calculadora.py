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
    



   





    

