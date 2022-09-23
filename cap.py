#-*- coding: utf8-*-
'''module cap'''


class Paragraphe(str):
    '''add cap and iscap methods to str'''
    def cap(self):
        ''' ceci est une chaine. une simple chaine ->  Ceci est une chaine. Une simple chaine'''
        phrases = self.split('.') 
        for indice, phrase in enumerate(phrases):
            phrase_ = phrase.lstrip()
            phrase_ = phrase_.capitalize()
            phrase_ = phrase_.rjust(len(phrase))
            phrases[indice] = phrase_
        return Paragraphe('.'.join(phrases))

    def iscap(self):
        '''paragraphe == paragraphe.cap() -> True'''
        return self == self.cap()


def main():
    paragraphe1 = Paragraphe('ceci est une chaine. une simple chaine de caractères')
    print(paragraphe1.cap())
    print(paragraphe1.iscap())

if __name__ == '__main__':
    main()
