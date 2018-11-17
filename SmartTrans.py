
# coding: utf-8

# In[1]:


from googletrans import LANGUAGES
def getLangString(lang):
    LANGCODES = dict(map(reversed, LANGUAGES.items()))
    simbols = list(LANGCODES.values())
    strings = list(LANGCODES.keys())
    simbolIndex = simbols.index(lang)
    langString = strings[simbolIndex]
    return langString


# In[2]:


from googletrans import LANGUAGES
def langExists(lang):
    LANGCODES = dict(map(reversed, LANGUAGES.items()))
    simbols = list(LANGCODES.values())
    return lang in simbols


# In[3]:


import requests
def getCountryLang(countryCode):
    link = "https://restcountries.eu/rest/v2/alpha/" + countryCode
    response = requests.get(link).json()
    langSimbol = response["languages"][0]["iso639_1"]
    return langSimbol


# In[4]:


import requests
def getCountryCode():
    link = "http://ip-api.com/json"
    response = requests.get(link).json()
    return response['countryCode']


# In[5]:


def getWords(sentence):
    words = sentence.split()
    return words


# In[6]:


from collections import Counter
def countWords(sentence):
    words = getWords(sentence)
    wordCounter = Counter(words)
    count = sum(wordCounter.values())
    return count


# In[7]:


from collections import Counter
def getUniqueWords(sentence):
    words = getWords(sentence)
    wordCounter = Counter(words)
    uniqueWords = wordCounter.keys()
    return uniqueWords


# In[8]:


def doTranslate(translator, sentence, langFrom, langTo):
    trans = translator.translate(sentence, src=langFrom, dest=langTo)
    transText = trans.text
    return transText


# In[9]:


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


# In[10]:


from textblob import TextBlob
def getSentements(statement) :
    sentiment = TextBlob(statement)
    ploarity = sentiment.sentiment.polarity
    if ploarity > 0.5 :
        return "Positive"
    else :
        return "Negative"


# In[ ]:


from googletrans import Translator
translator = Translator()

print("*** *** *** *** *** *** *** *** *** *** *** ***")
print("Welcome to smartTrans")
print("I'm very simple to use, just enter the sentence you want to translate!!!")
print("To exit, just enter the word 'End'")
print("Good luck :)")
print("*** *** *** *** *** *** *** *** *** *** *** ***\n")

try:
    while True :
        print("*** *** *** *** *** *** *** *** *** *** *** ***")
        print("Detecting Language to translate to...")
        langTo = getCountryLang(getCountryCode())
        print("What language(lan code) you want to translate to? ( default is", langTo,"): ")
        languageToInput = input()
        if languageToInput.lower() == "end":
            raise StopIteration   
        elif langExists(languageToInput):
            langTo = languageToInput
        else:
            print("Will translate to", langTo, "!!!")
        langToString = getLangString(langTo)

        sentence = getSentence()
        print("*** *** ***")
        print("Detecting language...")
        detectedLanguage = translator.detect(sentence)
        langFrom = detectedLanguage.lang;
        langFromString = getLangString(langFrom)
        print("Detected language is", langFromString, "!!!")
        print("*** *** ***")
        
        try:
            while True :
                print("Translating to",langToString,"...")
                transText = doTranslate(translator, sentence, langFrom, langTo)
                print("*** *** ***")
                print("'" + sentence + "'", "in", langToString, "is:", transText)
                print("*** *** ***")

                words = getUniqueWords(sentence)
                
                #add suggested replies
                #classify words types
                
                if len(words) > 1:
                    englishSentence = doTranslate(translator, sentence, langFrom, "en")
                    print("This statement is" , getSentements(englishSentence))
                    print("*** *** ***")
                    for word in words:
                        wordTrans = doTranslate(translator, word, langFrom, langTo)
                        print("'" + word + "'", "in", langToString, "is:", wordTrans)
                    print("*** *** *** *** *** *** *** *** *** *** *** ***\n")
                sentence = getSentence()
        except StopIteration: pass
            
except StopIteration:
    print("See you :)")
except:
    print("Something went wrong !!!")
    print("Exiting...")

