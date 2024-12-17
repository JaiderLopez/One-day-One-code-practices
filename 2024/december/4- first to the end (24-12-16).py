import string
#problem (copilot)
"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
Leave punctuation marks untouched.

Examples
    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !
"""

#What I think I gonna do
"""
to split the word and reverse the orden, then to add 'ay' at end
"""

#First implementation
"""
def pig_it(text):
    words = text.split(' ')
    text = ''
    for word in words:
        if not len(word) > 1:
            if word in string.punctuation:
                text += word + ' '
                continue
            text+= word + 'ay '
            continue
        text+= word[1:] + word[0] + 'ay '
    return text.strip()
"""

#clean code
def pig_it(text):
    words = text.split(' ')
    text = ''
    for word in words:
        text+= word+ ' ' if word in string.punctuation else ( word+ 'ay ' if len(word) <= 1 else word[1:] + word[0] + 'ay ')
    return text.strip()

print(pig_it('Pig latin is cool'))