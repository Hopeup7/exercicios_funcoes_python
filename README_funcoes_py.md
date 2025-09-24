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
 

Você pode colocar o comando %reset -f diretamente em uma célula do Jupyter Notebook, como se estivesse executando um código normal.
💡 Passos para limpar todas as variáveis:
1️⃣ Crie uma nova célula no Jupyter Notebook.
2️⃣ Digite:     %reset -f

3️⃣ Execute a célula (Shift + Enter).
✅ Isso apagará todas as variáveis da memória do Jupyter Notebook!
🔹 Se quiser limpar via terminal, no modo interativo do Python (IPython ou Jupyter Console), também pode usar %reset—mas o mais comum é fazer isso direto no notebook.
🚀 Deus é BOM!!!

📌 Como funciona um except específico?
💡 Python tem diversos tipos de exceções, cada uma representando um tipo de erro diferente.
Podemos capturar erros específicos usando except NomeDoErro:
🔹 Exemplos de exceções específicas:
✅ ValueError → Ocorre quando um tipo de dado inválido é fornecido (como converter texto para número).
✅ ZeroDivisionError → Ocorre ao tentar dividir por zero (10 / 0).
✅ IOError → Erro relacionado a entrada/saída de arquivos.
✅ FileNotFoundError → Arquivo não encontrado.
✅ TypeError → Ocorre quando uma operação é feita em tipos incompatíveis.
✅ IndexError → Acontece quando tentamos acessar um índice fora dos limites de uma lista ou tupla.
✅ KeyError → Erro ao tentar acessar uma chave inexistente em um dicionário.


# Estudo da Função `add_elem` com Tratamento de Exceções

Neste notebook vamos desenvolver e testar uma função padrão que:
- Adiciona elementos a uma lista.
- Utiliza **try/except/finally** para tratar possíveis erros.
- Contém boas práticas, como documentação (docstring) e validação de dados.

Cada célula a seguir funcionará como um bloco lógico do nosso estudo, com explicações e cenários de teste.

def add_elem(lista):
    """
    Adiciona um elemento a uma lista de nomes com segurança usando try/except.

    Parâmetros:
        lista (list): Lista onde o novo nome será adicionado.

    Retorno:
        list ou None: Lista atualizada se o nome for válido, ou None se houver erro.
    """
    try:
        # Solicita ao usuário que informe um nome e remove espaços extras
        elemento = input("Digite um nome para adicionar à lista: ").strip()
        
        # Verifica se a entrada não é vazia; se for, levanta uma exceção
        if not elemento:
            raise ValueError("Erro: O nome não pode ser vazio.")
        
        # Adiciona o nome à lista se tudo estiver correto
        lista.append(elemento)
        return lista

    except ValueError as e:
        # Captura o erro e exibe uma mensagem clara
        print(f"{e}")
        return None

    finally:
        # Este bloco é sempre executado, mesmo que ocorra uma exceção
        print("Execução finalizada.")


## Detalhamento da Função `add_elem`

**1. Definição e Docstring:**  
- A função é definida com `def add_elem(lista):` e documentada com uma docstring que explica o propósito, os parâmetros e o retorno.

**2. Bloco `try`:**  
- Solicita a entrada do usuário e usa `.strip()` para remover espaços.
- Verifica se a entrada é vazia; se sim, lança um `ValueError`.

**3. Bloco `except`:**  
- Captura especificamente um `ValueError` e exibe a mensagem associada.
- Retorna `None` caso haja erro.

**4. Bloco `finally`:**  
- Executa sempre, exibindo "Execução finalizada."  
  Esse bloco é útil para ações que devem ocorrer independentemente do sucesso ou falha da operação.

> **Nota:**  
> Mantenha a ordem das células para garantir que a função definida esteja disponível para os testes nas próximas células.

# Cenário 1: Teste com entrada válida
def add_elem(lista):
    """
    Adiciona um elemento a uma lista de nomes com segurança usando try/except.

    Parâmetros:
        lista (list): Lista onde o novo nome será adicionado.

    Retorno:
        list ou None: Lista atualizada se o nome for válido, ou None se houver erro.
    """
    try:
        # Solicita ao usuário que informe um nome e remove espaços extras
        elemento = input("Digite um nome para adicionar à lista: ").strip()
        
        # Verifica se a entrada não é vazia; se for, levanta uma exceção
        if not elemento:
            raise ValueError("Erro: O nome não pode ser vazio.")
        
        # Adiciona o nome à lista se tudo estiver correto
        lista.append(elemento)
        return lista

    except ValueError as e:
        # Captura o erro e exibe uma mensagem clara
        print(f"{e}")
        return None

    finally:
        # Este bloco é sempre executado, mesmo que ocorra uma exceção
        print("Execução finalizada.")

print("Cenário 1: Adicionar um nome válido")
nomes = []  # Lista de nomes inicialmente vazia
resultado = add_elem(nomes)
print("Resultado da lista:", resultado)

'''Instrução: Quando solicitado, digite um nome, por exemplo, Carlos.

Cenário 1: Entrada Válida

- **Expectativa:**  
  Ao digitar um nome válido, a função adiciona esse nome à lista.
- **Resultado:**  
  A lista será atualizada, por exemplo: `["Carlos"]`, e a mensagem "Execução finalizada." será exibida.
'''

nome = input("Digite seu nome: ")
print(f"Nome digitado: {nome}")


# Cenário 2: Teste com entrada incorreta (vazia)
print("Cenário 2: Tentar adicionar um nome vazio")
resultado = add_elem(nomes)
print("Resultado da lista:", resultado)

''' 
Instrução: Quando solicitado, apenas pressione ENTER sem digitar nada.

### Cenário 2: Entrada Incorreta (String Vazia)

- **Explicação:**  
  Ao pressionar ENTER sem digitar, a função dispara um `ValueError` devido à verificação de entrada vazia.
- **Expectativa:**  
  A mensagem `"Erro: O nome não pode ser vazio."` será exibida, e a função retornará `None`.
- **Resultado:**  
  A lista não será modificada e, novamente, "Execução finalizada." será impresso.
'''

# Cenário 3: Teste com outra entrada válida após o erro
print("Cenário 3: Adicionar outro nome válido (por exemplo, 'Ana')")
resultado = add_elem(nomes)
print("Resultado final da lista:", resultado)

'''
Instrução: Ao ser solicitado, digite Ana.

## Resumo e Considerações

- Utilizamos **try/except/finally** para criar uma função robusta que trata entradas inválidas.
- Cada cenário de teste ilustrou como a função se comporta com dados válidos e inválidos.
- **Importância da Ordem:**  
  Em notebooks, é fundamental manter os blocos em ordem, porque definimos a função primeiro e depois a chamamos em diferentes células.
- Este padrão pode ser reutilizado em outras funções para garantir segurança e clareza no seu código.

> **Dica:**  
> Mesmo que dividir o código em células diferentes possa, às vezes, causar erros se a ordem não for corretamente mantida (porque variáveis e funções precisam estar definidas antes de serem chamadas), essa abordagem torna o desenvolvimento interativo e facilita testes e explicações.

Essa estrutura de células (Markdown e Código) permite que você aprofunde os conceitos e teste a função add_elem em diferentes cenários. Dessa forma, você internaliza cada parte da lógica e das boas práticas sem sobrecarregar um bloco único.
Quando estiver pronto para criar seus "programinhas", essa organização ajudará a manter o código claro, modular e fácil de depurar.
Deus é BOM!!!
'''

def bloco(texto):
    """Aqui eu crio uma função que vai me formatar o output com linhas personalizdas
    Param1:Rece o texto que colocara entre as linhas personalizaas,
    Try: Para verificar se antrada esta correta em form,atoptexto
    return do try: Retornar o valor para a função personalizado.
    raise: Para verfificar se o dado esta vazio.
    except; Para capturar o erro, excecão, sse houver.
    else: Para executar se o try obteve  exito.
    return: None
    """
    try:
        txt = input("Digite uma mensagem de Amor a Deus:\n").strip()
        #Aqui eu solicito um input em formato str. Sequencialmete utiliza .strip() para remover qualquer inperfeição na str digitada pelo usuario.
        if not any(char.isalpha() for char in txt):
        #if not txt.isalpha():
            # Aqui eu verifico se há dados em txt, e se sim,verfico se são todos caracteres do alfabeto. 
            raise ValueError("Erro: Digite somente caracteres do alfabeto.")# Aqui eu levanto uma exeção manualmente para identificar erros de  inclusão de dados em formato str (alfabeticos).
        
        texto = txt
        print("\n")
        print('*' * 80)
        print(texto)
        print('*' * 80)
        return texto
    
    except ValueError as e:
        print(f"O erro foi: {e}")
    else:
        print("Bloco de linhas personalizadas feito com sucesso.")
    finally:
        print("Encerrando operação")

def maiuscula(texto):
    """Aqui eu crio uma função que vai transformar em mausculas toda a frase
    Param1:Recebe o texto que colocara em maiusculas.
    Try: Para verificar se a entrada esta correta em formato de texto
    return do try: Retornar o valor para a função personalizado.
    raise: Para verfificar se o dado esta vazio.
    except; Para capturar o erro, excecão, sse houver.
    else: Para executar se o try obteve  exito.
    return: None
    """
    try:
        frase = input("Digite a frase quer que seja maiuscula:\n").strip()

        if not any(char.isalpha() for char in frase):
            raise ValueError("Erro: Digite somente caracteres alfabeticos.")
        
        return frase.upper()
        #print(f"{texto}")
        #return texto
    except ValueError as e:
        print(f"{e}")
        return None 
    else:
        print("Conversão para maiusculas feita com sucesso")
    finally:
        print("encerrando operação")

def minusculas(texto):
    """Aqui eu crio uma função que vai transformar em minusculas toda a frase
    Param1:Recebe o texto que transformara em minusculas,
    Try: Para verificar se antrada esta correta em form,atoptexto
    return do try: Retornar o valor para a função personalizado.
    raise: Para verfificar se o dado esta vazio.
    except; Para capturar o erro, excecão, sse houver.
    else: Para executar se o try obteve  exito.
    return: None
    """
    try:
        frase = input("Digite a frase que vc deseja converter em minusculas:\n").strip()
        if not any(char.isalpha() for char in frase):
            raise ValueError("Erro: digite somente caracteres alfabeticos.")
        return  frase.lower()
        #print(f"{texto}")
    except ValueError as e:
        print(f"{e}")
        return None
    else:
        print("A conversão para minusculas ocorreu com sucesso.")
    finally:
        print("Encerrando operação")    

def chaves(dicio):
    """Aqui eu crio uma função que me retorna todas as chaves e um dict.
    Param1: Recebe o dicionario que retornara as chaves.
    Try: Vai tentar ver se há erros
      ∟ return: Vai rtornar as chaves d dicionario.
    If not...: Vai verificar a existencia de conteudo no dicionario.
    raise: Se houver, vai levantar exceções sobre possiveis erros relacioados as chaves do diconario.
    except: Vai tratar o erro de forma adequada.
       ∟ return: Vai retornar None
    else: Vai retornar uma mensagem deccorente do exito do try.
    finally: Vai encerrar a operação de forma elegante, para limpar qualquer coisa que estiver pendente."""
    try:
        dicio.keys()
        if not dicio:
            raise KeyError("Erro: A chave não existe")
        print('*' * 60)
        print(f"As chaves do dicionario que vc me passou são:\n{dicio.keys()}")
        print('*' * 60)
    except KeyError as e:
        print('*' * 60)
        print(f"Houve este impasse: {e}")       
        print('*' * 60)
    else:
        print("Acima (↑) estão os nomes das chaves.")
        print('*' * 60)
    finally:
        print("Encerrando operação...")
        print('*' * 60)

def valores_dict(dicio):
    """Aqui eu crio uma função que me retorna todas os valores que contem   as chaves de um dict.
    Param1: Recebe o dicionario que retornara as chaves.
    Try: Vai tentar ver se há erros
     ∟ return: Vai rtornar os valores do dicionario.
    If not...: Vai verificar a existencia de conteudo no dicionario.
    raise: Se houver, vai levantar exceções sobre possiveis erros relacioados as chaves do diconario.
    except: Vai tratar o erro de forma adequada.
      ∟ return: Vai retornar None
    else: Vai retornar uma mensagem deccorente do exito do try.
    finally: Vai encerrar a operação de forma elegante, para limpar qualquer coisa que estiver pendente."""
    try:
        dicio.values()
        if not dicio:
            raise Exception("A chave não pode estar vazia.")
        print('*' * 90)
        print(f"Os valores que estão nesta estrutura dict são:\n {dicio}")     
    except Exception as e:
        print('*' * 60)
        print(f"Ocorreu esta discordancia:\n{e}")
        print('*' * 60)
    else:
        print("\nAcima (↑) estão os valores das chaves dos dicionarios.")
    finally:
        print('*' * 25)
        print('Encerrando operação')
        print('*' * 25)

dados_pessoais = {"Nome": "Eduardo", "Idade": "37", "Profissão": "Estudante", "Hobbie": "Assistir animes"}



dados_complementares =  []

for k, v in dados_pessoais.items():
    print(f" a chave é {k} e o seu valor é:{v}")


def somar(a, b):
    return a + b

operacao = somar  # Atribuindo a função a uma variável
print(operacao(3, 4))  # Chama a função com argumentos

