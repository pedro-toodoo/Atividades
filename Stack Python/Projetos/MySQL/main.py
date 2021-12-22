import pymysql.cursors

def insert_empregado(conexao, id, nome, endereco):
    with conexao.cursor() as db:
        sql = 'INSERT INTO Empregado(idEmpregado, nome, endereco) VALUES(%s, %s, %s)'
        db.execute(sql, (id, nome, endereco))
        conexao.commit()

def insert_dependentes(conexao, nome, endereco, fk):
    with conexao.cursor() as db:
        sql = 'INSERT INTO Dependentes(nome, endereco, idEmpregado) VALUES(%s, %s, %s)'
        db.execute(sql, (nome, endereco, fk))
        conexao.commit()

def select_empregado(conexao):
    with conexao.cursor() as db:
        sql = 'SELECT * FROM Empregado'
        db.execute(sql)
        result = db.fetchall()

        for i in result:
            print(f"iD: {i['idEmpregado']} / Nome: {i['nome']} / Endereço: {i['endereco']}")

def select_dependentes(conexao):
    with conexao.cursor() as db:
        sql = 'SELECT * FROM Dependentes'
        db.execute(sql)
        result = db.fetchall() #consultas no banco usa-se fetchall

        for i in result:
            print(f"iD: {i['idDependente']} / Nome: {i['nome']} / Endereço: {i['endereco']} / ID Empregado: {'idEmpregado'}")
            #print(i)

def update_empregado(conexao, id, endereco):
    with conexao.cursor() as db:
        sql = 'UPDATE Empregado SET endereco = %s WHERE idEmpregado = %s'
        db.execute(sql, (endereco, id))
        conexao.commit() #escrita no banco (inserção, att, exclusão) é feito commit

def update_dependentes(conexao, id, nome):
    with conexao.cursor() as db:
        sql = 'UPDATE Dependentes SET nome = %s WHERE idDependente = %s'
        db.execute(sql, (nome, id))
        conexao.commit() #escrita no banco (inserção, att, exclusão) é feito commit

def delete_empregado(conexao, id):
    with conexao.cursor() as db:
        sql = 'DELETE FROM Empregado WHERE idEmpregado = %s'
        db.execute(sql, id)
        conexao.commit()

def delete_dependentes(conexao, id):
    with conexao.cursor() as db:
        sql = 'DELETE FROM Dependentes WHERE idDependente = %s'
        db.execute(sql, id)
        conexao.commit()

def pesquisar(conexao):
    with conexao.cursor() as db:
        sql = 'SELECT E.nome, D.nome FROM Empregado E JOIN Dependentes D USING (idEmpregado)'
        #sql = 'SELECT E.nome, D.nome FROM Empregado E JOIN Dependentes D ON D.idEmpregado = E.idEmpregado'
        db.execute(sql)
        result = db.fetchall()

        for i in result:
            print(i)

if __name__ == '__main__':
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='Par15632@',
        db='Empresa',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )


    #insert_empregado(conexao, 1, 'Spider Man', 'NY')
    #insert_empregado(conexao, 3, 'Taz mania', 'Cataguases')

    #insert_dependentes(conexao, 'Tia May', 'NY', 1)
    #insert_dependentes(conexao, 'Uncle Ben', 'NY', 1)

    #update_empregado(conexao, 1, 'Brooklyng')
    #select_empregado(conexao)

    #update_dependentes(conexao, 2, 'Tony Stark')
    #select_dependentes(conexao)

    #delete_empregado(conexao, 2)
    #select_empregado(conexao)

    #delete_dependentes(conexao, 3)
    #select_dependentes(conexao)

    #pesquisar(conexao)

    insert_empregado(conexao, 4, 'Thor', 'Asgard')
