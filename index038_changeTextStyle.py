"""
Kivy - Codemy.com #38 : How To Use Markup To Change Text Style - Python Kivy GUI Tutorial #38
Lien : https://www.youtube.com/watch?v=tJdQ8ZEDktE

Dans ce programme on apprend à utiliser dans le fichier .kv l'instruction markup qui permet de changer la mise en forme
des textes. Cette instruction est similaire à la mise en forme d'un texte en fichier .html mais les noms des fonctions
diffèrent :
-> balises ouvrantes et fermantes [b] : caractères en gras
-> balises ouvrantes et fermantes [i] : caractères en italique
-> balises ouvrantes et fermantes [color=#codeHexadecimal] : caractères en couleur
-> balises ouvrantes et fermantes [size=] : taille des caractères
-> balises ouvrantes et fermantes [u] : soulignement des caractères
-> balises ouvrantes et fermantes [s] : barre les caractères
-> balises ouvrantes et fermantes [font] : police d'écriture des caractères
-> balises ouvrantes et fermantes [sup] : caractères en haut
-> balises ouvrantes et fermantes [sub] : caractères en bas

L'avantage de cette méthode c'est qu'on peut sélectionner le mot pour lequel il y aura une mise en forme différentes que
les autres mots.

Éditeur : Laurent REYNAUD
Date : 12-02-2021
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script

Builder.load_file('index038_changeTextStyle.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv

    pass


class AwesomeApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on appelle la classe MyLayout() ci-dessus"""
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
