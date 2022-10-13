from Linked_list import Linked_list
from Hash_function import h


class Hash_table:
    def __init__(self, function, size):
        if function == "d":
            self.function = "d"
        elif function == "m":
            self.function = "m"
        else:
            print("error")
            return
        self.table = []
        for i in range(0, size):
            self.table.append(Linked_list())
        self.n = 0

    def get_size(self):
        return len(self.table)

    def get_table(self):
        return self.table

    def get_n(self):
        return self.n

    def insert(self, value):
        self.table[h(value, self.function, self.get_size())].add(value)
        self.n = self.n + 1

    def find(self, value):
        return self.table[h(value, self.function, self.get_size())].search(value)

    def delete(self, value):
        self.table[h(value, self.function, self.get_size())].remove(value)



