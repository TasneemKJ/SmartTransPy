from SmartTrans import SmartTrans 

print("*** *** *** *** *** *** *** *** *** *** *** ***")
print("Welcome to smartTrans")
print("I'm very simple to use, just enter the sentence you want to translate!!!")
print("To exit, just enter the word 'End'")
print("Good luck :)")
print("*** *** *** *** *** *** *** *** *** *** *** ***\n")

smartTranslator = SmartTrans()

try:
    while True:
            print("*** *** *** *** *** *** *** *** *** *** *** ***")
            print("Detecting Language to translate to...")
            langTo = smartTranslator.getCountryLang(smartTranslator.getCountryCode())
            print("What language(lan code) you want to translate to? ( default is", langTo, "): ")
            languageToInput = input()
            if languageToInput.lower() == "end":
                raise StopIteration
            elif smartTranslator.langExists(languageToInput):
                langTo = languageToInput
            else:
                print("Will translate to", langTo, "!!!")
            langToString = smartTranslator.getLangString(langTo)
    
            sentence = smartTranslator.getSentence()
            print(sentence)
            print("*** *** ***")
            print("Detecting language...")
            detectedLanguage = smartTranslator.detectLanguage(sentence)
            langFrom = detectedLanguage.lang
            langFromString = smartTranslator.getLangString(langFrom)
            print("Detected language is", langFromString, "!!!")
            print("*** *** ***")
    
            try:
                while True:
                    print("Translating to", langToString, "...")
                    transText = smartTranslator.doTranslate(sentence, langFrom, langTo)
                    print("*** *** ***")
                    print("'" + sentence + "'", "in", langToString, "is:", transText)
                    print("*** *** ***")
    
                    words = smartTranslator.getUniqueWords(sentence)
    
                    # add suggested replies
                    # classify words types
    
                    if len(words) > 1:
                        englishSentence = smartTranslator.doTranslate(sentence, langFrom, "en")
                        print("This statement is", smartTranslator.getSentements(englishSentence))
                        print("*** *** ***")
                        for word in words:
                            wordTrans = smartTranslator.doTranslate(word, langFrom, langTo)
                            print("'" + word + "'", "in", langToString, "is:", wordTrans)
                        print("*** *** *** *** *** *** *** *** *** *** *** ***\n")
                    sentence = smartTranslator.getSentence()
            except StopIteration:
                pass       
except StopIteration:
    print("See you :)")
except:
    print("Something went wrong !!!")
    print("Exiting...")
