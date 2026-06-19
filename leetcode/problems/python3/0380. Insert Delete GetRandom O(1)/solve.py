from random import choice
from typing import Dict, List


class RandomizedSet:
    def __init__(self):
        self.values: List[int] = []
        self.indexes: Dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False

        self.values.append(val)
        self.indexes[val] = len(self.values) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False

        target_index = self.indexes[val]
        last_value = self.values[-1]

        self.values[target_index], self.values[-1] = last_value, val
        self.indexes[last_value] = target_index
        self.values.pop()
        del self.indexes[val]

        return True

    def getRandom(self) -> int:
        return choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
