#1880. Check if Word Equals Summation of Two Words
# O(n) | Space: O(n)
class Solution:
    dictionary = {}
    
    def __init__(self):
        alphabet = list(map(chr, range(97, 123)))
        for i in range(len(alphabet)):
            self.dictionary[alphabet[i]] = i
    
    def sumWord(self, word):
        curry = []
        match_first_number = False
        for l in word:
            n = self.dictionary[l]
            if n != 0:
                match_first_number = True
                curry.append(str(n))
            if n == 0 and match_first_number == True:
                curry.append(str(n))
        
        if len(curry) == 0:
            return 0
        return int("".join(curry))
        
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.sumWord(firstWord) + self.sumWord(secondWord) == self.sumWord(targetWord)