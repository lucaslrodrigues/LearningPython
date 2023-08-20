import json
from typing import List

class Kwargs:
    def __init__(self) -> None:
        self.__kwargs: dict = {
            "name": "Linus",
            "last_name": "Torvalds"
        }
        self.__listKwargs: List[dict] = [
            {
                "name": "Maria",
                "last_name": "Famosa"
            }, {
                "name": "Niels",
                "last_name": "Bohr"
            }
        ]

    def main(self) -> None:
        self.showKwargs(self.__kwargs)
        self.showListKwargs(self.__listKwargs)
        self.testJsonToDict(self.__listKwargs)

    def showKwargs(self, kwargs: dict) -> None:
        print(kwargs)

    def showListKwargs(self, *kwargs: List[dict]) -> None:
        print(kwargs)

    def testJsonToDict(self, *kwargs: List[dict]) -> None:
        toJson: List[json] = [json.dumps(i) for i in kwargs]
        print(toJson)
        toDict: List[dict] = [json.loads(i) for i in toJson]
        print(toDict[0][0])


if __name__ == "__main__":
    print(json)
    Kwargs().main()
