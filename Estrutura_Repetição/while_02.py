senha= input("Cadastro:\n\nCrie uma senha: ")
print("Senha caddastrada com sucesso!")
entrar=input("\n\n\nEntrar\n Informe sua senha: ")
cont= 2
while (senha != entrar) and (cont != 0): #and (novamente != senha):
    cont-=1
    print("Chance:",cont," para tentar novamente.")
    entrar= input("Senha incorreta!\n\nTente novamente.\n\n")
    break
print("Você conseguiu entrar CARAIOOOOOOOOOOO!")
