#import the Library
from translate  import Translator

#Create a translator object
translator = Translator(to_lang='es') #Spanish

#Choose a Phrase
text = 'Hello, how are you?'

#Translate
translation = translator.translate(text)

print('Translated Text:', translation)
