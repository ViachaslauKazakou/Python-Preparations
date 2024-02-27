class MyDictionary:
    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def __getitem__(self, key):
        hash_key = hash(key) % self.size
        while self.keys[hash_key] != key:
            hash_key = (hash_key + 1) % self.size
        return self.values[hash_key]

    def __setitem__(self, key, value):
        hash_key = hash(key) % self.size
        while self.keys[hash_key] is not None and self.keys[hash_key] != key:
            hash_key = (hash_key + 1) % self.size
        self.keys[hash_key] = key
        self.values[hash_key] = value


mydict = MyDictionary()

print(mydict.keys)
