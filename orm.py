from bestdss import api


db = api.DataBase()


class Model(object):
    """
    You need to override this model class with a class of your own.
    The convention used by this ORM is that the model's name is the same as the table's name but without s at the end.
    eg: table -> users , model -> user ( or User)
    """

    def __init__(self):
        pass

    @classmethod
    def get(cls, key):
        return cls.entry_to_object(db.find_entry(cls.__name__.lower()+'s', key))

    @classmethod
    def get_all(cls):
        return [cls.entry_to_object(i) for i in db.get_entries(cls.__name__.lower()+'s')]

    @classmethod
    def save(cls, new):
        db.create_entry(cls.__name__.lower()+'s', *cls.object_to_entry(new))

    @classmethod
    def entry_to_object(cls, entry):
        obj = cls()
        fields = db.get_table_fields(cls.__name__.lower()+'s')
        for i in range(len(fields)):
            setattr(obj, fields[i], entry[i])
        return obj

    @classmethod
    def object_to_entry(cls, obj):
        fields = db.get_table_fields(cls.__name__.lower()+'s')
        entry = []
        for field in fields:
            entry.append(getattr(obj, field))
        return entry

# example:


class User(Model):
    pass
