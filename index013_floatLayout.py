"""
Kivy - Codemy.com #13 : Kivy Float Layout - Python Kivy GUI Tutorial #13
Lien : https://www.youtube.com/watch?v=9DaVDNP-NOM&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=13

Dans ce programme on apprend à disposer les widgets dans la fenêtre principale (en haut à droite, en bas à gauche...)

Éditeur : Laurent REYNAUD
Date : 13-01-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script

Builder.load_file('index013_floatLayout.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


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
