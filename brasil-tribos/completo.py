from conexao import conectar
def listar(conn, cursor):
    # Abrir uma conexão com o banco de dados
    conn = conectar()
    # Criando um objetivo cursor para executr as consultas SQL
    cursor = conn.curssor()
    # Executar a consulta SQL para listar os registros
    cursor.execute("SELECT * FROM tribo")
    # Obter resultados
    resultados = cursor.fetchall()
    # Imprimir resultados
    for resultado in resultados:
        print(resultado)
    # Fechar a conexao e o cursor 
    cursor.close()
    conn.close()
    
def inserir(codigo, nome):
    # Abrir uma conexão com o banco de dados
    conn = conectar()
    # Criando um objetivo cursor para executr as consultas SQL
    cursor = conn.curssor()
    # Executar a consulta SQL para interigir um novo registro 
    sql = "INSERT INTO tribo (ID_tribo, nome_tribo, num_habit, renda_mensal, escolaridade, trab_assa) VALUES (%s, %s)"
    val = (ID_tribo, nome_tribo, num_habit, renda_mensal, escolaridade, trab_assa)
    cursor.execute(sql, val)
    # Commit da transação 
    conn.commit()
    # Imprimir mensagem de sucesso
    print("Registro inserido com sucesso.")
    #  Fechar a conexão e o cursor 
    cursor.close()
    conn.close()
    
def atualizar (codigo, novo_nome):
     # Abrir uma conexão com o banco de dados
    conn = conectar()
    # Criando um objetivo cursor para executr as consultas SQL
    cursor = conn.curssor()
    # Executar a consulta SQL para atualizar o registro 
    sql = "UPDATDE tribo SET nome_tribo = %s WHERW id = %s"
    val = (novo_nome, codigo)
    cursor.execute(sql, val)
    # Commit da transação 
    conn.commit()
    # Verificar se algum registro foi atualizado
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")
    # Fechar a conexão e o cursor 
    cursor.close()
    conn.close()
    
def excluir (codigo):
    # Abrir uma conexão com o banco de dados
    conn = conectar()
    # Criando um objetivo cursor para executr as consultas SQL
    cursor = conn.curssor()
    # Executar a consulta SQL para excluir o registro 
    sql = "DELETE FROM tribo WHERE id = %s)"
    val = (codigo,)
    cursor.execute(sql, val)
    # Commit da transação 
    conn.commit()
    # Verificar se algum registro foi deletado
    if cursor.rowcount == 0:
        print("Nenhum registro deletado.")
    else:
        print("Registro deletado com sucesso.")
    # Fechar a conexão e o cursor 
    cursor.close()
    conn.close()
    
conn = conectar()
# Criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()
while True:
    # Mostra as opções de opreação
    print("O que você deseja fazer?")
    print("1 - Listar tribo")
    print("2 - Inserir nova tribo")
    print("3 - Atualizar uma tribo")
    print("4 - Deletar uma tribo")
    print("0 - Sair")
    
    opcao = int(input("Digite o número da opção desejada: "))
    
    if opcao == 1:
        # Listar estados
        listar(conn, cursor)
    
    elif opcao == 2:
        # Inserir novo estado
        ID_tribo = int(input("Digite o ID da nova tribo: "))
        nome_tribo = input("Digite o nome da nova tribo: ")
        num_habit = int(input("Digite o número de habitantes da tribo: "))
        renda_mensal = input("Digite a renda mensal da tribo:  ")
        escolaridade = input("Digite o nivel de escolaridade (fundamental, médio ou superior)")
        trab_assa = input("Digite se possuem trabalho assalariado sim ou não: ")
        inserir(ID_tribo, nome_tribo, num_habit, renda_mensal, escolaridade, trab_assa)
    
    elif opcao == 3:
        # Atualizar um estado
        codigo = int(input("Digite o código do estado que deseja: "))
        nome = input("Digite o novo nome do estado: ")
        atualizar(codigo, nome)
    
    elif opcao == 4:
        # Deletar um estado
        codigo = int(input("Digite o código do estado que deseja: "))
        excluir(codigo)
    
    elif opcao == 0:
        # Sair do programa
        break
    
    else:
        print("Opção inválida. Digite novamente")

# fechar a conexão
cursor.close()
conn.close()