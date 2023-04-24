senha= input("Cadastro:\n\nCrie uma senha: ")
print("Senha caddastrada com sucesso!")
entrar=input("\n\n\nEntrar\n Informe sua senha: ")
cont= 2
while (senha != entrar) and (cont != 0):
    print(cont," Chance(s) para tentar novamente.")
    entrar= input("**Senha incorreta!\n---Tente novamente ou redefina sua senha.---\n\n")
    cont-=1
    break
if (senha == entrar):    
    print("Você conseguiu entrar! Bem vindo(a)!")
else:
    print("O número de tentativas de acesso foi atingido. É necessário redefinir sua senha!")
