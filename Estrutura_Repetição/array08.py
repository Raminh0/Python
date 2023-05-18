
log=[]
senha=[]

for i in range(4):
    print("--CRIAR CONTA-- ")
    log.append(input("Login: "))
    senha.append(input("Senha: "))
    cad=int(input("Deseja realizar mais um cadastro?\n"))
    if (cad == 1):
        break

for x in range(4):
    print("\n   --Cadastrados-- \n  Usuário ",x,"\nLogin: ",log[x],"\nSenha: ",senha[x])
    if (cad == 1):
        break