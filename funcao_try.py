print(" * " * 35)
print("Meu Deus, me conceda sabedoria para poder estudar e absorver o conteudo aqui estudado.")
print(" * " * 35)

'''def add_elem(lista):
    """Adiciona um elemento à lista de nomes com segurança usando try/except."""
    try:
        elemento = (input("\nDigite um nome para adicionar à lista: ")).strip() # Digite um nome para adicionar à lista: Deus ► Por que não armazena os valores já adicionados anteriormente ? ► Aqui ela esta aceitando numbers, do tipo int (certo?)
        if not elemento and elemento == int: # ► Este if not elemento, seria: "Se não" elemento???como posso interpretar esta linhas de código de f orma correta?
            raise ValueError("\nErro: O nome não pode ser vazio.") #Digite um nome para adicionar à lista:Erro: O nome não pode ser vazio. ►Aqui esta funcionando...o que é este raise?
        
        #if elemento == int:
            raise ValueError("\nErro: Digite letras e vogais que formam palavras ou frases. ")
        
        lista.append(elemento)
        return lista
    except ValueError as e: # este parte do codigo é ligada ao try, correto?? mas por que o except esta retornando o valueError que o raise captou??? Quais suas relações, se tiver.. 
        print(f"{e}")
        return None
    finally: # ► Aqui eu percebi que funciona independente do numero ou texto digitado atender a condição do try...
        print("\nExecução finalizada.")

# Teste no VS Code # Cenário 1: Teste com entrada válida
nomes = []  
resultado = add_elem(nomes)
print(f"\nEsta é a minha lista atual:\n{nomes}")


# Cenário 2: Teste com entrada incorreta (vazia)
print("\n\nCenário 2: Tentar adicionar um nome vazio")
resultado = add_elem(nomes)
print("Resultado da lista:", resultado)
# Cenário 3: Teste com outra entrada válida após o erro
print("\n\nCenário 3: Adicionar outro nome válido (por exemplo, 'Ana')")
resultado = add_elem(nomes)
print("Resultado final da lista:", resultado)'''

#***********************************************
def menu(opcao1, opcao2):
    """Aqui eu crio uma função que vai direcionar meu programa para a execução especifica.
    Param1: Recebe a opção 1 que aplicara o metodo de limpeza por indice.
    Param2: Recebe a opção 2 que fará a remoção por elemento
    return: retorna a opção escolhida onde a lista em questão foi manipulada."""
    print(f"Escolha as opções que melhor for conveniente.")
    opcao1 = m_1
    opcao2 = m_2
    return opcao1, opcao2
        
def opcao1(metodo1):
    """Aqui eu crio uma função que vai receber um dado numerico representando o tipo de funcionalidade que fará que é o de remoção  pelo indice.
    Param1: recebe o método que será aplicado na remoção.
    return: Retorna a opção já trabalhada pelo metodo 1
    """
    opcao1 = metodo1
    return opcao1
     
def opcao2(metodo2):
    """Aqui eu crio uma função que vai receber um dado numerico representando o tipo de funcionalidade que fará que é o de remoção por elemento.
    Param1: recebe o método que será aplicado na remoção.
    return: Retorna a opção já trabalhada pelo metodo 1
    """
    opcao2 = metodo2
    return opcao2

def opcao3(metodo3):
    """Aqui eu crio uam função que chama o metodo 3 que é de acionar a interrupção do programa.
    Param1:"""
    opcao_3 = metodo3
    print(f"Você digitou 's', então programa se encerrará.")
    return metodo3

def metodo1(lista, metodo_pop, indice):
    """aqui eu crio uma função que recebe uma lista e a limpa pelo indice. 
    Utilizo o bloco try para manter a segurança e integridade dos dados da função.
    Param1: Recebe uma lista cujo elemento será removido pelo indice.
    Param2: Armazena o item removido.
    Param3: Recebe o indice que será usado para remoção
    """
    try:
       
        metodo_pop = opcao1
        indice =  int(input("Você gostaria de remover por qual indice?")).strip()

        if not metodo_pop.isdigit():
            raise ValueError("Digite dígitos ( 0 - 9 )")
        metodo_pop= lista.pop(indice)  
        print(f"Você escolheu o método 1 e a remoção foi feita.\nO item removido é:{metodo_pop}")
        opcao1 = metodo1
    except ValueError as e:
        print(f"Erro: Digite entradas válidas. {e}")
    finally:
        print(f"Finalizando remoção pelo índice")
    return metodo1, lista
    
def metodo2(lista, metodo2, elemento):
    """aqui eu crio uma função que recebe uma lista e a limpa pelo nome do elemento. 
    Utilizo o bloco try para manter a segurança e integridade dos dados da função.
    Param1: Recebe uma lista cujo elemento será removido pelo nome.
    Param2: Armazena o item removido.
    Param3: Recebe o elemento que será removido
    """
    try:
        elemento = input("Qual elemento c deseja remover?").strip()
        metodo2 = opcao2
        if not metodo2.isdigit():
            raise ValueError("Digite dígitos ( 0 - 9 )")
        metodo2 = lista.remove(elemento)  
        opcao2 = metodo2
        print(f"Você escolheu o método 2 e a remoção foi feita.\n")
        opcao2 = metodo2
    except ValueError as e:
        print(f"Erro: Digite entradas válidas. {e}")
    finally:
        print(f"Finalizando remoção pelo índice")
    return metodo2, lista

def metodo3(s, S):
    """aqui eu crio uma função que encerra o menu interativo
    Recebe como parametro 2 strings
    Param1: Recebe a string 's'
    Param2: Recebe a string 'S'
    """
    try:
        sair = input("você deseja realmente sair?")
        if sair == str:
            if not sair.isalpha():
                raise ValueError("Erro: O encerramento \"somente\" acontecerá se você apertar 's'.")
        return sair
    except ValueError as e:
        print(f"Erro: {e}")
    finally:
        print("Menu se encerrando.")
    return None

lista_tarefas = ["Cozinhar", "Limpar a casa", "Lavar o quintal", "Limpar o banheiro"]

lista_tarefas = opcao1(metodo1)

lista_tarefas = opcao2(metodo2)

m_1 = 0
m_2 = 0
sair = None
indice = 0
elemento = ''

while True:
    opcao = input("Há 2 métodos de limpeza. Se for indice digite 1 - m_1 - , se for por elemento, digite -m_2 -. Para sair, digite 's' para sair.").strip()
   
    if opcao == m_1:
        m_1 = metodo1(lista_tarefas, metodo1, indice)
    
    elif opcao == m_2:
        m_2 = metodo2([], metodo2, elemento) 

    elif opcao == sair:
        print("Voce encerrou o menu. Flws!!!")
    else:
        print("Até mais!!!")
        break
 
