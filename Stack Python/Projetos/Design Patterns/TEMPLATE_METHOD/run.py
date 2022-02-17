from template import AlgorithmTemplate

class CSV_Processor(AlgorithmTemplate):
    def insert_value_in_doc(self,formatted_data_with_id):
        print('Connecting from CSV file')
        print(formatted_data_with_id)
        print('Saving data')

class DB_Processor(AlgorithmTemplate):
    def insert_value_in_doc(self,formatted_data_with_id):
        print('Connecting from Mysql DB...')
        print(formatted_data_with_id)
        print('Saving DB')

data1 = ['Pedro', 'Python', 'Toodoo']
csvProcessor = CSV_Processor()
csvProcessor.insert_data(data1)

DBProcessor = DB_Processor()
DBProcessor.insert_data(data1)