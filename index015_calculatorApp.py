"""
Kivy - Codemy.com #15 : Build A Simple Calculator App - Python Kivy GUI Tutorial #15
Lien : https://www.youtube.com/watch?v=Lu-HP4eOYM4&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=15

Dans ce programme on apprend à positionner uniquement les widgets pour la calculatrice et à effacer les chiffres saisis
en appuyant sur le bouton 'C'

Éditeur : Laurent REYNAUD
Date : 13-01-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script
from kivy.core.window import Window  # configuration de la taille de la fenêtre principale

"""Taille de la fenêtre principale"""
Window.size = (500, 700)

Builder.load_file('index015_calculatorApp.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv
    pass

    def clear(self):
        """Fonction permettant de réinitialiser les chiffres affichés en appuyant sur le bouton 'C'"""
        self.ids.calc_input.text = '0'


class CalculatriceApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on appelle la classe MyLayout() ci-dessus"""
        return MyLayout()


if __name__ == '__main__':
    CalculatriceApp().run()
