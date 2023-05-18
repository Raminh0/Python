opc=["Sim,","sim","SIM","1"]
medias=[]
while (opc == opc):
    n1 = (float(input("\nInforme a primeira nota: ")))
    n2 = (float(input("\nInforme a segunda nota: ")))
    media = 0

    media=(n1+n2)/2
    if media >= 7:
        print("Aprovado!")
    elif media >= 4:
        print("Recuperação...")
    else:
        print("Reprovado!")
    print("Deseja fazer uma nova verificação?(1.Sim/2.Não): ")
    opc=input()
    medias.append(media)