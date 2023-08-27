from io import TextIOWrapper
from typing import List


class OpenFile:
    def __init__(self) -> None:
        self.__arquivo: TextIOWrapper = None

    def create_file(self):
        self.__arquivo =  open('palavras.txt', 'w')

    def open_read_file(self) -> None:
        self.__arquivo =  open('palavras.txt', 'r')

    def append_words(self, text: str) -> None:
        self.__arquivo.write(text)

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
