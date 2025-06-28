class WordIterator:
    def __init__(self, sentence):
        self.words = sentence.split()#split() this metod split text and make without space
        self.index=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):#when word end stop
            raise StopIteration
        
        word=self.words[self.index]
        self.index += 1#we make more whats why next time take new character
        return word


exemple1 = "Programming is   awesome!"
it = WordIterator(exemple1)
print(list(it))  

exemple2 = "But sometimes very hard"
it = WordIterator(exemple2)
print(list(it))  