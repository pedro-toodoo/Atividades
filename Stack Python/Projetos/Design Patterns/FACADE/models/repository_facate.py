from .delete import Delete
from .insert import Insert
from .select import Select

class Repository:

    def __init__(self):
        self.delete = Delete()
        self.insert = Insert()
        self.select = Select()

    def select_one(self):
        return self.select.select_single_element()

    def select_many(self):
        return self.select.select_many_elements()

    def insert_one(self):
        return self.insert.insert_single_element()

    def insert_many(self):
        return self.select.insert_many_elements()

    def delete_one(self):
        return self.delete.delete_single_element()

    def delete_many(self):
        return self.delete.delete_many_elements()
