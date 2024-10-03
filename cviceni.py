from abc import ABC, abstractmethod

class Instrument(ABC):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

class StringInstrument(Instrument):
    def __init__(self, name, num_of_strings):
        super().__init__(name)
        self.__num_of_strings = num_of_strings

    def get_num_of_strings(self):
        return self.__num_of_strings

    def set_num_of_strings(self, num_of_strings):
        self.__num_of_strings = num_of_strings

violin = StringInstrument("Violin", 4)

print(f"Name: {violin.get_name()}")
print(f"Number of strings: {violin.get_num_of_strings()}")
