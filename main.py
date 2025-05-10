class Slot:
    def __init__(self):
        self.status = "never used"  # "never used", "occupied", or "tombstone"
        self.key = None

class HashTable:
    def __init__(self):
        self.table = [Slot() for _ in range(26)]

    def _hash(self, key):
        return ord(key[-1]) - ord('a')

    def search(self, key):
        idx = self._hash(key)
        start = idx
        while True:
            slot = self.table[idx]
            if slot.status == "never used":
                return -1
            if slot.status == "occupied" and slot.key == key:
                return idx
            idx = (idx + 1) % 26
            if idx == start:
                return -1

    def insert(self, key):
        if self.search(key) != -1:
            return
        idx = self._hash(key)
        start = idx
        while True:
            slot = self.table[idx]
            if slot.status in ("never used", "tombstone"):
                slot.key = key
                slot.status = "occupied"
                return
            idx = (idx + 1) % 26
            if idx == start:
                return

    def delete(self, key):
        idx = self.search(key)
        if idx != -1:
            self.table[idx].status = "tombstone"
            self.table[idx].key = None

    def output(self):
        result = []
        for slot in self.table:
            if slot.status == "occupied":
                result.append(slot.key)
        print(" ".join(result))

def main():
    import sys
    ops = input().strip().split()
    table = HashTable()
    for op in ops:
        if op.startswith("A"):
            table.insert(op[1:])
        elif op.startswith("D"):
            table.delete(op[1:])
    table.output()

if __name__ == "__main__":
    main()
