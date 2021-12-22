from pymongo import MongoClient

def verifica(resultado):
    if resultado.acknowledged:
        print("Operação feita com sucesso!")
    else:
        print("Erro de operação!")

if __name__ == '__main__':
    cliente = MongoClient('mongodb://localhost:27017')
    db = cliente['hospital']

    paciente1 = {
        'nome': 'Pedro',
        'ano_nasc': 1998,
        'cpf': '111.222.333-45',
        'enfermidade': 'cisto no rim',
        'leito': 32,
        'alergico': 'amoxicilina',
        'familiares': {
            'pai': 'José',
            'mae': 'Tânia',
            'conjuge': 'Amanda'
        }
    }
    paciente2 = {
        'nome': 'Livia',
        'ano_nasc': 2002,
        'cpf': '333.111.333-66',
        'enfermidade': 'intoxicação alimentar',
        'leito': 50,
        'familiares': {
            'pai': 'Antonio',
            'mae': 'Maria',
        }
    }
    paciente3 = {
        'nome': 'Kleiton',
        'ano_nasc': 1997,
        'cpf': '777.777.777-45',
        'enfermidade': 'braço quebrado',
        'leito': 35,
        'alergico': 'fenitoína',
        'familiares': {
            'pai': 'Gabriel',
            'mae': 'Roberta',
        }
    }

    leito1 = {
        'numero': 32,
        'sala': 10,
        'alergico': 'amoxicilina',
        'medicamento': {
            'antibiotico': 'penicilina',
            'analgesico': 'dipirona'
        }
    }
    leito2 = {
        'numero': 50,
        'sala': 30,
        'medicamento': {
            'analgesico': 'buscopan',
            'procedimento': 'soro fisiologico'
        }
    }
    leito3 = {
        'numero': 35,
        'sala': 15,
        'alergico': 'fenitoina',
        'medicamento': {
            'antibiotico': 'penicilina',
            'analgesico': 'dipirona'
        }
    }

    #result = db.pacientes.insert_one(paciente1)
    #verifica(result)

    #result = db.pacientes.insert_many([paciente2, paciente3])
    #verifica(result)

    #result = db.leitos.insert_many([leito1, leito2, leito3])
    #verifica(result)

    #BUSCAS
    leitos = db.leitos
    pacientes = db.pacientes

    '''filter: {leito: {$gte: 34}}
     $eq = 
     $lt <
     $gte >='''

    '''
    Project: {nome: 1, leito: 1, _id:0} _id:0 desabilita chave primária
    '''
    '''
    sort: {nome: 1} 1 crescente, -1 decrescente
    '''

    """result = pacientes.find({'leito': {'$gte': 35}})
    for i in result:
        print(i)
    print("-"*30)

    result = leitos.find()
    for i in result:
        print(i)"""

    #ATUALIZAR
    '''result = pacientes.find()
    for i in result:
        print(i['nome'])
    print("-"*30)

    result = pacientes.update_one(
        {'cpf': '111.222.333-45'},
        {'$set': {'nome': 'Homem aranha'}}
    )
    verifica(result)

    result = pacientes.find()
    for i in result:
        print(i['nome'])
    print("-"*30)'''

    #EXCLUIR
    '''result = pacientes.find()
    for i in result:
        print(i['nome'])
    result = pacientes.delete_one({'leito': 32})
    verifica(result)

    print("-" * 30)

    result = pacientes.find()
    for i in result:
        print(i['nome'])
    print("-" * 30)'''

    '''result = leitos.find()
    for i in result:
        print(i['numero'])

    result = leitos.delete_one({'numero': 32})
    verifica(result)
    print("-"*20)
    result = leitos.find()
    for i in result:
        print(i['numero'])'''

    #AGREGAÇÃO
    ag1 = {
        '$lookup': {
            'from': 'leitos', #coleção estrangeira
            'localField': 'leito', #coleção local
            'foreignField': 'numero', #campo estrangeiro
            'as': 'LEITO'
        }
    }

    ag2 = {
        '$project': {
            '_id': 0,
            'Nome': '$nome',
            'Ano': '$ano_nasc',
            'Dor': '$enfermidade',
            'Leito': '$leito',
            'Info': {'$arrayElemAt': ['$LEITO', 0]}
        }
    }

    ag3 = {
        '$project': {
            'Nome': '$Nome',
            'Ano': '$Ano',
            'Dor': '$Dor',
            'Leito': '$Leito',
            'Sala': '$Info.sala',
            'Analgesico': '$Info.medicamento.analgesico'
        }
    }

    result = pacientes.aggregate([ag1, ag2, ag3])
    for i in result:
        print('Nome:', i['Nome'])
        print('Ano de Nascimento:', i['Ano'])
        print('Enfermidade:', i['Dor'])
        print('Leito:', i['Leito'])
        print('Sala:', i['Sala'])
        print('Analgésico:', i['Analgesico'])
        print("-"*30)








