from Node import TextFile, Directory

class System:
    def __init__(self):
        self.__root = Directory('root')
        self.__current_node = self.__root

    def __iterate_path(self, path, type = None):
        current = (self.__root if path[0] == '/' else self.__current_node)
        path_list = list(path.split('/'))
        for name in path_list:
            next = current.find(name)
            if next:
                current = next
            else:
                print('PATH ERROR')
                return None

        if type and type(current) != type:
            print('PATH ERROR')
            return None

        return current

    def current_path(self):
        return self.__current_node.path

    def mkdir(self, folder_name, path = ''):
        node = self.__iterate_path(path, Directory)
        if node:
            node.add_child(Directory(folder_name, node))

    def touch(self, file_name, path = ''):
        node = self.__iterate_path(path, Directory)
        if node:
            node.add_child(TextFile(file_name, node))

    def rm(self, path):
        node = self.__iterate_path(path)
        if node:
            del node

    def cd(self, path):
        if path == '..':
            if self.__current_node.parent:
                self.__current_node = self.__current_node.parent
            return

        node = self.__iterate_path(path, Directory)
        if node:
            self.__current_node = node

    def ls(self):
        self.__current_node.ls()

    def nwfiletxt(self, path):
        node = self.__iterate_path(path, TextFile)
        if node:
            node.edit_file()

    def appendtxt(self, path):
        node = self.__iterate_path(path, TextFile)
        if node:
            node.append_file()

    def editline(self, path, line_index, text):
        node = self.__iterate_path(path, TextFile)
        if node:
            node.edit_line(line_index - 1, text)

    def deline(self, path, line_index):
        node = self.__iterate_path(path, TextFile)
        if node:
            node.delete_line(line_index - 1)

    def cat(self, path):
        node = self.__iterate_path(path, TextFile)
        if node:
            node.show()

    def mv(self, source_path, destination_path):
        source_node, destination_node = self.__iterate_path(source_path), self.__iterate_path(destination_path, Directory)
        if source_node and destination_node:
            source_node.move(destination_node)

    def cp(self, source_path, destination_path):
        source_node, destination_node = self.__iterate_path(source_path), self.__iterate_path(destination_path, Directory)
        if source_node and destination_node:
            source_node.copy(destination_node)

    def rename(self, path, new_name):
        node = self.__iterate_path(path)
        if node:
            node.name = new_name
