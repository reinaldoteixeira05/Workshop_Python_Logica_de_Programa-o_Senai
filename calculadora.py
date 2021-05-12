def calcular():
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
        print('{}+{}= '.format(num_1,num_2) )
        print(num_1+num_2)
    elif operacao == '-':
        print('{}-{}= '.format(num_1,num_2))
        print(num_1-num_2)
    elif operacao == '*':
        print('{}*{}= '.format(num_1,num_2))
        print(num_1*num_2)
    elif operacao == '/':
        if  num_1 ==0 or num_2 ==0 :
            print('{}/{}= '.format(num_1,num_2))
            print(0)  
        if num_1 !=0 and num_2 !=0:
            print('{}/{}= '.format(num_1,num_2))
            print(num_1/num_2) 
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