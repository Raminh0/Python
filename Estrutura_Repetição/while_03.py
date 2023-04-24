deseja="1"
cont= 3
n1=0
n2=0
while (deseja == "1") or (deseja==sim):
    while (n1 < 0) or (n1 > 10) and (cont != 0):
        n1 = float(input("Informe a nota da primeira avaliação (0 a 10): "))
        cont -= 1
        break
        while ((n2 < 0) or (n2 > 10)) and (cont != 0):
            n2 = float(input("Informe a nota segunda avaliação (0 a 10): "))
            cont -= 1
            break
        media = (n1 + n2) / 2
        print(f"O resultado da média é: {media:.1f}\n\nDeseja realizar um novo cálculo?(1-Sim - 2-Não)")
        deseja = input()
else:
    print("tchau.")
# Atualizar para tratar as notas individualmente
