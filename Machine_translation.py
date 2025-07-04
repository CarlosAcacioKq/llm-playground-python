#Automatically converst text from one language to another using computer algorithms.(google translate)
from translate import Translator

translator_es = Translator(to_lang='es') #Spanish
translator_ko = Translator(to_lang='ko') #Korean
translator_fr = Translator(to_lang='fr') #French
#text to be translated
text = 'Hello, how are you?'

#translate
translation_es = translator_es.translate(text)
translation_ko = translator_ko.translate(text)
translation_fr = translator_fr.translate(text)

print('Translated Text to Spanish:', translation_es)
print('Translated Text to Korean:', translation_ko)
print('Translated Text to French:', translation_fr)