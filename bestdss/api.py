"""
Provides a wrapper to the engine class
"""
from . import engine


class DataBase(object):
    """
    A wrapper to use our cool database
    """

    def __init__(self):
        self.engine = engine.Engine()

    def get_table_fields(self, table_name):
        return self.engine.get_fields(table_name)

    def create_table(self, name, *field_names, exists=False):
        return self.engine.create_table(name, *field_names, exists=False)

    def delete_table(self, table_name):
        return self.engine.delete_table(table_name)

    def create_entry(self, table_name, *fields):
        return self.engine.create_entry(table_name, *fields)

    def find_entry(self, table_name, key):
        return self.engine.find_entry(table_name, key)

    def get_entries(self, table_name):
        x = self.engine.get_entries(table_name)
        if x == "not found":
            return {}
        return x

    def delete_entry(self, table_name, key):
        return self.engine.delete_entry(table_name, key)

    def update_entry(self, table_name, key, fields, values):
        return self.engine.update_entry(table_name, key, fields, values)

    def __str__(self):
        return self.engine.__str__()

    def __repr__(self):
        return self.engine.__repr__()
