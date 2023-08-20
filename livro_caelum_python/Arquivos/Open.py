from io import TextIOWrapper
from typing import List


class Open:
    def __init__(self) -> None:
        self.__arquivo: TextIOWrapper = None

    def main(self):
        self.create_file()
        print(type(self.__arquivo))
        self.append_words()
        self.close_file()
        self.open_read_file()
        self.read_file()
    def create_file(self):
        self.__arquivo =  open('file.txt', 'w')

    def open_read_file(self) -> None:
        self.__arquivo =  open('file.txt', 'r')

    def append_words(self) -> None:
        self.__arquivo.write("Loren\nIpsum")

    def close_file(self) -> None:
        self.__arquivo.close()

    def read_file(self) -> None:
        [print(i.strip()) for i in self.__arquivo]

        self.close_file()
        self.open_read_file()

        line = self.__arquivo.readlines()
        print(line)

        self.close_file()
        self.open_read_file()

        line: List = []
        [line.append(i.strip()) for i in self.__arquivo.readlines()]
        print(line)


if __name__ == "__main__":
    Open().main()
