import os

data = [["Java How To Program", "Deitel & Deitel","2007"], ["Patterns of Enterprise Application Architecture","Martin Fowler","2002"],["Head First Design Patterns","Elisabeth Freeman","2004"],["Internet & World Wide Web: How to Program","Deitel & Deitel","2007"]]


def ord():
    select=''
    print("\n----------|ORDENAÇÃO|----------\n")
    while select!='1' or select!='2' or select!='3':    
        select = input("Título Ascendente [1] | Autor Ascendente, Título Descendente [2], Edição descendente, Autor descendente, Título ascendente [3] | sair [q] :")
        if select =='1':
            return sorted(data, key=lambda x:x[0])
            
        elif select=='2':
            return sorted(sorted(data,key=lambda x:x[0], reverse=True),key=lambda x:x[1])
            
        elif select=='3':
            return sorted(sorted(sorted(data,key=lambda x:x[0]),key=lambda x:x[1],reverse=True), key=lambda x:x[2], reverse=True)
        elif select =='q' or select=='Q':
            return main()
        else:    
            clear()
            print("-----Opção inválida------")

def save(titulo,autor,ano):
    data.append([titulo,autor,ano])

def cadastro():
    clear()
    print("----------|CADASTRO|----------\n")
    titulo = input("Título: ")
    autor = input("Autor: ")
    data = input("Data :")
    save(titulo,autor,data)
    select = ''
    while select!='1' or select!='2':    
        select = input("Novo cadastro[1] | sair[2]   :")
        if select=='1':
            return cadastro()
        elif select=='2':
            return main()
        else:
            print("Opção inválida")
        

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    select=''
    print("----------|SISTEMA DE CADASTRO|----------\n")
    while select!='1' or select!='2': 
        select = input ("Cadastrar [1] | Ordenar [2]    :")
        if select=='1':
            clear()
            return cadastro()
        elif select=='2':
            clear()
            return ord()
        else:
            print("Opção inválida")


if __name__=="__main__":
    print(main())

