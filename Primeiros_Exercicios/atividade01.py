tipo= input("Informe o tipo de combustivel (G;gasolina R$ 5,80 / E;etanol R$ 4,90)")
if tipo in "GggasolinaEeetanol":
    litro= float(input("Infome quantos L você quer abastecer: "))
    if ((tipo == "G") or (tipo == "gasolina") or (tipo == "g")):
        valG= (5,80 * litro)
        print(f"O valor a ser pago é: R$ {valG:.2f}")
    elif (tipo in "Eeetanol"):
        valE= (4,90 * litro)
        print(f"O valor a ser pago é: R$ {valE:.2f}")
else:
  print("Informações invalidas!")
