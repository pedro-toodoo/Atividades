import pymysql.cursors

def insert_cliente(conexao, nome, cpf, endereco, ano_nasc):
    with conexao.cursor() as db:
        sql = 'INSERT INTO Cliente(nome, cpf, endereco, ano_nasc) VALUES(%s, %s, %s, %s)'
        db.execute(sql, (nome, cpf, endereco, ano_nasc))
        conexao.commit()

def update_cliente(conexao, id, ano_nasc):
    with conexao.cursor() as db:
        sql = 'UPDATE Cliente SET ano_nasc = %s WHERE idCliente = %s'
        db.execute(sql, (ano_nasc, id))
        conexao.commit()

def delete_cliente(conexao, id):
    with conexao.cursor() as db:
        sql = 'DELETE FROM Cliente WHERE idCliente = %s'
        db.execute(sql, (id))
        conexao.commit()


if __name__ == '__main__':
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='Par15632@',
        db='banco',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    #inserção de 2 clientes:
    insert_cliente(conexao, 'Naruto', '123.456.789-00', 'Rua Konoha')
    insert_cliente(conexao, 'Gojo', '321.654.987-11', 'Rua Jujutsu')

    update_cliente(conexao, 1, 2002)
    update_cliente(conexao, 2, 2020)

    delete_cliente(conexao, 1)

