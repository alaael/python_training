#-*- coding: utf8-*-
'''module cap'''

from __future__ import print_function
from __future__ import unicode_literals

class Paragraphe(unicode):
    '''add cap and iscap methods to str'''
    def cap(self):
        ''' ceci est une chaine. une simple chaine ->  Ceci est une chaine. Une simple chaine'''
        if '.' not in self:
            return self.lstrip().capitalize().rjust(len(self))
        else:
            return '.'.join([Paragraphe(e).cap() for e in self.split('.')])

    def iscap(self):
        '''paragraphe == paragraphe.cap() -> True'''
        return self == self.cap()


if __name__ == '__main__':
    paragraphe1 = Paragraphe('ceci est une chaine. une simple chaine de caractères')
    print(paragraphe1.cap())
    print(paragraphe1.iscap())
