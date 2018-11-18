from googletrans import LANGUAGES
from googletrans import Translator
from collections import Counter
from textblob import TextBlob
import requests

class SmartTrans :
    
    def __init__(self, translator = None):
        self.translator = translator
         
    def getTranslator(self):
        if self.translator == None :
            self.translator = Translator()
        return self.translator 
    
    def detectLanguage(self, sentence):
        return self.getTranslator().detect(sentence)
    
    def getLangString(self, lang):
        LANGCODES = dict(map(reversed, LANGUAGES.items()))
        simbols = list(LANGCODES.values())
        strings = list(LANGCODES.keys())
        simbolIndex = simbols.index(lang)
        langString = strings[simbolIndex]
        return langString
    
    def langExists(self, lang):
        LANGCODES = dict(map(reversed, LANGUAGES.items()))
        simbols = list(LANGCODES.values())
        return lang in simbols
    
    def getCountryLang(self, countryCode):
        link = "https://restcountries.eu/rest/v2/alpha/" + countryCode
        response = requests.get(link).json()
        langSimbol = response["languages"][0]["iso639_1"]
        return langSimbol
    
    def getCountryCode(self):
        link = "http://ip-api.com/json"
        response = requests.get(link).json()
        return response['countryCode']
    
    def getWords(self, sentence):
        words = sentence.split()
        return words
    
    def countWords(self, sentence):
        words = self.getWords(sentence)
        wordCounter = Counter(words)
        count = sum(wordCounter.values())
        return count
    
    def getUniqueWords(self, sentence):
        words = self.getWords(sentence)
        wordCounter = Counter(words)
        uniqueWords = wordCounter.keys()
        return uniqueWords
    
    def doTranslate(self, sentence, langFrom, langTo):
        trans = self.getTranslator().translate(sentence, src=langFrom, dest=langTo)
        return trans.text
    
    def getSentence(self):
        sentence = ":)"
        reenter = True
        while reenter:
            print("Enter the Sentence you want to translate:")
            sentence = input()
            print("*** *** ***")
            
            if sentence.lower() == "end":
                raise StopIteration
        
            count = self.countWords(sentence)
            print("Sentence has", count, "words.")
            if count > 10 :
                reenter = True
                print("Sentence is long!!!")
            else:
                reenter = False
        return sentence
    
    def getSentements(self, statement) :
        sentiment = TextBlob(statement)
        ploarity = sentiment.sentiment.polarity
        if ploarity > 0.5 :
            return "Positive"
        else :
            return "Negative"




