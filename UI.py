from System import System

class UI:
    def __init__(self, username):
        self.__username = username
        self.__system = System()
        self.__run()

    def __run(self):
        while 1:
            command = input(self.__username + '@' + self.__system.current_path() + ' $ ')
            command = list(command.split())

            match command[0]:
                case 'mkdir':
                    match len(command):
                        case 2:
                            self.__system.mkdir(command[1])
                        case 3:
                            self.__system.mkdir(command[2], command[1])
                        case _:
                            print('WRONG COMMAND')

                case 'touch':
                    match len(command):
                        case 2:
                            self.__system.touch(command[1][:-4])
                        case 3:
                            self.__system.touch(command[2][:-4], command[1])
                        case _:
                            print('WRONG COMMAND')

                case 'rm':
                    match len(command):
                        case 2:
                            self.__system.rm(command[1])
                        case _:
                            print('WRONG COMMAND')

                case 'cd':
                    match len(command):
                        case 2:
                            self.__system.cd(command[1])
                        case _:
                            print('WRONG COMMAND')

                case 'nwfiletxt':
                    match len(command):
                        case 2:
                            self.__system.nwfiletxt(command[1])
                        case _:
                            print('WRONG COMMAND')

                case 'appendtxt':
                    match len(command):
                        case 2:
                            self.__system.appendtxt(command[1])
                        case _:
                            print('WRONG COMMAND')

                case 'editline':
                    match len(command):
                        case 4:
                            self.__system.editline(command[1], command[2], command[3])
                        case _:
                            print('WRONG COMMAND')

                case 'deline':
                    match len(command):
                        case 3:
                            self.__system.deline(command[1], command[2])
                        case _:
                            print('WRONG COMMAND')

                case 'cat':
                    match len(command):
                        case 2:
                            self.__system.cat(command[1])
                        case _:
                            print('WRONG COMMAND')

                case 'mv':
                    match len(command):
                        case 3:
                            self.__system.mv(command[1], command[2])
                        case _:
                            print('WRONG COMMAND')

                case 'cp':
                    match len(command):
                        case 3:
                            self.__system.cp(command[1], command[2])
                        case _:
                            print('WRONG COMMAND')

                case 'rename':
                    match len(command):
                        case 3:
                            self.__system.rename(command[1], command[2])
                        case _:
                            print('WRONG COMMAND')

                case 'ls':
                    match len(command):
                        case 1:
                            self.__system.ls()
                        case _:
                            print('WRONG COMMAND')


                case 'shutdown':
                    match len(command):
                        case 1:
                            break
                        case _:
                            print('WRONG COMMAND')

                case _:
                    print('WRONG COMMAND')
