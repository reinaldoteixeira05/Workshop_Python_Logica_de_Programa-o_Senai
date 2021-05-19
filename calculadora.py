def calcular():
    print("Bem Vindo a Calculadora do Workshop Python")
    num_1= int(input('Digite um numero : ')) 
    operacao = input('''
Escolha sua operação:
+ para somar 
- para subtrair
* para multiplicar
/ para dividir 
''')
    num_2= int(input('Digite um numero : ')) 
    
    if operacao == '+':
        res=(num_1+num_2)
        print('{}+{}={} '.format(num_1,num_2,res) )
    elif operacao == '-':
        res=(num_1-num_2)
        print('{}-{}={} '.format(num_1,num_2,res))
    elif operacao == '*':
        res=(num_1*num_2)
        print('{}*{}={} '.format(num_1,num_2,res))
    elif operacao == '/':
        if  num_1 ==0 or num_2 ==0 :
            print('{}/{}= '.format(num_1,num_2))
            print(0)  
        if num_1 !=0 and num_2 !=0:
            res=(num_1/num_2)
            print('{}/{}={} '.format(num_1,num_2,res))
        else:
            print('Opção invalida')
            calcular()
    reiniciar()
            
def reiniciar():
    retornar = input('''
Calular novamente 
Digite 1 para reiniciar
Digite 2 para sair: ''' )
    if retornar=='1':
        calcular()
    elif retornar=='2':
        print('Ate mais...')


calcular()