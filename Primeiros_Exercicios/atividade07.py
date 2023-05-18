while True:
    print("Informe sua data de nascimento.")
    d = int(input("Dia: "))
    m = int(input("Mês: "))
    a = int(input("Ano: "))
    dias=0
    for dia in range(a):
        dias+=365
    for mes in range(m):
        dias+=30
    dias+=d
    anoA=738900.75
    print("Dias vividos:",anoA-dias,"\nDeseja fazer um novo cálculo?(1.Sim/2.Não)")
    opc=input("")
    if opc==2:
        break