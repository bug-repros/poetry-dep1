from typing import Set


class Dep:
    def __init__(self, names: Set[str]):
        self.__names = names

    def has_name(self, name: str):
        return name in self.__names
