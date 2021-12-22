from pymongo import MongoClient

def verifica(r):
    if r.acknowledged:
        print("OK")
    else:
        print("ERRO")

if __name__ == '__main__':
    cliente = MongoClient('mongodb://localhost:27017')
    db = cliente['educação']

    prof1 = {
        "nome": "Pamela",
        "ano_nasc": 1950,
        "cpf": "789.012.345-67",
        "natural": {
            "cidade": "Serra da Saudade",
            "estado": "Minas Gerais",
            "pais": "Brasil"
        }
    }

    prof2 = {
        "nome": "Elza",
        "ano_nasc": 1997,
        "cpf": "901.234.567-89",
        "natural": {
            "cidade": "São Tomé das Letras",
            "estado": "Minas Gerais",
            "pais": "Brasil"
        }
    }

    '''prof = db.professores.insert_many([prof1, prof2])
    verifica(prof)'''

    escola1 = {
        "nome": "Sinhá Moreira",
        "endereco": "Av. Dr. Delfim Moreira",
        "numero": 509,
        "cpf_prof": "789.012.345-67"
    }

    escola2 = {
        "nome": "Zenaide",
        "endereco": "Conj. Hab. Gilberto Rossetti",
        "numero": 332,
        "cpf_prof": "901.234.567-89"
    }

    escola = db.escolas.insert_many([escola1, escola2])
    verifica(escola)












