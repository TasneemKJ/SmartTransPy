from googletrans import LANGUAGES
from googletrans import Translator
from collections import Counter
from textblob import TextBlob
import requests

class SmartTrans :
    """A library for smart language translation.

    """
    
    def __init__(self, translator = None):
        """The constructor of the SmartTrans class
        
        Args:
            translator: a translator of type Translator (default = None)
        """
        self.translator = translator
         
    def getTranslator(self):
        """Get the translator
        
        Returns:
            an instance of type Translator
        """
        
        if self.translator == None :
            self.translator = Translator()
        return self.translator 
    
    def detectLanguage(self, sentence):
        """Detect the language of the sentence.
    
        Args:
            sentence: the sentence to detect language of
            
        Returns:
            a dictionary of the detected language
        """
        return self.getTranslator().detect(sentence)
    
    def getLangString(self, lang_code):  
        """Get the language string from the language code.
        
        Note:
            The function uses the languages codes in LANGUAGES module
    
        Args:
            lang_code: the language code
            
        Returns:
            The String of the language
        """
        LANGCODES = dict(map(reversed, LANGUAGES.items()))
        simbols = list(LANGCODES.values())
        strings = list(LANGCODES.keys())
        simbolIndex = simbols.index(lang_code)
        langString = strings[simbolIndex]
        return langString
    
    def langExists(self, lang_code):
        """Check if the language code is valid and exists in the library.
        
        Note:
            The function uses the languages codes in LANGUAGES module
    
        Args:
            lang_code: the language code
            
        Returns:
            True is the language code exists in LANGUAGES
        """
        LANGCODES = dict(map(reversed, LANGUAGES.items()))
        simbols = list(LANGCODES.values())
        return lang_code in simbols
   
    def getCountryLang(self, country_code):    
        """Get the language code of a country from the country code.
        
        Note:
            this function uses restcountries REST API 
    
        Args:
            country_code: the code of the country
            
        Returns:
            the code of the main language of the country
        """
        link = "https://restcountries.eu/rest/v2/alpha/" + country_code
        response = requests.get(link).json()
        langSimbol = response["languages"][0]["iso639_1"]
        return langSimbol
    
    def getCountryCode(self):
        """Get the code of the country the program is running from.
        
        Note:
            this function uses ip-api REST API 
        
        Returns:
            The code of current country
        """
        link = "http://ip-api.com/json"
        response = requests.get(link).json()
        return response['countryCode']
    
    def getWords(self, sentence):
        """Split a sentence into words using space delimiter.
        
        Args:
            sentence: the sentence to split
        """
        words = sentence.split()
        return words
    
    def countWords(self, sentence):
        """Count the words in a sentence.
        
        Note:
            The function uses Counter module to count the words
        
        Args:
            sentence: the sentence to count words in
            
        Returns:
            the number of words in the sentence
        """
        words = self.getWords(sentence)
        wordCounter = Counter(words)
        count = sum(wordCounter.values())
        return count
    
    def getUniqueWords(self, sentence):
        """Get the unique words in a sentence.
        
        Note:
            The function uses Counter module to count the words
        
        Args:
            sentence: the sentence
            
        Returns:
            a list of the unique words in the sentence
        """
        words = self.getWords(sentence)
        wordCounter = Counter(words)
        uniqueWords = wordCounter.keys()
        return uniqueWords
    
    def doTranslate(self, sentence, lang_from="en", lang_to="en"):
        """Translates a sentence from alanguage to a nother.
        
        Args:
            sentence: the sentence to translate
            lang_from: the language to translate the sentence from (default="en")
            lang_to: the language to translate the sentence to (default="en")
            
        Returns:
            The translated sentence
        """
        trans = self.getTranslator().translate(sentence, src=lang_from, dest=lang_to)
        return trans.text
    
    def getSentence(self):
        """Requests a sentence from user.
        
        Note:
            the sentense should countain 10 words as maximum. If the sentence is long,
            the input is requested again.
        
            if "end" is entered, StopIteration exception is thrown
            
        Returns:
            The sentence entered by the user
        """
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
    
    def getSentements(self, sentence) :
        """Gets the sentements of a sentence.
        Note:
            The function uses TextBlob library to get the sentements
        
        Args:
            sentence: the sentence to translate
            
        Returns:
            a string containing "Positive" if the sentence is positive, or it returns "Negative"
        """
        sentiment = TextBlob(sentence)
        ploarity = sentiment.sentiment.polarity
        if ploarity > 0.5 :
            return "Positive"
        else :
            return "Negative"




