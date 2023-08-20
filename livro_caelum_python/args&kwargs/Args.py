import json


class Args:
    def __init__(self) -> None:
        self.valores: tuple = (
            "Linus", "Torvalds", "creates", "Linux"
        )
        self.person: dict = {
            "name": "Linus",
            "last_name": "Torvalds"
        }

    def main(self):
        self.showValues(self.valores[0], self.valores[1:])
        print(self.getJson(self.person))

    def showValues(self, arg: str, *args: tuple):
        print(f'%s %s' % (arg, args))

    def getJson(self, person: dict) -> json:
        return json.dumps(person)


if __name__ == "__main__":
    Args().main()
