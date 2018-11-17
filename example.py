# from googletrans import LANGUAGES
# import requests
# from collections import Counter
# from textblob import TextBlob
from googletrans import Translator

import SmartTrans

translator = Translator()

print("*** *** *** *** *** *** *** *** *** *** *** ***")
print("Welcome to smartTrans")
print("I'm very simple to use, just enter the sentence you want to translate!!!")
print("To exit, just enter the word 'End'")
print("Good luck :)")
print("*** *** *** *** *** *** *** *** *** *** *** ***\n")

try:
    while True:
        print("*** *** *** *** *** *** *** *** *** *** *** ***")
        print("Detecting Language to translate to...")
        langTo = getCountryLang(getCountryCode())
        print("What language(lan code) you want to translate to? ( default is", langTo, "): ")
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
            while True:
                print("Translating to", langToString, "...")
                transText = doTranslate(translator, sentence, langFrom, langTo)
                print("*** *** ***")
                print("'" + sentence + "'", "in", langToString, "is:", transText)
                print("*** *** ***")

                words = getUniqueWords(sentence)

                # add suggested replies
                # classify words types

                if len(words) > 1:
                    englishSentence = doTranslate(translator, sentence, langFrom, "en")
                    print("This statement is", getSentements(englishSentence))
                    print("*** *** ***")
                    for word in words:
                        wordTrans = doTranslate(translator, word, langFrom, langTo)
                        print("'" + word + "'", "in", langToString, "is:", wordTrans)
                    print("*** *** *** *** *** *** *** *** *** *** *** ***\n")
                sentence = getSentence()
        except StopIteration:
            pass

except StopIteration:
    print("See you :)")
except:
    print("Something went wrong !!!")
    print("Exiting...")
