import re
from bestdss import engine


class Interpreter(object):
    def __init__(self):
        """
        Contains the definitions of our regex patterns to database commands
        Compiling them only once allows a big bump in performance.
        """
        self.DECLARE = re.compile(r'DECLARE +(\w+) +AS +(\w+(, *\w+)*)')
        self.engine = engine.Engine()

        self.ADD = re.compile(
            r"""ADD +\(((?:"(?:(?:\w|')+)"|'(?:\w+)')(?:, *(?:"(?:(?:\w|')+)"|'(?:\w+)'))*)\) +TO +(\w+)""")

        self.FIND = re.compile(
            r"""FIND +("(?:(?:\w|')+)"|'(?:\w+)'|ALL) +IN +(\w+)""")

        self.UPDATE = re.compile(
            r"""UPDATE +("(?:(?:\w|')+)"|'(?:\w+)') +IN +(\w+) +SET +(\w+) *= *("(?:(?:\w|')+)"|'(?:\w+)')""")

        self.DELETE = re.compile(
            r"""DELETE +("(?:(?:\w|')+)"|'(?:\w+)') +FROM +(\w+)""")

    def update(self, expression):
        try:
            y = self.UPDATE.match(expression)
            # [1:-1] to remove quotes at the begin and end of string
            user_id = y.group(1)[1:-1]
            table_name = y.group(2)
            field_name = y.group(3)
            value = y.group(4)[1:-1]
            return self.engine.update_entry(table_name, user_id, [
                field_name], [value])
        except:
            return False

    def declare(self, expression):
        try:
            y = self.DECLARE.match(expression)
            table_name = y.group(1)
            fields = y.group(2).split(',')
            return self.engine.create_table(table_name, *fields)
        except:
            return False

    def add(self, expression):
        try:
            y = self.ADD.match(expression)
            # [1:-1] to remove quotes at the begin and end of string
            values = [i.strip()[1:-1] for i in y.group(1).split(',')]
            table = y.group(2)
            return self.engine.create_entry(table, *values)
        except:
            return False

    def find(self, expression):
        try:
            y = self.FIND.match(expression)
            table = y.group(2)
            if y.group(1) == 'ALL':
                return self.engine.get_entries(table)
            # [1:-1] to remove quotes at the begin and end of string
            return self.engine.find_entry(table, y.group(1)[1:-1])
        except:
            return False

    def delete(self, expression):
        try:
            y = self.DELETE.match(expression)
            # [1:-1] to remove quotes at the begin and end of string
            key = y.group(1)[1:-1]
            table = y.group(2)
            return self.engine.delete_entry(table, key)
        except:
            return False

    def parse_text(self, text):
        found = self.find(text)
        if found:
            return found
        return self.delete(text) or self.declare(text) or self.add(text) or self.update(text)

    def prompt(self):
        while True:
            try:
                user_input = input('> ').strip()
            except:
                print()
                break
            if user_input == "":
                continue
            res = self.parse_text(user_input)
            if res == "not found":
                continue
            elif not res:
                print('* ERROR')
            elif isinstance(res, list):
                represent = "'"+"','".join(res)+"'"
                print(f'* {represent}')
            elif isinstance(res, tuple):
                represent = "'"+"','".join(res)+"'"
                print(f'* {represent}')
            elif isinstance(res, dict):
                entries = list(res.values())
                for entry in entries:
                    represent = "'"+"','".join(entry)+"'"
                    print(f'* {represent}')
            else:
                print(f'* OK')
