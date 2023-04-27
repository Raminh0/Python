
logs=[]
senhas=[]

for i in range(4):
    print("--CRIAR CONTA-- ")
    logs.append(input("Login: "))
    senhas.append(input("Senha: "))
    cad=int(input("Deseja realizar mais um cadastro?\n"))
    if (cad == 1):
        break

for x in range(4):
    print("\n   --Cadastrados-- \n  Usuário ",x,"\nLogin: ",log[x],"\nSenha: ",senha[x])
    if (cad == 1):
        break

print("  ---Plataforma---\nEntre com sua conta.")
log=input("Login: ")
senha=input("Senha: ")
cont=0
for x in range(4):

    if ((log==logs[x]) and (senha==senhas)):
        print("Você conseguiu entrar!")
        break
    else:
        cont+=1
print("Senha incorreta.\nTente novamente.")
