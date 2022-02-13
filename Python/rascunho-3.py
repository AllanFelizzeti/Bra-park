import mysql.connector
from mysql.connector import Error

def Conectar():#Função faz a conecão com o Banco tem que estar em todas as outra Funções
    try:
        global con#É oq permite usar a Função Conectar dentro das outras Funcões
        con = mysql.connector.connect(host='localhost', database='testbra_park', user='root', password='')
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
def CadastroHora(vaga):#Tentar colocar unificar com a Função Cadastrar
    try:
        Conectar()
        preencher_vaga = "UPDATE vagas SET Hora_entrada = CURTIME() WHERE N_Vagas =" + vaga
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
        consulta_sql = f"SELECT * FROM carro INNER JOIN vagas ON carro.Vagas_N_Vagas =vagas.N_Vagas" \
                       f" WHERE Placa = '{busc_placa}'"
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print(f"VagaN°:{linha[4]}")
            print(f"Cpf:{linha[0]}")
            print(f"Placa:{linha[1].upper()}")
            print(f"Cel:{linha[2]}")
            print(f"Hora de entrada:{linha[5]}")
            print(f"Hora de saida:{linha[6]}")
            print("---------------------------\n")
    except Error as erro:
        print(f"Falha ao consultar a tabela:{format(erro)}")
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

def HoraFinal(horaf):#Função finaliza o cliente \Função ainda em desenvolvimento
    try:
        Conectar()
        preencher_saida = "UPDATE Vagas SET Hora_saida = CURTIME() WHERE N_Vagas =" + horaf
        cursor = con.cursor()
        cursor.execute(preencher_saida)
        con.commit()
        print("Vaga Finalizada com sucesso!")
    except Error as erro:
        print(f"Falha ao peencher Vaga:{format(erro)}")
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
def VagasOcupadas():
    try:
        Conectar()
        consulta_sql = "SELECT * FROM carro INNER JOIN vagas ON carro.Vagas_N_Vagas =vagas.N_Vagas" \
                       " WHERE Hora_entrada > 1 ORDER BY N_Vagas "#Aqui em teste
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print(f"VagaN°:{linha[4]}")
            print(f"Cpf:{linha[0]}")
            print(f"Placa:{linha[1].upper()}")
            print(f"Cel:{linha[2]}")
            print(f"Hora de entrada:{linha[5]}")
            print(f"Hora de saida:{linha[6]}")
            print("---------------------------\n")
    except Error as erro:
        print(f"Falha ao consultar a tabela:{format(erro)}")
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
def ConfirmeCliente(busc_placa):#Função em teste para ver se nessecaria
    try:
        Conectar()
        consulta_sql = f"SELECT * FROM carro INNER JOIN vagas ON carro.Vagas_N_Vagas =vagas.N_Vagas" \
                       f" WHERE Placa = '{busc_placa}'"
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print(f"VagaN°:{linha[4]}")
            print(f"Cpf:{linha[0]}")
            print(f"Placa:{linha[1].upper()}")
            print(f"Cel:{linha[2]}")
            print(f"Hora de entrada:{linha[5]}")
            print(f"Hora de saida:{linha[6]}")
            print("---------------------------\n")
    except Error as erro:
        print(f"Falha ao consultar a tabela:{format(erro)}")
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
def Codranca(horaf):#Faz a diferença das horas entrada e saida ainda em Desenvolvimento
    try:
        Conectar()
        consulta_sql = "SELECT TIMEDIFF(Hora_saida , Hora_entrada) from vagas WHERE N_vagas =" + horaf
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print(f"Tempo de uso:{linha[0]}")
        #Apenas um esboço não foi testado ainda
        print("Tabela de Preço")
        if '00:15:00' in linha[0]:
            print("Livre")
        elif '00:16:00' in linha[0] or '03:00:00' in linha[0]:
            print("Valor é 15 R$")
        elif '03:00:01' in linha[0] or '05:00:00' in linha[0]:
            print("Valor é 20 R$")
        else:
            print("Valor é 30 R$")

    except Error as erro:
        print(f"Falha ao consultar a tabela:{format(erro)}")
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
def LiberarVaga(horaf):#Retira os dados do cliente para poder cadastrar o proximo
    try:
        Conectar()
        liberar_carro = f"UPDATE carro SET Cpf = '{horaf}' , Placa = '', Cel = '' WHERE Vagas_N_Vagas =" + horaf
        liberar_vagas = "UPDATE vagas SET Hora_entrada = '', Hora_saida = '' WHERE N_Vagas =" + horaf
        cursor = con.cursor()
        cursor.execute(liberar_vagas)
        cursor.execute(liberar_carro)
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
      ### B-R-A Park ###
      1 - Consultar Vagas Livres
      2 - Cadastra Veiculo 
      3 - Buscar Veiculo por Placa
      4 - Ver Todas Vagas Ocupadas
      5 - Buscar por Cpf Ainda não desenvolvido
      6 -  
      0 - Sair \n""")
    n = int(input('Escolha sua opção:'))
    print("\n")
    if n == 1:#Busca vagas livres
        print("Vagas livres")
        Colsulta()
    elif n == 2:#Cadastrar Veicolos
        #Ideia fazer um menu interativo para alterar somemte um campo
        #que possa ser digito errado.
        print("Cadastrar o Carro")
        cpf = input("Digite o Cpf do dono:")
        pl = input("Digite a placa do Carro: ")
        cel = input("Digite o Celular do dono: ")
        vaga = input("Digite a vaga a ser ocupada: ")
        declaracao = """UPDATE Carro SET Cpf = """ '\'' + cpf + '\','""" Placa = """ '\'' + pl + '\','""" Cel = 
        """ '\'' + cel + '\''""" WHERE Vagas_N_Vagas = """ + vaga
        Cadastra(declaracao)
        CadastroHora(vaga)
    elif n == 3:#Busca por placa do Veiculo
        print("Buscar por Placa")
        busc_placa = input("Informe a Placa desejada:")
        print("\n")
        Busca_Placa(busc_placa)
        p = -1
        while p != 0:#Segundo menu interativo
            print(f""" 
                  ### B-R-A Park ###
                  1 - Buscar outra Placa 
                  2 - Finalizar
                  3 - Liderar Vaga
                  0 - Sair \n""")
            p = int(input('Escolha sua opção:'))
            if p == 1:#Caso vc erre a placa pode fazer uma nova busca
                busc_placa = input("Informe a Placa:")
                print("\n")
                Busca_Placa(busc_placa)
            elif p == 2:#finaliza o cliente ainda em Desenvolvimento
                ConfirmeCliente(busc_placa)
                horaf = input("Informe a vaga da placa que deve ser finalizada:")
                print("(s) para SIM ou (n) para NÂO")
                f = input(f"Certeza que quer Finalizar esse Cliente:")
                if 's' == f:
                    HoraFinal(horaf)
                    Codranca(horaf)
                else:
                    p = 0
            elif p == 3:
                horaf = input("Informe a vaga da placa que deve ser finalizada:")
                LiberarVaga(horaf)
            else:
                p = 0
    elif n == 4:
        print("Vagas Ocupadas")#Busca pelas vagas ocupasdas
        VagasOcupadas()
    elif n == 5:
        print("Em Desenvolvimrnto")
    elif n == 6:
        print("Em Desenvolvimrnto")
#favor comentar qualquer alteração feita no codigo
#Desde já muito obrigado
#Alterações feitas hoje 25/11
#Função buscar por vagas ocupadas
#Adaptação do projeto para funcionar com duas tabelas em MySQL
#Alterações feitas hoje 26/11
#Função Cobrança mais ainda não foi finalizada
#Função Liberar vaga