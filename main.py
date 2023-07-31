class PalindromeIterator:
    def __init__(self, list):
        self.current = 0
        self.words = list

    def __iter__(self):
        return self

    def is_palindrome(self, word):
        return word == word[::-1]

    def __next__(self):
        while self.current < len(self.words):
            current_word = self.words[self.current]
            self.current += 1
            if self.is_palindrome(current_word):
                return current_word
        raise StopIteration


words_list = ['level', 'racecar', 'python', 'madam']
palindrome_iter = PalindromeIterator(words_list)
for word_example in palindrome_iter:
    print(word_example)
