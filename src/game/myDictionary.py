'''
Created on Nov 20, 2015

@author: mrthinks@gmail.com
'''

# ~/.pyenv/versions/3.4.3/lib/python3.4/site-packages/konlpy/java/data/kE
#dicPath = '/home/mrthink/.pyenv/versions/3.4.3/lib/python3.4/site-packages/konlpy/java/data/kE/dic_system.txt'
dicPath = '/usr/local/lib/python3.4/dist-packages/konlpy/java/data/kE/dic_system.txt'

class MyDictionary():
    dic = None 
    
    def loadDic(self):
        if self.dic is not None:
            return
        self.dic = dict()
            
        with open(dicPath) as f:
            lines = f.readlines()
            
            for line in lines:
                word = line.split()[0]
                start_c = word[0]
                
                dic2 = self.dic.get(start_c)
                if dic2 is None :
                    dic2 = set()
                    self.dic[start_c] = dic2
                dic2.add(word)

        
    def __init__(self):
        self.loadDic()
        return
    
    def isExist(self, word):
        self.loadDic()
        if len(word) <= 0:
            return False
        
        if word[0] in self.dic:
            return word in self.dic[word[0]]
        else:
            return False
    
    def isExistStartLetter(self, letter):
        self.loadDic()

        if letter in self.dic:
            return True
        else:
            return False
    
    def getSubWord(self, letter):
        return self.dic[letter]

myDictionary = MyDictionary()

if __name__ == '__main__':
        print(myDictionary.isExist("AIDS"))
        print(myDictionary.isExist("ADIDAS"))
