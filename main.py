class DictKeysIterator:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.keys = list(self.dictionary.keys())
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.keys) > self.current:
            index = self.current
            self.current += 1
            return self.keys[index]
        else:
            raise StopIteration


dictionary_example = {'a': 1, 'b': 2, 'c':3}
dict_iter = DictKeysIterator(dictionary_example)
for key in dict_iter:
    print(key)
