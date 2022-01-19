import mysql.connector
from mysql.connector import Error

def Conectar():#Função faz a conecão com o Banco
    try:
        global con
        con = mysql.connector.connect(host='localhost', database='bra_park', user='root', password='')
    except Error as erro:
        print(f"Erro de Conexão:{format(erro)}")

def Colsulta():#Função faz consulta ao Banco
    try:
        Conectar()
        consulta_sql = "SELECT * fROM Vagas WHERE Hora_entrada = ''"
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print(f"VagaN°:{linha[0]}")
    except Error as erro:
        print(f"Falha ao consultar a tabela:{format(erro)}")
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

def Cadastra(declaracao):#Função Cadastra um novo Cliente ao banco
    try:
        Conectar()
        preencher_vaga = declaracao
        cursor = con.cursor()
        cursor.execute(preencher_vaga)
        con.commit()
        print("Vaga preenchida com sucesso!")
    except Error as erro:
        print(f"Falha ao peencher Vaga:{format(erro)}")
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

def Busca_Placa(busc_placa):#Função faz uma busca no banco
                            # pela placa do Veiculo
    try:
        Conectar()
        consulta_sql = busc_placa
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print(f"VagaN°:{linha[0]}")
            print(f"Hora de entrada:{linha[1]}")
            print(f"Hora da saida:{linha[2]}")
            print(f"Placa:{linha[3].upper()}")
            print(f"Cel:{linha[4]}")
    except Error as erro:
        print(f"Falha ao consultar a tabela:{format(erro)}")
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

def Finalizar(finalizar):#Função finaliza o cliente 
                         #Função ainda em desenvolvimento
    try:
        Conectar()
        preencher_vaga = finalizar
        cursor = con.cursor()
        cursor.execute(preencher_vaga)
        con.commit()
        print("Vaga Finalizada com sucesso!")
    except Error as erro:
        print(f"Falha ao peencher Vaga:{format(erro)}")
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()



print("Bem vindo ao B-R-A Park")

n = -1
while n != 0:#Menu interativo ainda em Desenvolvimento
    print(f""" 
      ### B-R-a Park ###
      1 - Consultar Vagas Livres
      2 - Cadastra Veiculo 
      3 - Buscar Veiculo por Placa
      4 - 
      5 - 
      6 -  
      0 - Sair """)
    n = int(input('Escolha sua opção:'))
    if n == 1:#Busca vagas livres
        print("Vagas livres")
        Colsulta()
    elif n == 2:#Cadastrar Veicolos
        print("Cadastrar o Carro")
        pl = input("Digite a placa do Carro: ")
        cel = input("Digite o Celular do dono: ")
        vaga = input("Digite a vaga a ser ocupada: ")
        declaracao = """UPDATE Vagas SET Placa = """ '\'' + pl + '\','"""Cel = """ '\'' + cel + '\','"""
        Hora_entrada = CURTIME() WHERE N_Vagas = """ + vaga
        Cadastra(declaracao)
    elif n == 3:#Busca por placa do Veiculo
        print("Buscar por Placa")
        bp = input("Informe a Placa desejada:")
        busc_placa = f"SELECT * FROM Vagas WHERE Placa = '{bp}'"
        Busca_Placa(busc_placa)
        p = -1
        while p != 0:#Segundo menu interativo
            print(f""" 
                  ### B-R-a Park ###
                  1 - Buscar outra Placa 
                  2 - Finalizar
                  0 - Sair """)
            p = int(input('Escolha sua opção:'))
            if p == 1:#Caso vc erre a placa pode fazer uma nova busca
                fp = input("Informe a Placa:")
                busc_placa = f"SELECT * FROM Vagas WHERE Placa = '{fp}'"
                Busca_Placa(busc_placa)
            elif p == 2:#finaliza o cliente ainda em Desenvolvimento
                finalizar = f"""UPDATE Vagas SET Hora_saida = CURTIME() 
                WHERE Placa = '{fp}'"""
                print("(S) para ou (N) para não")
                f = input(f"Certeza que quer Finalizar a Placa {fp.upper()}: ")
                if f == 'S':#Ajuda a não fazer merda e perder o emprego
                    Finalizar(finalizar)
                else:
                    p = 0
            else:
                p = 0
    elif n == 4:
        print("Em Desenvolvimento")
    elif n == 5:
        print("Em Desenvolvimrnto")
    elif n == 6:
        print("Em Desenvolvimrnto")
#favor comentar qualquer alteração feita no codigo 
# desde já muito obrigado