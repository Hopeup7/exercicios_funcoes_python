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