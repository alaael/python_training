#-*- coding: utf8-*-
'''module age'''

from __future__ import print_function
from __future__ import unicode_literals
from datetime import date

class Personne(object):
    '''class Personne'''
    def __init__(self, nom, prenom, *naissance):
        self.nom = nom
        self.prenom = prenom
        self.naissance = date(*naissance)

    @property
    def age(self):
        '''return the age of personne'''
        aujourdhui = date.today()
        try:
            anniversaire = self.naissance.replace(year=aujourdhui.year)
        except ValueError:
            anniversaire = self.naissance.replace(year=aujourdhui.year,day=28)
        age = aujourdhui.year - self.naissance.year
        if anniversaire<aujourdhui:
            age -= 1
        return age

if __name__ == '__main__':
    personne1 = Personne('nom1', 'prenom1', 1980, 2, 29)
    print(personne1.age)
