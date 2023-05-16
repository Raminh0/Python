from MinhaBF import Preco
A=input("Nome do produto: ")
B=int(input("Quantidade no estoque: "))
C=float(input("Preço (Un): "))

produto= Preco(A,B,C)
valor=produto[1]
print(f"\nDescrição do produto: {A}\nValor Total (R$):{valor}")
