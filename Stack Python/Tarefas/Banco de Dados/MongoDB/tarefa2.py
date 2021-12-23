from pymongo import MongoClient

def verifica(resultado):
    if resultado.acknowledged:
        print("Operação feita com sucesso!")
    else:
        print("Erro de operação!")

if __name__ == '__main__':
    cliente = MongoClient('mongodb://localhost:27017')
    db = cliente['educação']

    escola = db.escolas
    prof = db.professores

    busca_escola = escola.find({'nome': {'$regex': 'r'}, 'numero': {'$lte': 400}}, {'_id': 0}) #509
    for i in busca_escola:
        print(f"Nome: {i['nome']}")
        print(f"Endereço: {i['endereco']}")
        print(f"Número: {i['numero']}")

    print("-"*20)

    busca_prof1 = prof.find({'$or': [{'ano_nasc': {'$lte': 1990}, 'natural.estado': 'Minas Gerais'}]}, {'_id': 0})
    for i in busca_prof1:
        print(f"Nome: {i['nome']}")
        print(f"Estado: {i['natural']['estado']}")
        print(f"Cidade: {i['natural']['cidade']}")

    print("-"*20)

    busca_prof2 = prof.find({'$or': [{'nome': {'$regex': 'a$'}, 'ano_nasc': {'$lte': 1980},
                                      'ano_nasc': {'$gt': 1987}}]})
    #busca_prof2 = prof.find({'nome': {'$regex': 'a$'}, 'ano_nasc': {'$lte': 1980}})
    for i in busca_prof2:
        print(f"Nome: {i['nome']}")
        print(f"Ano de nascimento: {i['ano_nasc']}")







