#!/bin/python3
import os
import json
import shutil
from . import helpers


class Table(object):
    "Represents a table in our database having a schema and entries"

    def __init__(self, table_name, *field_names, exists=False):
        self.entries = {}
        self.table_name = table_name
        self.storage_path = f'storage/{table_name}/'
        self.entries_path = self.storage_path + 'entries/'
        self.ensure_storage_folder()

        if exists:
            self.fields = self.get_schema_from_storage()
            self.fields = [i.strip() for i in self.fields]
        else:
            self.fields = list(field_names)
            self.fields = [i.strip() for i in self.fields]
            self.save_schema()

        self.primary_key = self.fields[0]

    def all_entries(self):
        if not self.all_entries_cached:
            for entry in helpers.get_subfiles(self.entries_path):
                if not entry in self.entries:
                    self.get_entry_from_storage(entry)
        self.all_entries_cached = True
        return self.entries if len(self.entries) else "not found"

    def add_entry(self, *entry):
        "adds an entry to the list in cache and to persistant storage"
        if len(entry) != len(self.fields):
            return False
        entry_primary_key = entry[0]
        if self.entry_exists(entry_primary_key):
            return False
        self.entries[entry_primary_key] = list(entry)
        self.persist_entry_to_storage(entry)
        return True

    def save_schema(self):
        "saves the Table fields so they can be restored in later use"
        with open(self.storage_path + 'schema', 'w') as outfile:
            json.dump(self.fields, outfile)

    def serialize_object(self, obj, file, is_entry=True):
        "used to save entries and schema to storage"
        file_path = self.entries_path + \
            file if is_entry else self.storage_path + file
        with open(file_path, 'w') as outfile:
            json.dump(obj, outfile)

    def ensure_storage_folder(self):
        """makes sure the storage skeleton is what it needs to be ,
        all entries cached means that all entries are currently in cache
        and thus no need to search in storage"""
        try:
            os.makedirs(self.storage_path)
            os.makedirs(self.entries_path)
            self.all_entries_cached = True
        except OSError:
            self.all_entries_cached = False

    def delete_entry(self, key):
        try:
            self.storage_delete_entry(key)
            del self.entries[key]
            return True
        except:
            return False

    def get_entry_from_storage(self, key, check_only=False):
        "reads an entry from persistant storage to cache"

        if check_only:
            return not self.all_entries_cached and os.path.isfile(f'{self.entries_path}{key}')
        try:
            with open(f'{self.entries_path}{key}') as json_data:
                entry_data = json.load(json_data)
                self.entries[key] = entry_data
                return entry_data
        except:
            return "not found"

    def get_schema_from_storage(self):
        "reads the table schema from storage"
        # try:
        with open(self.storage_path + 'schema') as json_data:
            return json.load(json_data)
        # except:
        #     raise Exception('Schema file not found')

    def entry_exists(self, key):
        "checks if an entry exists"
        return key in self.entries or self.get_entry_from_storage(key, check_only=True)

    def find_entry(self, key):
        "returns the entry if it exists in cache , else looks for it in storage"
        if key in self.entries:
            return self.entries[key]
        return self.get_entry_from_storage(key)

    def update_entry(self, key, difference):
        """updates an entry , takes a key and dictionary argument containing the changes
        eg:{'name':'ghazi'}
        """
        # can't find entry to change
        if not self.entry_exists(key):
            return False
        # changing entry primary key to an existing entry
        if self.primary_key in difference and difference[self.primary_key] in self.entries:
            return False
        old_name = key
        if not key in self.entries:
            self.get_entry_from_storage(key)

        for i in difference.keys():
            val_index = self.fields.index(i)
            self.entries[key][val_index] = difference[i]
            if val_index == 0:
                # changing the primary key
                self.entries[difference[i]] = self.entries.pop(key)
                key = difference[i]
        self.storage_delete_entry(old_name)
        self.persist_entry_to_storage(self.entries[key])
        return True

    def persist_entry_to_storage(self, entry):
        "writes an entry to storage"
        self.serialize_object(entry, entry[0])

    def delete_storage(self):
        "deletes the table from storage"
        shutil.rmtree(self.storage_path)

    def storage_delete_entry(self, key):
        "deletes an entry from storage if it exists"
        try:
            os.unlink(f'{self.entries_path}{key}')
            return True
        except:
            return False

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return json.dumps(self.__dict__)
