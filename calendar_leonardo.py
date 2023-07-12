#Solicita ao usuário que informe o número de dias do mês e armazena na variável.
num_dias_mes = int(input('Informe o número de dias do mês: '))
#Laço de repetição para continuar solicitando ao usuário sempre que digitar um valor que não seja entre 28 e 31.
while num_dias_mes < 28 or num_dias_mes > 31:
    num_dias_mes = int(input('VALOR INVÁLIDO Informe o número de dias do mês: '))


#Solicita ao usuário que informe um dia da semana e armazena na variável.
num_dias_sem = int(input('Informe o dia da semana: '))
#Laço de repetição para continuar solicitando ao usuário sempre que digitar um valor que não seja entre 1 e 7.
while num_dias_sem < 1 or num_dias_sem > 7:
    num_dias_sem = int(input('VALOR INVÁLIDO Informe o dia da semana: '))

x = 1

#Imprimi os dias da semana de Domingo a Sábado
print('DOM SEG TER QUA QUI SEX SAB')

#Verifica se o dia da semana é maior que 1, para que assim imprima os espaços a partir de Segunda.
if num_dias_sem > 1:
    #Imprimi os espaços no Calendário.
    print(f'{(num_dias_sem-1) * "    "}', end='')
    #Laço de repetição para imprimir os dias do mês. 
for x in range(1, num_dias_mes + 1): 
    print(f'{x:02}', end='  ')
    num_dias_sem += 1
    #Verifica se o dia da semana é maior que 7(Sábado), para que a variável receba o valor 1(Domingo), assim voltando a imprimir os dias do mês no Domingo.
    if num_dias_sem > 7:
        num_dias_sem = 1
        print()




    






    

        