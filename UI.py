from System import System

class UI:
    def __init__(self):
        self.__system = System()
        self.__run()

    def __run(self):
        while 1:
            command = input(self.__system.current_path() + ' ')

            pass