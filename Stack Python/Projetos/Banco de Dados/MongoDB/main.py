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
    result = pacientes.find()

    for i in result:
        print(i)




















