import json
import os
from . import helpers
from . import table


class Engine(object):
    """
    The main class , is constitued of tables and passes update operations to concerned table instance
    """

    def __init__(self):
        try:
            os.makedirs('storage')
        except OSError:
            pass
        self.tables = {}
        for i in helpers.get_subdirs('storage'):
            try:
                self.create_table(i, exists=True)
            except:
                pass

    def get_fields(self, table_name):
        if table_name in self.tables:
            return self.tables[table_name].field_names
        raise Exception('table not exist')

    def create_table(self, name, *field_names, exists=False):
        if name in self.tables:
            return False
        self.tables[name] = table.Table(name, *field_names, exists=exists)
        return True

    def delete_table(self, table_name):
        if not table_name in self.tables:
            return False
        self.tables[table_name].delete_storage()
        del self.tables[table_name]
        return True

    def create_entry(self, table_name, *fields):
        return self.tables[table_name].add_entry(*fields)

    def find_entry(self, table_name, key):
        return self.tables[table_name].find_entry(key)

    def get_entries(self, table_name):
        return self.tables[table_name].all_entries()

    def delete_entry(self, table_name, key):
        return self.tables[table_name].delete_entry(key)

    def update_entry(self, table_name, key, fields, values):
        difference = {}
        if len(fields) != len(values):
            return False
        for i in range(len(fields)):
            difference[fields[i]] = values[i]
        return self.tables[table_name].update_entry(key, difference)

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return json.dumps(self.__dict__)
