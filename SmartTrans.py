from googletrans import LANGUAGES
import requests
from collections import Counter
from textblob import TextBlob
from googletrans import Translator

def getLangString(lang):
    LANGCODES = dict(map(reversed, LANGUAGES.items()))
    simbols = list(LANGCODES.values())
    strings = list(LANGCODES.keys())
    simbolIndex = simbols.index(lang)
    langString = strings[simbolIndex]
    return langString

def langExists(lang):
    LANGCODES = dict(map(reversed, LANGUAGES.items()))
    simbols = list(LANGCODES.values())
    return lang in simbols

def getCountryLang(countryCode):
    link = "https://restcountries.eu/rest/v2/alpha/" + countryCode
    response = requests.get(link).json()
    langSimbol = response["languages"][0]["iso639_1"]
    return langSimbol

def getCountryCode():
    link = "http://ip-api.com/json"
    response = requests.get(link).json()
    return response['countryCode']

def getWords(sentence):
    words = sentence.split()
    return words






def countWords(sentence):
    words = getWords(sentence)
    wordCounter = Counter(words)
    count = sum(wordCounter.values())
    return count



def getUniqueWords(sentence):
    words = getWords(sentence)
    wordCounter = Counter(words)
    uniqueWords = wordCounter.keys()
    return uniqueWords




def doTranslate(translator, sentence, langFrom, langTo):
    trans = translator.translate(sentence, src=langFrom, dest=langTo)
    transText = trans.text
    return transText



def getSentence():
    sentence = ":)"
    reenter = True
    while reenter:
        print("Enter the Sentence you want to translate:")
        sentence = input()
        print("*** *** ***")
        
        if sentence.lower() == "end":
            raise StopIteration
    
        count = countWords(sentence)
        print("Sentence has", count, "words.")
        if count > 10 :
            reenter = True
            print("Sentence is long!!!")
        else:
            reenter = False
    return sentence





def getSentements(statement) :
    sentiment = TextBlob(statement)
    ploarity = sentiment.sentiment.polarity
    if ploarity > 0.5 :
        return "Positive"
    else :
        return "Negative"




