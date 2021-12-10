class HashSet:
    def __init__(self):
        self.buckets = 1000
        self.iter_per_buckets = 1001
        self.set = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def pos(self, key):
        return key // self.buckets

    def add(self, key):
        hash_key = self.hash(key)
        if len(self.set[hash_key]) == 0:
            self.set[hash_key] = [0] * self.iter_per_buckets
        self.set[hash_key][self.pos(key)] = 1
        return

    def remove(self, key):
        hash_key = self.hash(key)
        if len(self.set[hash_key]) != 0:
            self.set[hash_key][self.pos(key)] = 0
        return

    def contains(self, key):
        hash_key = self.hash(key)
        if len(self.set[hash_key]) == 0:
            return False
        else:
            if self.set[hash_key][self.pos(key)] == 0:
                return False
        return True
