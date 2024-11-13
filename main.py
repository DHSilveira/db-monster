import sqlite3

# Conectando ao banco de dados (ou criando, se não existir)
con = sqlite3.connect('meu_dicionario.db')
cur = con.cursor()

# Criando a tabela, se não existir
cur.execute('''
    CREATE TABLE IF NOT EXISTS dicionario (
        chave TEXT PRIMARY KEY,
        valor TEXT
    )
''')
con.commit()

def inserir_novo_item():
    chave = input("Digite a nova chave: ")
    valor = input("Digite o novo valor: ")

    # Inserindo o novo par chave-valor no banco de dados
    try:
        cur.execute('INSERT INTO dicionario (chave, valor) VALUES (?, ?)', (chave, valor))
        con.commit()
        print(f"Par chave-valor '{chave}: {valor}' inserido com sucesso.")
    except sqlite3.IntegrityError:
        print("Essa chave já existe no dicionário!")

def buscar_valor():
    chave = input("Digite a chave que deseja buscar: ")
    cur.execute('SELECT valor FROM dicionario WHERE chave = ?', (chave,))
    resultado = cur.fetchone()

    if resultado:
        print(f"O valor para a chave '{chave}' é: {resultado[0]}")
    else:
        print("Chave não encontrada no dicionário.")

# Loop de operações
while True:
    print("\nEscolha uma opção:")
    print("1. Inserir novo item")
    print("2. Buscar valor")
    print("3. Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        inserir_novo_item()
    elif opcao == "2":
        buscar_valor()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Fechando a conexão com o banco de dados
con.close()
