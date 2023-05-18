qtEle=int(input("Quantidade de eleitores: "))
vtB=int(input("Qtd votos em branco: "))
vtN=int(input("Qtd votos nulo: "))
vtV=int(input("Qtd de votos válidos: "))

vtB = (vtB * qtEle)/100
vtN = (vtN *qtEle)/100
vtV = (vtV *qtEle)/100
print("\nPorcentagem dos votos: \n\n%Brancos:",vtB,"\n\n%Nulos:",vtN,"\n\n%Validos:",vtV)