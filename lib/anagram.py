# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, list):
        matches = []
        for word in list:
            if sorted([letter for letter in word]) == sorted([letter for letter in self.word]):
                matches.append(word)
            else:
                continue
        return matches

