from pymongo import MongoClient

def verifica(r):
    if r.acknowledged:
        print("OK")
    else:
        print("ERRO")

if __name__ == '__main__':
    cliente = MongoClient('mongodb://localhost:27017')
    db = cliente['educação']

    ag1 = {
        '$lookup': {
            'from': 'escolas',
            'localField': 'cpf',
            'foreignField': 'cpf_prof',
            'as': 'CPF'
        }
    }

    ag2 = {
        '$project': {
            '_id': 0,
            'Nome': '$nome',
            'Cidade': '$natural.cidade',
            'Ano': '$ano_nasc',
            'Info': {'$arrayElemAt': ['$CPF', 0]}
        }
    }

    ag3 = {
        '$project': {
            'Nome': '$Nome',
            'Cidade': '$Cidade',
            'Ano': '$Ano',
            'Escola': '$Info.nome'
        }
    }

    result = db.professores.aggregate([ag1, ag2, ag3])
    for i in result:
        print(f"Nome: {i['Nome']}")
        print(f"Cidade Natal: {i['Cidade']}")
        print(f"Ano de Nascimento: {i['Ano']}")
        print(f"Escola: {i['Escola']}")
        print("-"*20)







