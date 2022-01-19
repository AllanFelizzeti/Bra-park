from tkinter import PhotoImage, Tk, Label
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
def VagasOcupadas():#Busca por todas as vagas ocupadas
    try:
        Conectar()
        consulta_sql = "SELECT * FROM carro INNER JOIN vagas ON carro.Vagas_N_Vagas =vagas.N_Vagas" \
                       " WHERE Hora_entrada > 1 ORDER BY N_Vagas "
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
def ConfirmeCliente(busc_placa):#Verifica se os dados estão certo
                                # pela placa do carro
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
def Tempofinal(horaf):#Faz a diferença das horas entrada e saida ainda em Desenvolvimento
    try:
        Conectar()
        consulta_sql = "SELECT TIMEDIFF(Hora_saida , Hora_entrada) from vagas WHERE N_vagas =" + horaf
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print(f"Tempo de uso:{linha[0]}")

    except Error as erro:
        print(f"Falha ao consultar a tabela:{format(erro)}")
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
def LiberarVaga(vaga):#Retira os dados do cliente para poder cadastrar o proximo
    try:
        Conectar()
        liberar_carro = f"UPDATE carro SET Cpf = '{vaga}' , Placa = '', Cel = '' WHERE Vagas_N_Vagas =" + vaga
        liberar_vagas = "UPDATE vagas SET Hora_entrada = '', Hora_saida = '' WHERE N_Vagas =" + vaga
        cursor = con.cursor()
        cursor.execute(liberar_vagas)
        cursor.execute(liberar_carro)
        con.commit()
        print("Vaga Liberada com sucesso!")
    except Error as erro:
        print(f"Falha ao peencher Vaga:{format(erro)}")
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
def ErroVaga(vaga):#Em caso de erro de cadastro do  Cliente
                    #apaga os dados errados
    try:
        Conectar()
        liberar_carro = f"UPDATE carro SET Cpf = '{vaga}' , Placa = '', Cel = '' WHERE Vagas_N_Vagas =" + vaga
        cursor = con.cursor()
        cursor.execute(liberar_carro)
        con.commit()
        print("Faça o Cadastro Novamente!")
    except Error as erro:
        print(f"Falha ao peencher Vaga:{format(erro)}")
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
def Cobranca(busc_placa):#Busca por placa para cobrança
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
def VagaCheck(vaga):#Verifica se os dados do cliente esta certo
    try:
        Conectar()
        consulta_sql = "SELECT * FROM carro INNER JOIN vagas ON carro.Vagas_N_Vagas =vagas.N_Vagas" \
                       " WHERE N_Vagas = " + vaga
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
def Zuera():
    root = Tk()
    root.title("B-R-A Park")
    img = PhotoImage(file="imagens/golle.png")
    label_imagem = Label(root, image=img).pack()
    root.mainloop()

print("Bem vindo ao B-R-A Park")

n = -1
while n != 0:#Menu interativo principal
            #Busca(Select) por vagas livres
            #Cadastra(Update) um Novo Cliente
            #Busca(select) por uma placa em especifico
            #Busca(Select) por vagas ocupadas[
            #Finaliza o Programa
    print(f""" 
      ### B-R-A Park ###
      1 - Consultar Vagas Livres
      2 - Cadastra Veiculo 
      3 - Buscar Veiculo por Placa
      4 - Ver Todas Vagas Ocupadas
      0 - Sair \n""")
    n = int(input('Escolha sua opção:'))
    print("\n")
    if n == 1:#Busca vagas livres
        print("Vagas livres")
        Colsulta()
    elif n == 2:#Cadastrar Veicolos
        print("Cadastrar o Carro")
        cpf = input("Digite o Cpf do dono:")
        pl = input("Digite a placa do Carro: ")
        cel = input("Digite o Celular do dono: ")
        vaga = input("Digite a vaga a ser ocupada: ")
        declaracao = """UPDATE Carro SET Cpf = """ '\'' + cpf + '\','""" Placa = """ '\'' + pl + '\','""" Cel = 
        """ '\'' + cel + '\''""" WHERE Vagas_N_Vagas = """ + vaga
        Cadastra(declaracao)
        print("\n")
        print("Os Dados do Cliente estão Certos?\n")
        VagaCheck(vaga)#Verifica se os dados estão certo
        check = input("(s) para SIM ou (n) para NÂO\n")
        if 's' == check:
            CadastroHora(vaga)
        else:
            ErroVaga(vaga)#Apaga dados errados
            p = 0
    elif n == 3:#Busca(Select) por placa do Veiculo
        print("Buscar por Placa")
        busc_placa = input("Informe a Placa desejada:")
        print("\n")
        Busca_Placa(busc_placa)
        p = -1
        while p != 0:#Menu Secundario de finalização
                    #Busca(select) por placa especifica
                    #Finaliza a hora_saida(UPDATE/CURTIME)
                    #Tambem calcula o o tempo de uso da vaga(SELECT/TIMEDIFF)
                    #Cobrar abre o terceiro menu interativo
                    #Liberar Vaga(Update) limpa os dados do Cliente da vaga
            print(f""" 
                  ### B-R-A Park ###
                  1 - Buscar outra Placa 
                  2 - Finalizar
                  3 - Cobrança
                  4 - Liberar Vaga
                  0 - Sair \n""")
            p = int(input('Escolha sua opção:'))
            if p == 1:#Caso vc erre a placa pode fazer uma nova busca por outra placa
                busc_placa = input("Informe a Placa:")
                print("\n")
                Busca_Placa(busc_placa)
            elif p == 2:#finaliza o cliente e devolve o tempo que ele usou a vaga
                horaf = input("Informe a Vaga que deve ser finalizada:")
                print("(s) para SIM ou (n) para NÂO")
                ConfirmeCliente(busc_placa)#Confirma se é o cliente certo se não so apertar (n)
                f = input(f"Certeza que quer Finalizar esse Cliente:")
                if 's' == f:
                    HoraFinal(horaf)
                    Tempofinal(horaf)
                else:
                    p = 0
            elif p == 3:
                #Menu Terciario de cobrança
                #com opções de valor dependendo do tempo
                # de que a vaga foi ocupada
                busc_placa = input("Informe a Placa desejada:")
                horaf = input("Informe a Vaga:")
                print("Tabela de Preços")
                print("Até 15 minutos livre")
                print(f""" 
                              ### B-R-A Park ###
                              1 - Tempo acima de 16 minutos até 3 horas
                              2 - Tempo acima 3 horas até 6 horas
                              3 - Acima de 6 horas  
                              0 - Sair \n""")
                q = -1
                while q != 0:
                    va = int(input("Opção de Cobrança:"))
                    if va == 1:
                        print("Valor a ser Cobrado 12 R$")
                        Tempofinal(horaf)
                        Cobranca(busc_placa)
                        q = 0
                    elif va == 2:
                        print("Valor a ser Cobrado 20 R$")
                        Tempofinal(horaf)
                        Cobranca(busc_placa)
                        q = 0
                    elif va == 3:
                        print("Valor a ser Cabrado 30 R$")
                        Tempofinal(horaf)
                        Cobranca(busc_placa)
                        q = 0
                    else:
                        q = 0
            elif p == 4:#Libera a vaga
                vaga = input("Informe a Vaga que deve ser finalizada:")
                print("(s) para SIM ou (n) para NÂO")#Caso tenha errado a vaga só colocar (n) para buscar novamente
                VagaCheck(vaga)
                f = input(f"Certeza que quer Finalizar essa Vaga:")
                if 's' == f:
                    LiberarVaga(vaga)
                else:
                    p = 0
            else:
                p = 0
    elif n == 4:
        print("Vagas Ocupadas")#Busca pelas vagas ocupasdas
        VagasOcupadas()
    else:
        Zuera()
#favor comentar qualquer alteração feita no codigo
#Desde já muito obrigado
#Alterações feitas hoje 25/11
#Função buscar por vagas ocupadas
#Adaptação do projeto para funcionar com duas tabelas em MySQL
#Alterações feitas hoje 26/11
#Função Cobrança mais ainda não foi finalizada
#Função Liberar vaga
#Alterações feitas hoje 28/11
#Função cobrança e menu cabrança