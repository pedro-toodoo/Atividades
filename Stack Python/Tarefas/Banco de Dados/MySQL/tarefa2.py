import pymysql.cursors

#INSERTS
def insert_agente(conexao, idAgente, nome, endereco, nascimento, habilidade, sexo, email):
    with conexao.cursor() as db:
        sql = 'INSERT INTO Agente(idAgente, nome, endereco, nascimento, habilidade, sexo, email) VALUES(%s, %s, %s, %s, %s, %s, %s)'
        db.execute(sql, (idAgente, nome, endereco, nascimento, habilidade, sexo, email))
        conexao.commit()

def insert_missao(conexao, data, nome, locali, duracao, idVilao):
    with conexao.cursor() as db:
        sql = 'INSERT INTO Missao(data, nome, locali, duracao, idVilao) VALUES(%s, %s, %s, %s, %s)'
        db.execute(sql, (data, nome, locali, duracao, idVilao))
        conexao.commit()

def insert_vilao(conexao, idVilao, nome, num_crimes):
    with conexao.cursor() as db:
        sql = 'INSERT INTO Vilao(idVilao, nome, num_crimes) VALUES(%s, %s, %s)'
        db.execute(sql, (idVilao, nome, num_crimes))
        conexao.commit()

def insert_agente_has_missao(conexao, idAgente, idMissao):
    with conexao.cursor() as db:
        sql = 'INSERT INTO Agente_has_Missao(idAgente, idMissao) VALUES(%s, %s)'
        db.execute(sql, (idAgente, idMissao))
        conexao.commit()

#BUSCA
def pesquisar_agente_missao(conexao):
    with conexao.cursor() as db:
        #sql = 'SELECT A.nome, A.email, M.nome, M.data FROM Agente A, Missao M JOIN Agente_has_Missao H ON H.idAgente == A.idAgente'
        sql = 'SELECT A.nome, A.email, M.nome, M.data FROM Agente A JOIN Missao M JOIN Agente_has_Missao H ON A.idAgente = H.idAgente AND M.idMissao = H.idMissao '
        db.execute(sql)
        result = db.fetchall()

        print(f"AGENTE-MISSÃO:")
        for i in result:
            print(f"{i['nome']} ({i['email']}) -> {i['M.nome']} ({str(i['data'])})")

def pesquisar_missao_vilao(conexao):
    with conexao.cursor() as db:
        sql = 'SELECT M.nome, M.data, M.duracao, V.nome FROM Missao M JOIN Vilao V USING (idVilao)'
        db.execute(sql)
        result = db.fetchall()

        print(f"MISSÃO-VILÃO:")
        for i in result:
            print(f"{i['nome']}: {str(i['data'])} ({i['duracao']}hrs) [{i['V.nome']}]")

def pesquisa_agente_missao_vilao(conexao):
    with conexao.cursor() as db:
        sql = 'SELECT A.nome, M.nome, V.nome FROM Agente A JOIN Missao M JOIN Vilao V JOIN Agente_has_Missao H ON A.idAgente = H.idAgente AND '\
              'M.idMissao = H.idMissao AND M.idVilao = V.idVilao; '
        db.execute(sql)
        result = db.fetchall()

        print(f"AGENTE-MISSÃO-VILÃO:")
        for i in result:
            print(f"{i['nome']}: {i['M.nome']} - {i['V.nome']}")

def update_data_missao(conexao, idMissao, data):
    with conexao.cursor() as db:
        sql = 'UPDATE Missao SET data = %s WHERE idMissao = %s'
        db.execute(sql, (data, idMissao))
        conexao.commit()

def delete_agente(conexao, idAgente):
    with conexao.cursor() as db:
        sql = 'DELETE FROM Agente WHERE idAgente = %s'
        db.execute(sql, idAgente)
        conexao.commit()

if __name__ == '__main__':
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='admin',
        db='secreto',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

#ADD AGENTES
'''insert_agente(conexao, 1, 'Pedro', 'Rua 1', '1998-03-14', 'Super velocidade', 'Masc', 'pedro@email.com')
insert_agente(conexao, 2, 'Flavio', 'Rua 2', '2021-12-22', 'hab1', 'Masc', 'flavio@email.com')
insert_agente(conexao, 3, 'Pamela', 'Rua 3', '2021-12-22', 'hab2', 'Fem', 'pamela@email.com')
insert_agente(conexao, 4, 'Igor', 'Rua 4', '2021-12-22', 'hab3', 'Masc', 'igor@email.com')
insert_agente(conexao, 5, 'Marcos', 'Rua 5', '2021-12-22', 'hab5', 'Masc', 'marcos@email.com')'''

#ADD VILÃO
'''insert_vilao(conexao, 1, 'Vilão 1', 5)
insert_vilao(conexao, 2, 'Vilão 2', 3)
insert_vilao(conexao, 3, 'Vilão 3', 12)
insert_vilao(conexao, 4, 'Vilão 4', 4)
insert_vilao(conexao, 5, 'Vilão 5', 2)'''

#ADD MISSÃO
'''insert_missao(conexao, '1998-03-14', 'Missão 1', 'Local 1', 1, 1)
insert_missao(conexao, '2021-12,22', 'Missão 2', 'Local 2', 4, 2)
insert_missao(conexao, '2021-10,22', 'Missão 3', 'Local 3', 8, 3)
insert_missao(conexao, '2021-12,14', 'Missão 4', 'Local 4', 3, 4)
insert_missao(conexao, '2021-12,20', 'Missão 5', 'Local 5', 5, 5)'''

#ADD Agente_has_Missao
'''insert_agente_has_missao(conexao, 1, 5)
insert_agente_has_missao(conexao, 2, 4)
insert_agente_has_missao(conexao, 3, 3)
insert_agente_has_missao(conexao, 4, 2)
insert_agente_has_missao(conexao, 5, 1)'''

#BUSCA
'''pesquisar_agente_missao(conexao)
print("-"*40)
pesquisar_missao_vilao(conexao)
print("-"*40)
pesquisa_agente_missao_vilao(conexao)'''

#update_data_missao(conexao, 3, '2002-04-03')
delete_agente(conexao, 5)

