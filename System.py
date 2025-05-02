from Node import Node, TextFile, Directory

class System:
    def __init__(self):
        self.__root = Directory('')
        self.__current_node = self.__root

    def __iterate_path(self, path) -> bool:
        current = (self.__root if path[0] == '/' else self.__current_node)
        path_list = list(path.split('/'))
        for name in path_list:
            next = current.find(name)
            if next:
                current = next
            else:
                print('PATH ERROR')
                return False

        self.__current_node = current
        return True

    def mkdir(self, folder_name, path = ''):
        save_current = self.__current_node

        if self.__iterate_path(path):
            if type(self.__current_node) == Directory:
                self.__current_node.add_child(Directory(folder_name, self.__current_node))
            else:
                print('PATH ERROR')

        self.__current_node = save_current

    def touch(self, file_name, path = ''):
        save_current = self.__current_node

        if self.__iterate_path(path):
            if type(self.__current_node) == Directory:
                self.__current_node.add_child(TextFile(file_name, self.__current_node))
            else:
                print('PATH ERROR')

        self.__current_node = save_current

    def rm(self, path):
        save_current = self.__current_node

        if self.__iterate_path(path):
            del self.__current_node

        self.__current_node = save_current

    def cd(self, path):
        if path == '..':
            if self.__current_node.parent:
                self.__current_node = self.__current_node.parent
            return

        save_current = self.__current_node

        if self.__iterate_path(path):
            if type(self.__current_node) == Directory:
                pass
            else:
                print('PATH ERROR')
                self.__current_node = save_current

    def ls(self):
        self.__current_node.ls()

    def nwfiletxt(self, path):
        save_current = self.__current_node

        if self.__iterate_path(path):
            if type(self.__current_node) == TextFile:
                self.__current_node.edit_file()
            else:
                print('PATH ERROR')

        self.__current_node = save_current

    def appendtxt(self, path):
        save_current = self.__current_node

        if self.__iterate_path(path):
            if type(self.__current_node) == TextFile:
                self.__current_node.append_file()
            else:
                print('PATH ERROR')

        self.__current_node = save_current

    def editline(self, path, line_index, text):
        save_current = self.__current_node

        if self.__iterate_path(path):
            if type(self.__current_node) == TextFile:
                self.__current_node.edit_line(line_index - 1, text)
            else:
                print('PATH ERROR')

        self.__current_node = save_current

    def deline(self, path, line_index):
        save_current = self.__current_node

        if self.__iterate_path(path):
            if type(self.__current_node) == TextFile:
                self.__current_node.delete_line(line_index - 1)
            else:
                print('PATH ERROR')

        self.__current_node = save_current

    def cat(self, path):
        save_current = self.__current_node

        if self.__iterate_path(path):
            if type(self.__current_node) == TextFile:
                self.__current_node.show()
            else:
                print('PATH ERROR')

        self.__current_node = save_current

    def mv(self, source_path, destination_path):
        save_current = self.__current_node

        souce_node, destination_node = None, None

        if self.__iterate_path(source_path):
            souce_node = self.__current_node
        self.__current_node = save_current
        if self.__iterate_path(destination_path) and type(self.__current_node) == Directory:
            destination_node = self.__current_node
        self.__current_node = save_current

        if souce_node and destination_node:
            souce_node.move(destination_node)

    def cp(self, source_path, destination_path):
        save_current = self.__current_node

        souce_node, destination_node = None, None

        if self.__iterate_path(source_path):
            souce_node = self.__current_node
        self.__current_node = save_current
        if self.__iterate_path(destination_path) and type(self.__current_node) == Directory:
            destination_node = self.__current_node
        self.__current_node = save_current

        if souce_node and destination_node:
            souce_node.copy(destination_node)

    def rename(self, path, new_name):
        save_current = self.__current_node

        if self.__iterate_path(path):
            self.__current_node.name = new_name

        self.__current_node = save_current
