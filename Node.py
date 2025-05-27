from copy import deepcopy

RESERVED_CHARACTERS = ['/', '.', '"', '\\', '\'', '$', ' ']

class Node:
    def __init__(self, name, parent = None):
        self.__name = ''
        self.__parent = parent

        self.name = name

    def copy(self, parent):
        node = deepcopy(self)
        parent.add_child(node)
        node.parent = parent

    def move(self, parent):
        if parent.is_ancestor(self):
            print('DIRECTORY ERROR')
            return
        
        self.__parent.remove_child(self)
        parent.add_child(self)
        self.__parent = parent
    
    def delete(self):
        if self.__parent:
            self.__parent.remove(str(self))

    def delete(self):
        if self.__parent:
            self.__parent.remove_child(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        for character in value:
            if character in RESERVED_CHARACTERS:
                print('DIRECTORY NAME ERROR', '| The following characters are reserved:', *RESERVED_CHARACTERS)
                return

        self.__name = value

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        self.__parent = value

    @property
    def path(self):
        return (self.parent.path if self.parent is not None else '') + '/' + self.name

    def __str__(self):
        pass

class TextFile(Node):
    def __init__(self, name, parent = None):
        super().__init__(name, parent)

        self.__lines = list()

        print(f'TEXT FILE "{self}" CREATED SUCCESSFULLY')

    @staticmethod
    def __input_lines():
        lines = list()

        print('Type "/end" for ending')
        while 1:
            line = input(">> ")
            if line.strip() == '/end':
                break
            lines.append(line)

        return lines

    def edit_file(self):
        self.__lines = self.__input_lines()

    def append_file(self):
        self.__lines += self.__input_lines()

    def edit_line(self, line_index: int, text):
        if line_index >= len(self.__lines) or line_index < 0:
            print("LINE INDEX ERROR", '| index is out of range')
            return

        self.__lines[line_index] = text

    def delete_line(self, line_index: int):
        if line_index >= len(self.__lines) or line_index < 0:
            print("LINE INDEX ERROR", '| index is out of range')
            return

        self.__lines.pop(line_index)

    def show(self):
        for index in range(len(self.__lines)):
            print(f'{index + 1}:', self.__lines[index])

    def __str__(self):
        return self.name + '.txt'

class Directory(Node):
    def __init__(self, name, parent = None):
        super().__init__(name, parent)

        self.__childs = list()

        # print(f'DIRECTORY "{self}" CREATED SUCCESSFULLY')

    def __sort_childs(self):
        self.__childs = sorted(self.__childs, key = lambda child: (0 if type(child) == Directory else 1, child.name))

    def is_ancestor(self, value):
        node = self
        while node is not None:
            if node is value:
                return True
            node = node.parent
        
        return False
    
    def ls(self):
        self.__sort_childs()
        for child in self.__childs:
            print(child)

    def find(self, name):
        for child in self.__childs:
            if str(child) == name:
                return child
        return None

    def add_child(self, child):
        self.__childs.append(child)

    def remove_child(self, child):
        self.__childs.remove(child)

    def remove(self, name):
        child = self.find(name)
        if child:
            self.__childs.remove(child)

    def __str__(self):
        return self.name
