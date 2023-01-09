

print("\n****************Python Calculator*****************************")
def add (x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply (x,y):
    return x*y
def divide (x,y):
    return x/y
def potentially(x,y):
    return x**y
while True:
    print("\n Selecione o número da operação desejada \n")
    print("1-Soma")
    print("2-Subtração")
    print("3-multiplicação")
    print("4-Divisão")
    print("5-potenciação")

    escolha = input("\n digite sua opçao (1/2/3/4)")

    num1=int(input("\n digite o primeiro numero: "))
    num2=int(input("\n digite o segundo numero"))

    if escolha =='1':
        print("\n")
        print(num1,"+",num2,"=",add(num1,num2))
        print("\n")
        pergunta=int(input("deseja cuntinuar ? [1]sim [0]nao: "))
        if pergunta ==0:
            print("\n")
            print("obrigado pela perefencia")
            break
    if escolha =="2":
        print("\n")
        print(num1,"-",num2,"=",subtract(num1,num2))
        print("\n")
        pergunta=int(input("deseja cuntinuar ? [1]sim [0]nao: "))
        if pergunta ==0:
            print("\n")
            print("obrigado pela perefencia")
            break
    if escolha=="3":
        print("\n")
        print(num1,"*",num2,"=",multiply(num1,num2))
        print("\n")
        pergunta=int(input("deseja cuntinuar ? [1]sim [0]nao: "))
        if pergunta ==0:
            print("\n")
            print("obrigado pela perefencia")
            break
    if escolha=="4":
        print("\n")
        print(num1,"/",num2,"=",divide(num1,num2))
        print("\n")
        pergunta=int(input("deseja cuntinuar ? [1]sim [0]nao: "))
        if pergunta ==0:
            print("\n")
            print("obrigado pela perefencia")
            break
    if escolha=="5":
        print("\n")
        print(num1,"**",num2,"=",potentially())
        print("\n")
        pergunta=int(input("deseja cuntinuar ? [1]sim [0]nao: "))
        if pergunta ==0:
            print("\n")
            print("obrigado pela perefencia")
            break